#imports
import re
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#Use for DLC later
LEVELS = [10]

QUEST_NAMES = [
    # Suburbs
    "Robot Repair",
    "Programmed for Protection",
    "Pie for the Putterpam",
    "The Patriot's Party",
    "These Tombstones Aren't Styrofoam",
    "Suburbs Bobbing for Apples",
    "Auburn Pines Hide 'n' Seek",
    "This Card Is So Rare",
    "Suburbs Collect 'em All",

    # Autumn Haven Mall
    "Tickets for Treats",
    "Earn Your Monster Slayer Badge",
    "The Mall-O-Rail is Broken",
    "The Dark Side of the Mall",
    "Extreme Costume Challenge!",
    "This Card Is Rarer",
    "Mall Collect 'em All",
    "Mall Bobbing for Apples",
    "Mall Hide 'n' Seek",

    # Fall Valley
    "The Original Costume Quest",
    "All's Fair That Ends Fare",
    "Children of the High Fructose Corn Syrup",
    "Fall Valley Hide 'n' Seek",
    "Fall Valley Bobbing for Apples",
    "This Card Is The Rarest",
    "Fall Valley Collect 'em All"
]

COSTUME_NAMES = [
    "Robot",
    "Knight",
    "Statue of Liberty",
    "Space Warrior",
    "Ninja",
    "Unicorn",
    "Pumpkin",
    "Vampire",
    "French Fries",
    "Black Cat",
    "Grubbin"
]

CARD_NAMES = [
    "Raz-Ums",
    "Glop",
    "Wobblers",
    "Choconana",
    "Shimmerfizz",
    "Chunkwutter",
    "Candy Hair",
    "Moops",
    "Chocolate Carrot",
    "Fuds",
    "Sweet Tooth",
    "Jammie Jams",
    "Lollopops",
    "Fruity Foam",
    "Swedish Noses",
    "Box Cake",
    "Gooz",
    "Fee-Fi-Fo-Fudge",
    "Slime Beetles",
    "Sour Feet",
    "Fish Head",
    "Gummy Water",
    "Licorice Cables",
    "Cinnamon Brain",
    "Mossy Log",
    "Wood Chips",
    "Pizza Sundae",
    "Sweet Fat",
    "Pimples",
    "Frozen Butter",
    "Edible Hat",
    "Sludge",
    "Coffee Toffee Taffee",
    "Banana Beard",
    "Broccoli Wafers",
    "Gingerbread Ham",
    "Mice Crispy Treat",
    "Jaw Hurters",
    "Blobbles",
    "Barf Roll-Ups",
    "Chocolate Hamburger",
    "Clippingz",
    "Salmon Rings",
    "Street Chews",
    "Fried Popcorn",
    "Coconuts & Bolts",
    "Jelly Has-Beens",
    "Unicorn Pellets",
    "Misfortune Cookie",
    "Sugar Bucket",
    "Old Lady Fingers",
    "Boogie Pie",
    "Human Crackers",
    "Gloop"
]

BATTLE_STAMP_NAMES = [
    "Fang of the Wolf",
    "Black Cat",
    "Moving Tombstone",
    "Egg",
    "Disembodied Hand",
    "Pumpkin Guts",
    "Screaming Spider",
    "Bloodshot Eyeballs",
    "Toilet Paper",
    "One-Eyed Vampire Bat",
    "Witch's Brew",
    "Jawbone of the Wolf",
    "Albino Black Cat",
    "Banshee",
    "Flying Tombstone",
    "Rotten Egg",
    "Disembodied Six Fingered Hand",
    "Moldy Pumpkin Guts",
    "Yodeling Black Widow",
    "2-Ply Toilet Paper",
    "Headless Banshee",
    "Vegetarian Witch's Brew",
    "No-Eyed Vampire Bat",
    "Bowl of Bloodshot Eyeballs"
]