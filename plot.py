#!/usr/bin/env python



import pprint
import argparse
import sys, os, shutil


from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))



parser = argparse.ArgumentParser(description='Generate a Circos Plot configuration set')
parser.add_argument('--path', required=True, help="path to a working directory")
parser.add_argument('--karyotype', type=argparse.FileType('r'), required=True )
parser.add_argument('--links',  type=argparse.FileType('r'), required=True )



if __name__ == '__main__':
    args      = parser.parse_args()
    karyotype = args.karyotype
    links     = args.links
    path      = args.path


    # maybe sanity check on input files?
    karyotype_path = karyotype.name
    karyotype.close()
    
    links_path = links.name
    links.close()

    # create directory for templates
    os.makedirs(path)    

    shutil.copy('templates/bands.conf', path )
    shutil.copy('templates/ideogram.conf', path )
    shutil.copy('templates/ideogram.label.conf', path )
    shutil.copy('templates/ideogram.position.conf', path )


    with open( path + '/circos.conf', 'w') as f:
        circos_conf = env.get_template('circos.conf')
        f.write( circos_conf.render( # citation_depth = data_path+'/citation_depth_'+str(year)+'.tsv',
                                     links     = links_path,
                                     karyotype = karyotype_path  ) )
