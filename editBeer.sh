#!/bin/bash

# show commands and stop if there is an error
set -ex

# make a final directory of the final edited beer images
mkdir -p final

# clears out the file ready for the final image
rm -rf final/*

# copy the resized images into the new directory ready for editing
# this seperates out the processes, so if taking a step bask is 
# wanted, the images are organised 
cp -r resized/. final

# add text onto the images
cd final
convert *.jpg \
  -pointsize 70 \
  -stroke '#000c' \
  -strokewidth 2 \
  -annotate +20+1100 'How Beer is Supposed \nto Be.' \
  -stroke none \
  -fill white \
  -annotate +20+1100 'How Beer is Supposed \nto Be.' \
  final_beer.jpg

# a taste like no other

# removes all the images without the text 
shopt -s extglob
rm !(final_beer*.jpg)
