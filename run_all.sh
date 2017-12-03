# a basic run all script which, once run once
# will generate an inDesign template named
# 'beer.idml' which will have all information
# filled out for a 'beer' page in the book

bash download.sh
bash img-downloads.sh
python beer.py
bash resizeBeer.sh
bash editBeer.sh
bash rand.sh
python gen_beer.py