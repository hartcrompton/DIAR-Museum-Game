﻿#variables
#default vs define
#default variables are meant to be CHANGEABLE. The value is stored in save files.
#define variables are meant to be CONSTANT. Changing a define variable will not be saved.

#when character names start with the same letter, all are given 2-letter abbreviations
#player character
define pc = Character("[pc_name]")

#main characters
define ar = Character("Arnolfini Portrait")
define arm = Character("Arnolfini Portrait") #man
define arw = Character("Arnolfini Portrait") #woman
define ard = Character("Arnolfini Portrait") #dog
define d = Character("The Davids")
define dm = Character("David") #mikey
define db = Character("David") #bernini
define dd = Character("David") #donny
define gi = Character("Gilgamesh")
define gl = Character("Glimmer")
define m = Character("Mona Lisa")
define p = Character("Poster")
define st = Character("St. Catherine")
define so = Character("Soup")
define su = Character("Sunflowers")
define ss = Character("Soup & Sunflowers")

#side characters
define ad = Character("Admin")
define e = Character("Ea-Nasir")
define n = Character("Nighthawks")
define sue = Character("Sue")
define t = Character("Theodore")
define v = Character("Vending Machine")

#utility characters
define meta = Character("") #deprecated, no use

#character name variables
default pc_name = ""

#player backgrounds
default pc_work = 0
default pc_skill = 0
default pc_education = 0

#choice variables
default phone_wait_count = 0

#character disposition trackers - deprecated, to be removed
default d_Arnolfini = 0
default d_Davids =  0
default d_Gilgamesh = 0
default d_Glimmer = 0
default d_MonaLisa = 0
default d_SaintCatherine = 0
default d_Soup = 0
default d_Sunflowers = 0

#disposition tier values - deprecated, to be removed
define d_Tier1 = -150
define d_Tier2 = -95
define d_Tier3 = -80
define d_Tier4 = -50
define d_Tier5 = 0
define d_Tier6 = 50
define d_Tier7 = 35
default d_Total = 0

#function to return disposition label from value - deprecated, to be removed
init python:

    class d_LabelFromValue():

        def __init__(self):
            self.value = 0
            self.label = "none"

        def ValueToLabel(self, value):
            if value == 0:
                self.label = "Terrible"
            elif value == 1:
                self.label = "Bad"
            elif value == 2:
                self.label = "Unpleasant"
            elif value == 3:
                self.label = "Neutral"
            elif value == 4:
                self.label = "OK"
            elif value == 5:
                self.label = "Good"
            elif value == 6:
                self.label = "Great"
            return self.label

default d_Label = d_LabelFromValue()


# start label is the first bit of game code that gets read
label start:
    scene museum bg1
    menu:
        "Skip to tour.":
            jump MuseumTour
        "Continue":
            call pronounselection

    scene museum bg1
    #will need to make this changeable through the preferences menu too
    "You picked [selectedpronouns], right on."
    "[they!c] [are] eating [their] apple."
    "[they!c] eat[s] [their] apple."
    "The apple is [theirs]."

    jump GameIntroduction

label end:
    return

#label used for in progress features, only accessible through developer commands
label testing:
    scene testing
    menu:
        "Cleaning":
            call minigamestart_cleaning("cleaning")
            jump testing
        "Saint Repair":
            menu:
                "Glass":
                    call minigamestart_stainedglass("glass")
                    jump testing
                "Plastic":
                    call minigamestart_stainedglass("plastic")
                    jump testing