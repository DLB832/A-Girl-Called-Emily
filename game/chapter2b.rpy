# Chapter 2b title page information:
# Date with Neil
# Location: The Pizza Place
# NPCs Present: Mrs. Camber
label chapter2b:
    #TODO: show The Pizza Placce
    "You've decided to go see Neil at the Pizza Place after school."
    "The Pizza Place is a familiar space for you. Comfortablle, but greasy."
    jump ch2b_001

label ch2b_001:
    "Right after the door dings loudly in your ear, the smell of the Pizza Place 
        hits your nose. Notes of warm grease, italian spices, and glass cleaner all mingle 
        together with the smell of freshly made bread. It is both migraine educing and 
        relaxing."
    "You are no stranger to the Pizza Place, even if you've never been with a large group 
        before. Your usual table at the back of the restaurant is currently being taken up 
        by one of the sophomore couples."
    "Neil is actively cleaning one of the many windows next to the long row of booths, and 
        spins toward the sound of the dinging door with what can only be called extreme 
        enthusiasm."
    #TODO show Neil
    neil "[pc.name]!! You're here!! So glad you could make it!!"

    menu greetNeil:
        "Wave as enthusiastically, making it as clear as possible that you, too, are excited to be here.":
            $ neil.affection += 1
            jump ch2b_002
        "Wave gently at Neil, so he knows you heard him.":
            jump ch2b_002
        
label ch2b_002:
    "Neil drops down from the table he was standing on to the floor, cleaning supplies 
        discarded on the table behind him."
    "Drop is a bit of a stretch, considering Neil's long limbs could step right back up on 
        the table without much effort."
    "Neil swivels his hips sideways quickly, whipping a rag that was tucked into the back of 
        his jeans into his hands. As he wipes the residue off his hands, you can't help but 
        notice that he missed a few spots."
    "He spins the rag back around with a quick wag-like motion, and opens towards you with a 
    huge grin. "
    neil "Em said you'd be swinging by!! How are you?! Can I get you anything? "
    neil "Actually wait, let me put this stuff away. Don't want to leave a mess for 
        Mrs. Camber. Why don't you head to the front table and I'll meet you there?"
    "You look towards where Neil pointed, and see the very first booth is open. 
        Mrs. Camber is chatting to the two teenagers in your usual spot, and she gives a 
        small smile as your eyes meet."
    "While you don't typically prefer the front booth, you make your way towards it and 
        take a seat."
    
    menu table2b2:
        "Your gaze wanders..."
        "look out the window":
            jump ch2b_003
        "look around the room":
            jump ch2b_004

label ch2b_003:
    "Outside, you see the main street of bustling Cape Bay."
    "A brief wind kicks up a few soggy leaves, providing a little movement on the otherwise still scene."
    "Behind you, on the other side of the parking lot, is Pepper's. Its neon sign is just a little too 
        saturated compared to the rest of the street. The lights reflecting strangely in the cars parked 
        between it and the Pizza Place."
    "You know on the other side of the Pizza Place sits the Buck Stretcher grocery and general store. 
        On the end of main street, you see City Hall and it's neighbor, the small Cape Bay public library."
    "Across the street is the Grind House, nestled between the Baxter Family Bakery and the old, and now abandoned,
        arcade."
    "On the other side of the old arcade is the Law Office of Demarcus Dillon, with it's large faded blue sign 
        proudly stating \"1-800-DIWORCE.\"" 
    "Your attention is drawn back to the Pizza Place as Neil calls out to you."
    jump ch2b_005

label ch2b_004:
    "Inside the Pizza Place, the bright white overhead lights are softened by just how yellow everything else is.
        Mustard wallpaper against off-white vinyl booths, accented by lovely mayonnaise and 
        light gray checkered tiles."
    "At one point the table tops had been red, but the excessive use and limited cleaning over the years left 
        a thin gray film that dulled the red beneath." 
    "Even with Neil's hardy elbow grease, the best he could do was add a shine to the gray film, 
        never penetrating to the red beneath."
    "At the opposite end of the restaurant, across from the kitchen, your booth remains taken by the star-crossed 
        sophomores, who were alternating between whispering conspiratorially and glancing at their phones."
    "To your left, past the few stand alone tables, is the window with the best view of what is locally called 
        the \"Ravine,\" although you know it is very much so not a ravine."
    "Settled next to the window in the corner of the restaurant was a small altar, carefully decorated with small 
        flowers and petals. You hadn't noticed this altar before during any of your previous visits, probably
        because your usual spot is on the other side."
    "Your attention is drawn back as Neil calls out to you."
    jump ch2b_005

