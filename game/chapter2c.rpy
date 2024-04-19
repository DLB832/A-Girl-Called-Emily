# Chapter 2c title page information:
# Date with Z3R0
    # NOTE: The day of the week is variable based off of the order you go on the dates.
# Location: The Grind House
# NPCs Present: varies
label chapter2c:
    #TODO: show The Hardware Store
    "You've decided to go see Z3R0 at the  Chicago Hardware Store after school."
    "The hardware store is bigger than most other stores, and smells like fertilizer and damp soil. "
    jump ch2c_001

label ch2c_001:
    "The automatic door squeaks a bit as you enter the hardware store. 
        You breathe in the smell of soil, plants, raw wood, and is that...popcorn?"
    unkown "B3 W1TH Y0U 1N 4 S3C0ND!"
    menu greetZero2c1:
        "TAK3 Y0UR T1M3! 1'M UP FR0NT WH3N3V3R Y0UR R34DY.":
            $ zero.affection += 1
            jump ch2c_002
        "No rush, it's me, [pc.name]!":
            jump ch2c_002

label ch2c_002:
    "You glance around the store, rows and rows of miscellaneous items in front of you."
    "To your right is the cashier aisle, but it doesn't look like anyone is there. Where had that voice come from?"
    zero "0H, 1T'S JUST Y0U. EMILY S41D Y0U W3R3 C0M1NG BY. 1'M SURPR1S3D Y0U C4M3."
    zero "W3LL, TH3R3'S N0TH1NG T0 D0 4B0UT 1T N0W, S0 WHY D0N'T Y0U T4K3 4 S34T 0V3R BY TH3 P0PC0RN M4CH1N3? 1'LL T3LL H4R0LD T0 C0V3R F0R M3. "
    "Z3R0 stalks off towards the back of the store, gesturing dismissively to your left. You see a small table and chairs next to a quaint little 
        popcorn machine in the corner of the store."
    "With a shrug, more to yourself than anyone else, you make your way towards it and sit down; wondering
        just how does she do that with her voice...?"
    menu sit2c2:
        "Taking a seat by the popcorn machine, which direction do you face?"
        "Face towards the window, looking outside":
            jump ch2c_003
        "Face inwards, letting your eyes wander around the store":
            jump ch2c_004

label ch2c_003:
    "Outside, a little off to your left down the road, you see the intersection of Creek Drive and Main Street."
    "It is crowned by the town's one and only stop light. You know if you take a right onto Main Street, you'll pass the \"main strip,\" made famous mostly 
        by the Pepper's."
    "The Grind House, Pizza Place, dentist office, and old arcade make appearances, but you can't see them from where you're sitting thanks to the Buck Stretcher 
        grocery and general store blocking your view." 
    "The enormous parking lot at the back of the Buck Stretcher reaches all the way to the edge of the \"ravine,\" which was just a large creek that had 
        stubbornly burrowed a good 10 feet into the earth, creating a small cliff's edge in several spots."
    "The subtle squeak of boots on freshly cleaned floors brings your attention back inside."
    jump ch2c_005

label ch2c_004:
    "Inside the Chicago Hardware Store, you feel simultaneously at home and like you just spilled a 1,000 piece jigsaw puzzle on the ground."
    "On the one hand, the smell of fresh popcorn mixed with what can only be described as the smell of \"outside\" is comforting to you. 
        The scenery is full of greens, browns, and tans as a menagerie of potted plants hang from each display, each counter, each corner of the room."
    "On the other hand, the store's many aisles of tools, supplies, and doohickeys mean absolutely nothing to you."
    "Rows upon rows of gadgets and gizmos, all looking very important for very specific jobs, and not one of them making a lick of sense to you"
    "Except the paint aisle. You can say, with confidence, which one is the paint aisle."
    "The front of the store contains the table and popcorn machine, then the automatic doors to the parking lot, then the small checkout counters before finally 
        getting to the double doors leading to the open air nursery."
    "To your left, the aisles of the store stretch out. You can see down one of them all the way to the back of the store, where you spot two doors."
    "The left door has \"BATHROOM\" painted above it in bold red letters, and the right door has a faded yellow sign on it that you can't read from here."
    "As you look down towards these doors, you see the bathroom door swing open, and Z3R0 holds it for a moment with her boot as she adjust the trash can. 
        The bathroom is relatively clean, and even has a little display in the corner, with something pastel colored decorating it, almost like an altar."
    "Z3R0 turns out of the bathroom, and walks down the aisle towards you."
    jump ch2c_005

label ch2c_005:
    zero "4LR1GHT L0S3R, L3T'S D0 TH1S TH1NG. P0PC0RN?"
    default ch2c5Like = ""
    menu popcorn2c5:
        "\"That depends, am I allowed to try and throw some into my mouth?\"":
            $ zero.affection += 1
            $ ch2c5Like = "M3"
        "What kind of container are we talking about? I'll take the smallest one, thanks.":
            $ ch2c5Like = "S0X"
        "\"Absolutely! Got any \"Flavor BLAST Ya!\" seasonings? Those are my favorite.\"":
            $ ch2c5Like = "N31L"
        "\"Sure, but can I get it without salt?\"":
            $ ch2c5Like = "Emily"
    jump ch2c_006

