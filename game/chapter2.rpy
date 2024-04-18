# Chapter 2 title page information:
# Day 2-5: Monday, April 2nd - Thursday, April 5th.
    # NOTE: The day of the week is variable based off of the order you go on the dates.
# Location: varies
# NPCs Present: varies
# NOTE: This is the jumping off point for Chapter 2. The Player can decide on 
    # what dates to go in and what order to go in them.
    # REF: https://www.reddit.com/r/RenPy/comments/qhibwn/hiding_an_option_after_a_player_has_selected_it/ 
default ch2charMenu = set()
label chapter2:
    $ date += 1 
    '[get_day(date)]'
    while len(ch2charMenu) < 3:
        menu ch2Dates:
            set ch2charMenu
            "Who should I go see?"
            "Sox":
                jump chapter2a
            "Neil":
                jump chapter2b
            "Z3R0":
                jump chapter2c
    "You've been on a date with each member of the Mystery Crew."
    menu ch2checkin:
        "Time to check back in with Emily":
            jump  chapter2d
        
    
return