import json
import random
import os
import tracery
from random import randint
from tracery.modifiers import base_english


# save outputs to file
wineDes = open("wines.tsv", "w")
# types_file = open("types.txt")

# put your grammar here as the value assigned to "rules"
# "origin" to have enough sentence options to create variance in the generated content
rules = {
# sentences for print
    "name":["#mood.capitalize# #label.capitalize#"],
    "style":["#body.capitalize# #colour[label:#type#]#"],
    "origin":["Made from grapes grown in lavish vinyards in #loc#. A fine taste that #des#."],
    "flavour":["A fine #savoury# wine that holds #fruit-forward# flavours."],
    "pairing":["A #small# side of #food# to emphasize the #finish# of the wine."],
    "serving":["Best experienced #temp# with the #scent# scent of #flower# in the air."],
# rules
    "type":["riesling", "gewurztraminer", "chardonnay", "sauvignon blanc", "syrah", "merlot", "cabernet sauvignon", "pinot noir", "zinfandel", "pinot gris", "malbec", "pinot blanc", "rose", "sherry"],
    "colour":["red", "white"],
    "fruit-forward":["fruit-driven", "sweet attack", "jammy", "extracted", "flamboyant", "sweet tannin", "juicy", "ripe", "fruit-forward", "tart", "mellow", "soft"],
    "savoury":["savoury", "herbaceous", "earthy", "rustic", "food friendly", "bone dry", "elegant", "closed", "vegetal", "stalky", "stemmy", "high minerality"],
    "des":["holds no residual suger, accompanied by the presence of astringency", 
        "situates in the mouth like a delicate unsweetened iced green tea or a refreshing lemonade", 
        "teases out a long aftertaste that tingles on the tongue",
        "fills the palate with rich texture and intensity",
        "is light in body, and even lighter on the palatte",
        "common in oak-aged wines",
        "is very common in wines from cool climate growing regions",
        "should be considered a great quality",
        "containing an amazing flavour combination when paired with rich fatty foods",
        "has a bouquet of complex aromas",
        "is as if childhood summers in Provence have been taken and placed inside a glass",
        "is worth the price"],
    "body":["light bodied", "medium bodied", "full bodied"],
    "small":["delicate", "tender", "precise"],
    "finish":["smooth finish", "tart finish", "sweet tannin finish", "smoky sweet finish", "spicy finish", "bitter finish"],
    "temp":["at room temperature", "ice cold", "freshly boiled", "lukewarm", "chilled", "cold", "warmed", "warm", "stale"],
    "scent":["fine", "crisp", "rich", "sharp"]
}

# load in the json data from files downloaded from corpora project
fruit = json.loads(open("downloads/fruits.json").read())
mood = json.loads(open("downloads/moods.json").read())
wine = json.loads(open("downloads/wine_descriptions.json").read())
food = json.loads(open("downloads/menuItems.json").read())
loc = json.loads(open("downloads/countries.json").read())
flowers = json.loads(open("downloads/flowers.json").read())

# set values for the variables data from downloaded files
rules["fruit"] = fruit["fruits"]
rules["mood"] = mood["moods"]
rules["wine"] = wine["wine_descriptions"]
rules["loc"] = loc["countries"] 
rules["food"] = food["menuItems"]
rules["flower"] = flowers["flowers"]


grammar = tracery.Grammar(rules) # create a grammar object from the rules
grammar.add_modifiers(base_english) # add pre-programmed modifiers

# create multiple versions of the text
for i in range(12):
    print("NAME: ", (grammar.flatten("#name#")), file=wineDes)
    print("STYLE: ", (grammar.flatten("#style#"))), file=wineDes)
    print("DESCRIPTION: ", file=wineDes)
    print((grammar.flatten("#origin#")), file=wineDes)
    print("PAIRING: ", (grammar.flatten("#pairing#")), file=wineDes)
    print("FLAVOUR: ", (grammar.flatten("#flavour#")), file=wineDes)
    print("SERVING: ", (grammar.flatten("#serving#")), file=wineDes)

    #GENERATE RANDOM YEAR FOR THE 'FIRST BREWED'
    randYear = str(randint(1900, 2017))
    print("FIRST BREWED IN: ", randYear, file=wineDes)

    #GENERATE RANDOM NUMBER FOR PERCENTAGE
    randNum = str(randint(1, 25))
    print("ALCOHOL PERCENT: ", randNum, "%", file=wineDes)
    print("----------", file=wineDes)
