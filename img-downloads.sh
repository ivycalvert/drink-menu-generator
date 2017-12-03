# download images

#!/bin/bash

# show commands and stop if there is an error
set -ex

mkdir -p beer




# build the url
URL='https://www.flickr.com/photos/tigerphotostock/albums/72157647605404468'

# fetch the images
# plz note: this page causes error when downlong and using the 'accept=*.jpg' command
# so as a work around, the reject and rm commands are used to clean the scraped content
wget \
  --adjust-extension \
  --no-directories \
  --convert-links \
  --backup-converted \
  --random-wait \
  --limit-rate=100k \
  --span-hosts \
  --directory-prefix=beer \
  --page-requisites \
  --timestamping \
  --execute robots=off \
  --reject=*.png,*.svg,*.eot,*.ttf,*.woff,*.css,*.js,*.ico,*.orig \
  $URL

# change directory to remove all remaining file types that are not jpg
cd beer
shopt -s extglob
rm !(*.jpg)
