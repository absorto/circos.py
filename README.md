circos.py
=========

Galaxy tool conf
----------------

Placing the galaxy_circos.xml within reach of a tools_conf.xml gives
you access to a convenient Galaxy Tool for generating Circos Plots.
The script plot.py was actually created for this wrapper.

For the time being you must manually set up circos and its
dependencies. Then you must set the proper path to the circos
executable in the galaxy_circos.xml file.

Not all features are accesible, but it's good enough for a lot of
uses. If you need full control, you can't have an easy frontend! :-D


plot.py
-------

The script *plot.py* provides a command line interface for the creation of Circos Plot conf files.

    usage: plot.py [-h] --output OUTPUT --circos_path CIRCOS_PATH --karyotype
                   KARYOTYPE --cytobands {true,false} [--chromosomes CHROMOSOMES]
                   [--links [LINKS [LINKS ...]]]
                   [--links_colors [LINKS_COLORS [LINKS_COLORS ...]]]
                   [--links_radius LINKS_RADIUS]
                   [--links_bezier_radius LINKS_BEZIER_RADIUS]
                   [--tracks [TRACKS [TRACKS ...]]]
                   [--types [{histogram,line,scatter,heatmap} [{histogram,line,scatter,heatmap} ...]]]
                   [--orientations [{in,out} [{in,out} ...]]]
                   [--extend_bins [{yes,no} [{yes,no} ...]]] [--r0 [R0 [R0 ...]]]
                   [--r1 [R1 [R1 ...]]]
                   [--tracks_colors [TRACKS_COLORS [TRACKS_COLORS ...]]]
    
    Generate a Circos Plot configuration set and run circos on it.
    
    optional arguments:
      -h, --help            show this help message and exit
      --output OUTPUT       absolute path to output file
      --circos_path CIRCOS_PATH
                            absolute path to circos command
      --karyotype KARYOTYPE
                            absolute path to karyotype file
      --cytobands {true,false}
                            display cytobands
      --chromosomes CHROMOSOMES
                            select chromosomes to plot
      --links [LINKS [LINKS ...]]
                            absolute paths to links data files
      --links_colors [LINKS_COLORS [LINKS_COLORS ...]]
      --links_radius LINKS_RADIUS
      --links_bezier_radius LINKS_BEZIER_RADIUS
      --tracks [TRACKS [TRACKS ...]]
                            absolute paths to tracks data files
      --types [{histogram,line,scatter,heatmap} [{histogram,line,scatter,heatmap} ...]]
      --orientations [{in,out} [{in,out} ...]]
      --extend_bins [{yes,no} [{yes,no} ...]]
      --r0 [R0 [R0 ...]]
      --r1 [R1 [R1 ...]]
      --tracks_colors [TRACKS_COLORS [TRACKS_COLORS ...]]



