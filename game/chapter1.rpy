label chapter1: 
    # Chapter 1 title page information:
    # Day 1: Sunday, April 1st.
    # Location: Pepper's Interior
    # NPCs Present: Mr. & Mrs. Jamis
    '[get_day(date)]'
    scene bg peppers
    with fade
    jump ch1_001    

label ch1_001:
    "You flick your wrist up quickly, avoiding the eyes of the nearby tables and fellow Pepper's patrons. 
        You're right on time, but Emily has clearly been here a while."
    "A half full glass of water sits next to her, condensation pooling gently around the bottom. 
        Emily hasn't seen you yet, her back is towards you."
    
    menu approach1:
        "How do you approach?"
        "Close the distance to the table quickly, calling out to her to let her know you've arrived.":
            jump ch1_002
        "Take your time getting to the table, taking in a few more details about Pepper's.":
            jump ch1_003

label ch1_002:
    $ pc.path1points += 1
    show emily happy
    "Emily turns to find you, hair flicking clear of her face. Her big brown eyes crinkle just a bit, 
        but all other details are lost as your attention is captured by her smile. "
    "Her cheeks puff up to accommodate her unbridled excitement, 
        and you feel a little heat prickle in your own cheeks. "
    "You know Emily is pretty, but something about her smile magnetizes the whole room; 
        as if every set of eyes can't help but to look at her. "

    menu approached2:
        "\"I hope I'm not late - have you been waiting long?\"":
            jump ch1_008

            
label ch1_003:
    "As you walk towards the table, you notice Emily start to fret with the ends of her hair, 
        twirling it nervously between her fingers."
    "She shifts a little in her seat, and you here a slight creak as she unsticks herself from the vinyl. 
        She's been here longer than you first thought."
    
    menu approaching:
        "Suddenly unsure if you had the wrong time, you rush to the table and let her know you have arrived.":
            jump ch1_004
        "You know you had the right time. Continue walking at your current pace, taking a look around at the nearby tabels.":
            jump ch1_005
        
label ch1_004: # TODO: Update with correct text once narrative has been changed. 
    $ pc.path2points += 1
    show emily happy
    "Emily turns to find you, hair flicking clear of her face. Her big brown eyes crinkle just a bit, 
        but all other details are lost as your attention is captured by her smile. "
    "Her cheeks puff up to accommodate her unbridled excitement, 
        and you feel a little heat prickle in your own cheeks. "
    "You know Emily is pretty, but something about her smile magnetizes the whole room; 
        as if every set of eyes can't help but to look at her. "

    menu approach4:
        "\"I hope I'm not late - have you been waiting long?\"":
            jump ch1_008   

label ch1_005:
    # TODO: show Mr. & Mrs. Jamis
    "As you approach the table you notice Mr. and Mrs. Jamis sitting two booths further down, 
        both facing you and Emily. " 
    "There is a distinct frown on Mr. Jamis's face, although he quickly averts his eyes."
    "Mrs. Jamis gives you a tight smile."
    "As you return a brief smile of your own, you catch a hint of movement behind Mrs. Jamis." 
    # TODO: show Emily reflection 
    "On the wall behind her, a small mirror shows the distorted refelcteion of Emily at the table 
        in front of you, a smile sprouting from her lips." 
    menu approach_confront5:
        "How do you finalize your approach?"
        "Quickly and sheepishly ":
            jump ch1_006    
        "Slowly and confidently":
            jump ch1_007

label ch1_006: # TODO: Update with correct text once narrative has been changed. 
    $ pc.path2points += 1
    "Grateful to see she is happy to see you, you close the rest of the distance, giving her your best 
    \"Am I late? I'm so sorry!\" smile as you call out her name."
    show emily happy
    "Emily turns to find you, hair flicking clear of her face. Her big brown eyes crinkle just a bit, 
        but all other details are lost as your attention is captured by her smile. "
    "Her cheeks puff up to accommodate her unbridled excitement, 
        and you feel a little heat prickle in your own cheeks. "
    "You know Emily is pretty, but something about her smile magnetizes the whole room; 
        as if every set of eyes can't help but to look at her. "
    
    menu approach6:
        "\"I hope I'm not late - have you been waiting long?\"":
            jump ch1_008   

