#!/bin/bash

# this happens once

wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/colors/paints.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/beer_styles.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/fruits.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/herbs_n_spices.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/wine_descriptions.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/humans/moods.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/humans/descriptions.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/words/states_of_drunkenness.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/geography/winds.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/menuItems.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/humans/celebrities.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/animals/common.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/geography/countries.json
wget --directory-prefix=downloads https://raw.githubusercontent.com/dariusk/corpora/master/data/plants/flowers.json

brew install coreutils