ffmpeg and imagemagick
##########################

ffmpeg
=========
Cheatsheet
------------
.. code:: bash

    -pattern_type glob -i 'raw/*.png'  # repeat this to combine more than one pattern
    -loop -1  # for GIFs; number of times a gif plays; -1==infinite
    -r 1.5  # framerate
    -framerate 1.5  # same as -r


From images
------------
.. code:: bash

    ffmpeg -r 1.0 -i 'prefix_%04d.png' raw.gif  
    ffmpeg -r 1.0 -pattern_type glob -i '*.png' raw.gif  
    # problem: all images will be resized to the size of the first one (distortion)
    # solution: use imagemagick
    # problem2: low quality. 
    # solution2: use palette (see below)

    ffmpeg -r 0.5 -pattern_type glob -i '*.png' -c:v libx264 -pix_fmt yuv420p out.mp4
    # problem: all images will be resized to the size of the first one (distortion)
    # solution: use imagemagick

    ffmpeg -i prefix_%02d.png -vf "palettegen" palette.png
    ffmpeg -i prefix_%02d.png -i palette.png -filter_complex "paletteuse" output.gif

Imagemagick
===============
Cheatsheet
------------
.. code:: bash

    -delay 100  # hundreds of a sec
    -loop 5
    -dispose previous  # remove previous frame in the animation
    -gravity center  # center images
    -thumbnail 000x000  # resize image
    -extent 000x000  # adjust the image in a frame of this size

Examples
----------
.. code:: bash

    mogrify -geometry 640x480^ -gravity center -crop 640x480+0+0 *.png
    # force all images do to be 640x480. If bigger, cropped from the center

    mogrify -thumbnail 640x480 -background black -gravity center -extent 640x480 *.png
    # pad with black background

    convert -delay 200 -loop 5 -dispose previous *.png -gravity center iamanimating.gif
    # also creates a gif animation
