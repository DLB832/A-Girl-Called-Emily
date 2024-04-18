# The script of the game goes in this file.
# @see Quickstart
## file:///Users/derekcampbell/Documents/Game%20stuffs/renpy-8.2.1-sdk/doc/quickstart.html#a-simple-game

# Declare characters used by this game. The color argument colorizes the name of the character.

# PC is the "Player Character."  
define character.pc = Character("[pc.name]")
# NOTE: who_colors assigned to characters are arbituary at the moment. Correct to go with character designs once finalized.
# Emily Sanderson: The story's antagonist and driving force. 
define character.emily = Character("Emily (she/her)",image="emily", who_color="#33e7ff")
default emily.affection = 10 # sets Emily's affection level at 10 to start.
default emily.ch1ConversationTopics = False

# Z3R0:
define character.zero = Character("Z3R0 (she/her)", image="zero", who_color="#21b130d2")
default zero.affection = 10

# Soverign Sinclair
define character.sox = Character("Sox", image="sox") #placeholder for affection values.
define character.soxMasc = Character("Sox (he/him)", image="sox", who_color="#44256c")
define character.soxFem = Character("Sox (she/her)", image="sox", who_color="#44256c")
define character.soxNB = Character("Sox (they/them)", image="sox", who_color="#44256c")
default sox.affection = 10

# Neil Doubermann
define character.neil = Character("Neil (he/him)", image="neil", who_color="#f1ea1a")
default neil.affection = 10

# Placeholder for unkown speaker
define character.unkown = Character("???", who_color="#687d7e")

# Declare variables used here.
default pc.name = "Player Character"
default pc.nickname = "PC"
default pc.animal = "Squirrel"
default pc.hobby = "Play Video Games"
default pc.path1points = 0
default pc.path2points = 0
default pc.path3points = 0
# setting the PC's 3rd person pronouns.
    # NOTE: Most of the game will be written in 2nd person, but these will be useful for when the PC is being talked about and not to. 
    # @see Personal-pronouns-table-visual.webp
default pc.subPronoun = "she"
default pc.objPronoun = "her"
default pc.possPronoun = "hers"
default pc.singReflxPronoun = "herself"
default pc.plurReflxPronoun = ""

# tuples are indexed at 0
default dayOfWeek = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" )
default date = 1

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #NOTE: transitions are added directly after using the "with" command. can be used with both show and scene

    # scene bg room
    # with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "emily happy.png" to the images
    # directory.

    # show emily mad

    # Content/trigger warnings
    # "Thank you for playing \"A Girl Called Emily\"."
    # "This game contains themes of  Gaslighting, Maniuplation, Cursing, and Depicitions of Underage Drinking."

    #emily "[pc.name] created a new Ren'Py game."
    #emily happy "Once [pc.nickname] adds a story, pictures, and music, [pc.objPronoun] can release it to the world!"
    jump chapter2

    # This ends the game.

return

label character_profile_entry:
    #What is your name?
    #Do you have a nickname?
    #Pronouns?
    #What animal do you most relate with?
    #What do you do in your free time?
    emily "Hi! What's your name?"
    $ pc.name = renpy.input("What name would you like to go by?",default="Player", length=8)
    $ pc.nmae = pc.name.strip()
    emily "Do you have a nickname?"
    $ pc.nickname = renpy.input("What nickname do you go by?", default="MC")
    $ pc.nickname = pc.nickname.strip()
    emily "What are your pronouns?"
    python:
        pc.subPronoun = renpy.input("What 3rd Person Subject Pronoun do you use?", default="they")
        pc.subPronoun = pc.subPronoun.strip()
        pc.objPronoun = renpy.input("What 3rd Person Object Pronoun do you use?", default="them")
        pc.objPronoun = pc.objPronoun.strip()
        pc.possPronoun = renpy.input("What 3rd Person Possessive Pronoun do you use?", default="theirs")
        pc.possPronoun = pc.possPronoun.strip()
        pc.singReflxPronoun = renpy.input("What 3rd Person Singular Reflexive Pronoun do you use?", default="themself")
        pc.singReflxPronoun = pc.singReflxPronoun.strip()
    emily "If you had to choose, what animal would you say you most relate with?"
    $ pc.animal = renpy.input("What animal do you most relate with?",default="Squirrel")
    $ pc.animal = pc.animal.strip()
    emily "What do you like to do in your free time?"
    $ pc.hobby = renpy.input("What do you do in your free time?",default="Play Video Games")
    $ pc.hobby = pc.hobby.strip()
    emily "What is your mother's maiden name? The last four of your social?"
    "Emily lets out a hearty laugh, wiping small tears from the corner of her eyes. It is music to your ears."
    menu profile_entry1:
        "Laugh with her":
            jump ch1_011
        "\"Smith and 1593\"":
            $ pii_told = True
            jump ch1_011