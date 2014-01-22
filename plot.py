#!/usr/bin/env python



import pprint
import argparse
import sys, os, shutil


from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))



parser = argparse.ArgumentParser(description='Generate a Circos Plot configuration set')
parser.add_argument('--path', required=True, help="path to a working directory")
parser.add_argument('--karyotype', type=argparse.FileType('r'), required=True )
parser.add_argument('--links',  type=argparse.FileType('r'), required=False )
parser.add_argument('--tracks', type=argparse.FileType('r'), required=False, nargs='*')
parser.add_argument('--types', required=False, nargs='*', choices=['histogram', 'line', 'scatter','heatmap'])
parser.add_argument('--orientations', required=False, nargs='*', choices=['in', 'out'])
parser.add_argument('--r0', required=False, nargs='*')
parser.add_argument('--r1', required=False, nargs='*')
parser.add_argument('--colors', required=False, nargs='*')


if __name__ == '__main__':
    args       = parser.parse_args()
    karyotype  = args.karyotype
    links      = args.links
    path       = args.path
    tracks     = args.tracks
    radii0     = args.r0
    radii1     = args.r1
    colors     = args.colors
    types      = args.types
    orientations = args.orientations

    # maybe sanity check on input files?
    karyotype_path = karyotype.name
    karyotype.close()
    
    if links:
        links_path = links.name
        links.close()
    else:
        links_path = None

    if tracks:
        hist = list()
        for n in range(0,len(tracks)):
            hist.append({'path': tracks[n].name,
                         'type': types[n],
                         'color': colors[n],
                         'r0': "%sr" % radii0[n],
                         'r1': "%sr" % radii1[n],
                         'orientation': orientations[n] })
    else:
        hist = None


    pprint.pprint(hist)
    # create directory for templates
    os.makedirs(path)    

    # shutil.copy('templates/bands.conf', path )
    shutil.copy('templates/ideogram.conf', path )
    # shutil.copy('templates/ideogram.label.conf', path )
    # shutil.copy('templates/ideogram.position.conf', path )


    with open( path + '/circos.conf', 'w') as f:
        circos_conf = env.get_template('circos.conf')
        f.write( circos_conf.render( links      = links_path,
                                     tracks     = hist,
                                     karyotype  = karyotype_path  ) )