label ch2b_005:
    neil "Oh my gosh, do you want anything to eat?! We can totally split something?"
    neil "I need to take my break anyway! I know they don't actually pay me but I don't like to leave Mrs. Camber 
        for very long if I can help it. So what'll you have?"
    default ch2b5Order = ""
    default ch2b5Like = ""
    menu pizzaOrder2b5:
        "What do you want to order?"
        "\"Hawaiian Time all the way, please!\"":
            $ ch2b5Order = "Hawaiian pizza"
            $ ch2b5Like = "Z3R0"
        "\"The Big Veg works for me, thank you.\"":
            $ ch2b5Order = "Vegetable pizza"
            $ ch2b5Like = "Sox"
        "\"I'm here with THE Neil, how could I not get The Extreme Neil Pizza?\"":
            $ neil.affection += 1
            $ ch2b5Order = "pizza with nearly every topping imaginable"
            $ ch2b5Like = "a fellow pizza enthusiast"
        "\"oh, I'm good with whatever you recommend!\"":
            $ ch2b5Order = "Buffalo Chicken pizza"
            $ ch2b5Like = "Emily"
    jump ch2b_006

label ch2b_006:
    neil "That's so funny, you sound just like [ch2b5Like]!"
    if ch2b5Like == "Z3R0":
        neil "I'll set my watch to Hawaiian Time, one 'za coming right up!"
    elif ch2b5Like == "Sox":
        neil "Sustainable, flavorful, and full of those vegetables Sox keeps telling me I need; 
            one Big Veg coming your way!"
    elif ch2b5Like == "a fellow pizza enthusiast":
        neil "Now THAT'S what I'm talking about!! You've just got to give this pizza a try, 
            and let me know your HONEST thoughts okay? It's a new recipe!"
    else: #Emily
        neil "Leaving it up to the professional, huh? One mystery 'za coming right up!"

    with Pause(1.0)
    "Neil bounces up to grab Mrs. Camber on her way back into the kitchen, and by the gruff set of her hips and 
        loud eye roll, you can tell Neil has wormed his way into yet another free pizza."
    "Before you know it, a fresh [ch2b5Order] sits between you and Neil on table."
    jump ch2b_007

label ch2b_007:
    neil "Ya know, I don't think we've ever hung out one-on-one like this, [pc.name]! It's really cool of you 
        to do this, I've been rooting for you this whole time. Like, with Emily and everything."
    neil "Emily doesn't talk about herself a lot but she seems to be really excited about you, so I'm excited, too! 
        What do you want to talk about?"
    #TODO: update flavor options and expand on responses?
    menu smallTalkch2b7:
        "What do you want to talk about?"
        "Share that small talk makes you nervous":
            jump ch2b_008
        "Point out that it takes two to tango in a conversation":
            $ neil.affection -= 1
        "Excitedly bring up the first thing that comes to your mind":
            $ neil.affection += 1
        "Challenge Neil to an eating competition, his half of the pizza vs. your half. Ready, set, go!" if emily.ch1ConversationTopics == True:
            $ emily.affection += 1
            $ neil.affection += 1
    jump ch2b_008

label ch2b_008:
    "The conversation begins with gusto, Neil diving headfirst into any bone you throw out 
        in the conversation. He talks with you about anything and everything, and while you 
        find his bubbly energy stifling at first, you notice him start to mellow as the 
        conversation continues."
    "By the time he finishes his pizza (taking half the time it takes you, of course), you 
        can tell some of his frantic energy has worn off." 
    "You fall into a natural rhythm, surprised by the moments of calm and depth Neil has. 
        You knew Neil as the over active goofball, but seeing this slower pace helps you
        understand why Emily cares about him so much."
    "You ask about Sox, and Neil's resulting smile rose like fresh dough, expanding the last
        bits of baby fat on his face in a picture of angelic joy."
    "Sox was doing well, and they had found a new place to buy colored contacts recently, 
        so they were very happy about that."   
    #TODO: Additional details are learned about Neil's basic backstory. 
        #No large details or revelations, but now players know who Neil is. 
        #You learn Neil's pronouns are he/him, 
        #confirm he is dating Sox, is the mascot of the Clawdad's, 
        #and spends most of his free time planning eating competitions and "working" at the 
        #pizza place.
    jump ch2b_009

label ch2b_009:
    "As you sit there, plates now devoid of any pizza, you catch Mrs. Camber's fourth glance and decide it's 
        time to give the Pizza Place back their unpaid intern." 
    "As if shaken from a dream, Neil bolts upright and rushes to clear the table." 
    "He calls his goodbyes to you across the now empty restaurant, and you see him head towards the back 
        booth missing it's two love birds, a table bussing tub in hand."
    jump ch2b_010

label ch2b_010:
    "As you leave the Pizza Place, Emily texts you:"
    emily "I thought you two would get along. Isn't Neil the sweetest? Where are you going tomorrow?"
    $ ch2charMenu.add("Neil")
    jump chapter2

return