label ch2c_006:
    if ch2c5Like == "M3":
        if pc.subPronoun == "he":
            $ zeroReference = "M4N"
        elif pc.subPronoun == "she":
            $ zeroReference = "W0M4N"
        else: #they/other
            $ zeroReference = "P3RS0N"
        zero "4 [zeroReference] 4FT3R MY 0WN H34RT! 1'LL 4LL0W 1T."
    elif ch2c5Like == "S0X":
        zero "Y0U S0UND JUST L1K3 [ch2c5Like]. 0N3 SP3C14LY S3L3CT3D, 3XTR4 CUTE C0NT41N3R C0M1NG UP."
    elif ch2c5Like == "N31L":
        zero "Y0U S0UND JUST L1K3 [ch2c5Like]."
        zero "1 JUST S0 H4PP3N T0 K33P 3XTR4 0N H4ND TH3S3 D4YS, F0R W31RD0S L1K3 Y0U."
    else: #Emily
        zero "Y0U S0UND JUST L1K3 [ch2c5Like]."
        zero "LUCKY F0R Y0U, AN0TH3R CR4ZY P3RS0N 34TS H3R3, T00. PYSCOP4TH P0PC0RN, C0M1NG R1GHT UP."

    with Pause(1.0)
    "Z3R0 busies herself with the popcorn order, placing yours in front of you as she circles around to sit across from you. 
        She flicks a piece up into the air, catching it with her mouth as she sits down."
    "The move is too effortless, you think she's practiced it more times than she may ever admit."
    jump ch2c_007
        
label ch2c_007:
    zero "0K4Y N3W K1D, WH4T W0ULD Y0U L1K3 T0 KN0W? SUR3L3Y S0M30N3 1NT3R3ST3ED 1N Emily C4N C0M3 UP W1TH 4 D3C3NT 
        C0NV3RS4T10N T0P1C, R1GHT? SH0ULD B3 4 BR33Z3 F0R Y0U."
    menu smallTalkch2c7:
        "What do you want to talk about with Z3R0?"
        "Bring up your dislike of small talk, see if you can commiserate on it together.":
            jump ch2c_008
        "Point out that it's your first time really talking together, and ask for a fresh start. A clean slate. Emily would appreciate this, you think.":
            $ zero.affection += 1
        "Excitedly bring up the first thing that comes to your mind.":
            $ zero.affection -= 1
        "Ask Z3R0 for her thoughts on having grass lawns versus native lawns, then ask for mystery video game recommendations." if emily.ch1ConversationTopics == True:
            $ emily.affection += 1
            $ zero.affection += 1
    jump ch2c_008

label ch2c_008:
    "Despite Z3R0's repeated attempts to derail and otherwise turn the conversation, the two of you have more than a few things in common, and the conversation 
        flows." 
    "You hate to admit it, but you find yourself generally having a good time."
    "You can see the same realization in Z3R0's eyes as you both recall your favorite episodes of Brainchasers. Her cool, laid back demeanor never falters 
        throughout the conversation, but you notice her posture shift from \"I don't care AND I'm better than you\" to just \"I don't care.\""
    "While Z3R0 is generally not very expressive, you catch more of her subtle sarcastic cues as the conversation continues."
    "You steer the conversation towards interesting topics, like recent video game releases, city ordinances on \"weeds\" in front yards, and Emily's recent 
        articles. Once safely on the topic of Emily, Z3R0 seems to puff up just a bit, like a bird admiring it's finely built nest."
    #TODO: Additional details are learned about Z3R0's basic backstory. 
        #No large details or revelations, but now players know who Z3R0 is. 
        #You learn Z3R0's pronouns are she/her, 
        #confirm Emily is her best friend, 
        #is founding member of the high school gaming club, 
        #and spends most of her free time playing video games and hanging out with Emily and the rest of the crew.
    jump ch2c_009

label ch2c_009:
    "Popcorn containers now empty, and only a few pieces having littered the floor, the two of you startle a bit as the loudspeaker crackles to life."
    "Z3R0 is summoned to the cashier stand, and you can see her grandfather, Harold, there with a small line forming. You tell Z3R0 to head on over, 
        you'll clean up the table."
    "As she turns to go, she gives a small salute as she says, \"S33 Y0U N3XT T1M3, L0S3R,\" and you have the sudden feeling that you have passed a test."
    "You clean up the table and the few pieces of popcorn that had fallen to the floor, then head for the exit."
    jump ch2c_010

label ch2c_010:
    "As you leave the Chicago Hardware Store, Emily texts you:"
    emily "Try not to be too hard on Z3R0, she's just a little overprotective of me. Where are you going tomorrow?"
    $ ch2charMenu.add("Z3R0")
    jump chapter2
return