label ch1_007:
    $ pc.path3points += 1
    "Still confident you had the right time, and now suspecting she might have been watching your approach,
        you walk up to the table confidently."
    pc "\"Were you watching me just now?\""
    emily "Just now? No, I saw Mrs. Jamis smiling at something behind me so I figured someone was here. 
        I'm glad it's you!"
    pc "Am I late? I could have sworn we said 6:00 PM!"
    emily "Oh no, you're right on time! I have a chronic case of \"early is on time and on time is late.\" 
        I have the parents to thank for that lovely piece of anxiety."
    emily"It's a bit embarrassing, but I was just really...well...really excited for tonight."
    "Emily shifts her gaze down and away from your eyes a bit, a small bit of color rising on her cheeks."
    # TODO: show emily smiling
    "As she drifts her big brown eyes back up to you, she gives you a dazzling smile, warm as the sun."
    "Your fears melt away, and their place your excitement from earlier in the day returns. 
        She is excited to see you, that much is clear. "
    "All of her earlier apparent nervousness is gone without a trace, as if it had never been there."

    menu sit_down7:
        "Emily, THE Emily, is ona date with you! Take a seat across from her you dingus!":
            jump ch1_009

label ch1_008:
    emily "Oh no, you're right on time! I have a chronic case of \"early is on time and on time is late.\" 
        I have the parents to thank for that lovely piece of anxiety."
    emily"It's a bit embarrassing, but I was just really...well...really excited for tonight."
        
    menu sit_down8:
        "Emily, THE Emily, is ona date with you! Take a seat across from her you dingus!":
            jump ch1_009

label ch1_009:
    "Still slightly dazed by the radiance of her smile, you take your seat across from Emily." 
    "Her presence is calming, reassuring. You've seen her every day in class this year, and spent countless hours 
        in the school's Newspaper Club with her, but something is different now."
    "You have all of her attention, and boy does it feel good."

    "You've always liked Emily, ever since you arrived in Cape Bay a year and a half ago."
    "Junior year had been rough, but Emily made it all seem a little easier, more worthwhile."
    "You were able to tell yourself the move wasn't all bad, considering you got to meet her. 
        You could coast through the last year of high school in peace, before getting out of this salt soaked town and back to civilization."

    "Then, at the start of this year, lightning struck."
    "You noticed Emily sporting some merch from your favorite detective series, \"Brainchasers.\""
    "You plucked up every ounce of courage you could, and finally talked to her. 
        She had been ecstatic to meet another fan, and a whirlwind of smiles, touches, and glimmering eyes began."
    "In the aftermath, you found yourself as the second member of the two-person school Newspaper Club."

    "Your senior year since then has consisted of gray-scaled classes interrupted by the shimmering brilliance of 
        the daily Newspaper Club meetings."
    "Now, with the school year's end around the corner, Emily has asked you on a date."
    "This past Friday, after you had packed up to head home from club, she had stopped you at the door."
    "\"Sunday, 6pm, Pepper's restaurant. No story to chase, just the two of you.\" 
        As the door had closed behind you, your jaw had opened wide in shock."

    emily "I wish you'd stop looking so confused. I thought it was so obvious!"

    "Allegedly, Emily had been gently flirting with you all year."
    "Unfortunately, every single hint had gone straight over your head."

    "Emily, now sitting across from you (on a date!) looks expectantly at you to start the conversation."

    menu awkward_silence9:
        "So uh... how about them Clawdaddies, amiright?":
            jump ch1_010

