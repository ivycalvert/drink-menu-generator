GENERATE A BEER PAGE:

EITHER RUN THE MASTER SCRIPT run_all.sh (ONLY ONE PAGE IS GENERATED PER RUN THROGUH):

  $ bash run_all.sh

OR ALTERNATIVELY RUN THE SCRIPTS INDIVIDUALLY IN THE FOLLOWING ORDER:

1) first run download.sh this will collect all external json data sets we need and install additional tools if not already installed:

  $ bash download.sh

2) then run img-download.sh to download all the images of beer required:

  $ bash img-downloads.sh

3) then run beer.py:

  $ python beer.py

This will:

 * generate details about a fictional beer
 * print these details out into a tsv file for later use

4) then run resizeBeer.sh:

  $ bash resizeBeer.sh

This will:

 * resize the downloaded beer images to the required size

5) then run editBeer.sh:

  $ bash editBeer.sh

This will:

 * add text to the beer images

6) then run rand.sh:
NOTE: IT IS IMPORTANT THIS STEP IS COMPLETED AFTER THE TWO PREVIOUS STEPS 
	
  $ bash rand.sh

This will:
 
 * select a random edited beer image, moving and renaming it ready for the automation process

7) then run gen_beer.py:

  $ python gen_beer.py

This will:

 * Automate the process of inputting the beer details and image into the idml template page
 * This will generate a final page with the name 'beer.idml' 



! IF YOU WISH TO GENERATE MORE PAGES, FIRST SAVE THE BEER.IDML FILE UNDER A DIFFERENT NAME
! THEN REPEAT STEPS 3 THROUGH TO 7 AS MANY TIMES AS PREFERED, EACH TIME AFTER RUNNING STEP 7
! THE OUTPUT 'BEER.IDML' FILE WILL NEED TO BE SAVED UNDER A NEW NAME OR THIS FILE WILL BE
! OVERWRITTEN