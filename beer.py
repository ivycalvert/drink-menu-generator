import json
import random
import os
import tracery
from random import randint
from tracery.modifiers import base_english

# save outputs to file
beerDes = open("fields.tsv", "w")
# types_file = open("types.txt")

# put your grammar here as the value assigned to "rules"
# "origin" to have enough sentence options to create variance in the generated content
rules = {
# sentences for print
    "name":["#mood.capitalize# #colour.capitalize# #anim.capitalize#"],
    "style":["#descript.capitalize# #beer#.", "#wine.capitalize# #beer#.", "#mood.capitalize# #beer#."],
    "origin":["A #mood# flavour with subtle undertones of #herbs# and #spices#. Distilled from handgrown #fruit# and combined with the #wine# flavours of spring water from the #loc# mountain range. Part beer you need, and all beer you desire.",
        "Let this beverage be the #vehicle# to your #wish#. One #swig# will have you feeling like #people# #day#!"],
    "flavour":["#fruit.capitalize#, #herbs#, and subtle undertones of #spices#."],
    "pairing":["A #small# side of #food#, with a #hipster#."],
    "serving":["Best experienced #temp#, garnished with a fine sprig of #herbs#."],
# rules
    "vehicle":["jetplane", "ferrari", "limousine", "Bentley", "Audi"],
    "swig":["mouthful", "glass", "sip", "swig", "gulp", "bottle", "taste"],
    "day":["on a summer evening", "after recieving a paycheck", "relaxing in a private jet", "after avoiding a paparazzi scandle"],
    "colour":["Blue", "Black", "Green", "Eggplant", "Lavender", "Peach", "Blush", "Crimson"],
    "wish":["deepest desires", "wildest dreams", "yearning", "darkest dreams", "deepest wishes"],
    "small":["delicate", "tender", "precise"],
    "temp":["at room temperature", "ice cold", "freshly boiled", "lukewarm", "chilled", "cold", "warmed", "warm", "stale"],
    "hipster":["humble dash of good looks", "finely brewed coffee made from imported beans", "an even smaller dose of gluten"]
}

# load in the json data from files downloaded from corpora project
beer_styles = json.loads(open("downloads/beer_styles.json").read())
colours = json.loads(open("downloads/paints.json").read())
fruit = json.loads(open("downloads/fruits.json").read())
herb_spices = json.loads(open("downloads/herbs_n_spices.json").read())
mood = json.loads(open("downloads/moods.json").read())
wine = json.loads(open("downloads/wine_descriptions.json").read())
description = json.loads(open("downloads/descriptions.json").read())
drunk = json.loads(open("downloads/states_of_drunkenness.json").read())
location = json.loads(open("downloads/winds.json").read())
food = json.loads(open("downloads/menuItems.json").read())
people = json.loads(open("downloads/celebrities.json").read())
animal = json.loads(open("downloads/common.json").read())

# set values for the variables data from downloaded files
rules["beer"] = beer_styles["beer_styles"]
# rules["colour"] = colours["colors"] # revisit this one
rules["fruit"] = fruit["fruits"]
rules["herbs"] = herb_spices["herbs"]
rules["spices"] = herb_spices["spices"]
rules["mood"] = mood["moods"]
rules["wine"] = wine["wine_descriptions"]
rules["descript"] = description["descriptions"]
rules["drunk"] = drunk["states_of_drunkenness"]
rules["loc"] = location["winds"] # loc is actually wind names currently, fix later
rules["food"] = food["menuItems"]
rules["people"] = people["celebrities"]
rules["anim"] = animal["animals"]


grammar = tracery.Grammar(rules) # create a grammar object from the rules
grammar.add_modifiers(base_english) # add pre-programmed modifiers

# create multiple versions of the text
#
print("beer\t", (grammar.flatten("#name#")), file=beerDes)
print("blurb\t", (grammar.flatten("#origin#")), file=beerDes)
print("flavour\t", (grammar.flatten("#flavour#")), file=beerDes)
print("pairing\t", (grammar.flatten("#pairing#")), file=beerDes)
#GENERATE RANDOM YEAR FOR THE 'FIRST BREWED'
randYear = str(randint(1900, 2017))
print("year\t", randYear, file=beerDes)
#GENERATE RANDOM NUMBER FOR PERCENTAGE
print("style\t", (grammar.flatten("#style#")), file=beerDes)
randNum = str(randint(1, 25))
print("alcohol\t", randNum, "%", file=beerDes)
#print("----------", file=beerDes)
print("serving\t", (grammar.flatten("#serving#")), file=beerDes)