label ch1_010:
    "Her laugh is short, but not rude. It calms your nerves, if only a bit."

    emily "Tell you what, why don't we start from the beginning? As if we've never met? I'd really like to re-do 
        our first meeting. I don't even think I asked you your name that day!"

    "Emily chuckles a little, with a slight edge of annoyance, as if chiding her previous self for this 
        slight against you. You laugh slightly in agreement, and put on your best \"I've never met you before\" 
        expression. Emily smiles, and asks you the following questions:"
    jump character_profile_entry

label ch1_011:
    "Questions all answered to your satisfaction, you use every muscle in your brain to think of something 
        interesting to say."
    "After a second of panic as you realize your brain must never have worked out a day in its life, 
        you decide to ask her the exact same questions."
    with Pause(0.75)
    emily "Well, my name is Emily Sanderson, pronouns she/her. I can't say I've ever had a nickname, 
        but I'm open to that changing if you get any ideas!"
        # TODO: Show emily wry smile
    "She gives you a wry smile, and your heart flutters ever so slightly."
    # TODO: fix emily animal placeholders
    emily "I'd like to think I most relate with A SEEMINGLY HARMLESS BUT RESPECTED ANIMAL. But, if we're being 
        fully honest, reptiles capture me more."
    emily "I LOVE to slither into a warm spot and soak it all up. So final answer, snake."
    "From your perspective here, Emily was the furthest from reptilian you could imagine. FIRST ANIMAL definitely 
        seemed to be more fitting, but you'll take her word for it."
    emily "With my free time...well I'm usually out doing interviews!"
    emily "I love freelancing stories for the Cape Bay Gazette, as well as Clawdad Times. 
        I know what you're going to say! \"That's work and not free time, Emily!\""
    emily "So, to better answer the question, I do enjoy a good mystery novel or movie."
    emily "I'll curl up in my nook under the sunlight, and get absolutely lost in chase, in the clues and 
        revelations. I love a mystery, hence my friend group's nickname I suppose."

    "You have heard of the Mystery Crew." 
    "The group is comprised of four local seniors: Emily Sanderson, Sox Sinclair, Neil Doubermann, and Z3R0."
    "You've met the other three members since moving to Cape Bay, but never exchanged more than general 
        pleasantries."
    "Sox seemed nice enough, but gave the impression that if anyone came within 3 feet of them without their 
        permission, they would hiss."
    "Sox's boyfriend, Neil, was almost the exact opposite. Immediately drawn to any person that comes within 
        conversation striking distance."
    "Neil had talked to you on more than a few occasions, and often invites you to come see him at the Pizza 
        Place where he works."
    "Z3R0 was more of an enimga than the other two, even though you see her more often than either Sox or Neil." 
    "She was prone to showing up at the Newspaper Club room towards the end of your working sessions, 
        waiting for Emily to finish up. Evidently they'd known each other since childhood."
    
    emily "Speaking of which...how do you feel about spending some time with each of the crew this week? 
        I promise they don't bite! Well, maybe not Z3R0... but she's mostly harmless!"
    
    menu spend_time_11:
        "Sure!":
            jump ch1_012
        "Sure, but much more hesitently":
            jump ch1_013
        "Why?":
            jump ch1_014

label ch1_012:
    $ pc.path1points += 1
    "Emily sends another blazing smile your way, but it doesn't seem to reach her eyes." 
    "She must be distracted by the food coming towards your table, you think."
    jump chapter2

label ch1_013:
    $ pc.path2points += 1
    $ emily.affection += 1
    # NOTE: Emily approves of your level of caution
    emily "Fantastic! Who do you want to meet up with first? I know their schedules by heart, 
        so I know when they are all free."
    jump chapter2

label ch1_014:
    $ pc.path3points += 1
    $ emily.affection -= 1
    # NOTE: Emily is cautious
    emily "Fantastic! Who do you want to meet up with first? I know their schedules by heart, 
        so I know when they are all free."
    jump chapter2

# NOTE: End of Chapter 1