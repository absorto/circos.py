#!/usr/bin/env python



import pprint
import argparse
import sys, os, shutil, tempfile
import subprocess

from jinja2 import Environment, FileSystemLoader




parser = argparse.ArgumentParser(description='Generate a Circos Plot configuration set and run circos on it.')
parser.add_argument('--output', type=argparse.FileType('w'), required=True, help="absolute path to output file" )
parser.add_argument('--circos_path', required=True, help="absolute path to circos command")
parser.add_argument('--karyotype', type=argparse.FileType('r'), required=True, help="absolute path to karyotype file" )
parser.add_argument('--cytobands', required=True, choices=['true','false'], help="display cytobands")
parser.set_defaults(cytobands=False)
parser.add_argument('--chromosomes', required=False, help="select chromosomes to plot")
# links
parser.add_argument('--links',  type=argparse.FileType('r'), required=False, nargs='*', help="absolute paths to links data files"  )
parser.add_argument('--links_colors', required=False, nargs='*')
parser.add_argument('--links_radius', required=False)
parser.add_argument('--links_bezier_radius', required=False)
# tracks
parser.add_argument('--tracks', type=argparse.FileType('r'), required=False, nargs='*', help="absolute paths to tracks data files" )
parser.add_argument('--types', required=False, nargs='*', choices=['histogram', 'line', 'scatter','heatmap'])
parser.add_argument('--orientations', required=False, nargs='*', choices=['in', 'out'])
parser.add_argument('--extend_bins', required=False, nargs='*', choices=['yes','no'])
parser.add_argument('--r0', required=False, nargs='*')
parser.add_argument('--r1', required=False, nargs='*')
parser.add_argument('--tracks_colors', required=False, nargs='*')


if __name__ == '__main__':
    args       = parser.parse_args()
    output     = args.output.name
    circos_path = args.circos_path
    karyotype  = args.karyotype
    if args.cytobands == 'true':
        cytobands = True
    else:
        cytobands = False
    chromosomes = args.chromosomes

    links      = args.links
    links_colors = args.links_colors
    links_radius = args.links_radius
    links_bezier_radius = args.links_bezier_radius

    tracks     = args.tracks
    radii0     = args.r0
    radii1     = args.r1
    tracks_colors     = args.tracks_colors
    types      = args.types
    orientations = args.orientations
    extend_bins = args.extend_bins

    # maybe sanity check on input files?
    karyotype_path = karyotype.name
    karyotype.close()
    
    if links:
        l = list()
        for n in range(0,len(links)):
            l.append({'path': links[n].name,
                      'color': links_colors[n]})
    else:
        l = None


    if tracks:
        t = list()
        for n in range(0,len(tracks)):                      
            t.append({'path': tracks[n].name,
                      'type': types[n],
                      'color': tracks_colors[n],
                      'r0': "%sr" % radii0[n],
                      'r1': "%sr" % radii1[n],
                      'extend_bin': extend_bins[n],
                      'orientation': orientations[n] })
    else:
        t = None
    
    # create temp directory for templates and plot
    path = tempfile.mkdtemp( prefix='circos-' )
    plotpath = os.path.dirname(sys.argv[0])
    env = Environment(loader=FileSystemLoader(plotpath + '/templates'))

    # create conf file from template
    with open( path + '/circos.conf', 'w') as f:
        circos_conf = env.get_template('circos.conf')
        f.write( circos_conf.render( links        = l,
                                     links_radius = "%sr" % links_radius,
                                     links_bezier_radius = "%sr" % links_bezier_radius,
                                     tracks       = t,
                                     karyotype    = karyotype_path,
                                     cytobands    = cytobands,
                                     chromosomes  = chromosomes ) )



    os.chdir(path)
    p = subprocess.Popen(circos_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()

    shutil.copy( path + "/circos.png", output )
#    if os.path.exists( path ):
#        shutil.rmtree( path )    
