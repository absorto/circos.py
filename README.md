circos.py
=========

Easier frontend for a set of Circos Plot features.


     usage: plot.py [-h] --circos_path CIRCOS_PATH --path PATH 
     	    	    --karyotype KARYOTYPE 
		    [--links [LINKS [LINKS ...]]]
                    [--links_colors [LINKS_COLORS [LINKS_COLORS ...]]]
                    [--links_radius LINKS_RADIUS]
                    [--links_bezier_radius LINKS_BEZIER_RADIUS]
                    [--tracks [TRACKS [TRACKS ...]]]
                    [--types [{histogram,line,scatter,heatmap} [{histogram,line,scatter,heatmap} ...]]]
                    [--orientations [{in,out} [{in,out} ...]]] [--r0 [R0 [R0 ...]]]
                    [--r1 [R1 [R1 ...]]]
                    [--tracks_colors [TRACKS_COLORS [TRACKS_COLORS ...]]]
     
     Generate a Circos Plot configuration set and run circos on it.
     
     optional arguments:
       -h, --help            show this help message and exit
       --circos_path CIRCOS_PATH
                             absolute path to circos command
       --path PATH           path to a working directory
       --karyotype KARYOTYPE
                             absolute path to karyotype file
       --links [LINKS [LINKS ...]]
                             absolute paths to links data files
       --links_colors [LINKS_COLORS [LINKS_COLORS ...]]
       --links_radius LINKS_RADIUS
       --links_bezier_radius LINKS_BEZIER_RADIUS
       --tracks [TRACKS [TRACKS ...]]
                             absolute paths to tracks data files
       --types [{histogram,line,scatter,heatmap} [{histogram,line,scatter,heatmap} ...]]
       --orientations [{in,out} [{in,out} ...]]
       --r0 [R0 [R0 ...]]
       --r1 [R1 [R1 ...]]
       --tracks_colors [TRACKS_COLORS [TRACKS_COLORS ...]]
