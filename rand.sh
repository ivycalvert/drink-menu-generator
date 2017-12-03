# clears out the outputs file ready for the final image
mkdir -p outputs
rm -rf outputs/*

# finds random editedBeer image and moves it to outputs folder
find final -type f | gshuf -n 1 | xargs -I{} cp "{}" outputs/ 

#renames the new image to match the name the inDesign file is looking for
mv outputs/*.jpg outputs/final_beer.jpg