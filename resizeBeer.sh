#!/bin/bash

# show commands and stop if there is an error
set -ex

# making a new directory for the resized images to export to
mkdir -p resized

# this command resizes the beer images to portrait images that will fit within the 
# area set in the inDesign document for the beer photo
mogrify \
  -path resized/ \
  -background black \
  -gravity center \
  -crop 271x443+0+0 \
  -resize 300% \
  'beer/*.jpg'

