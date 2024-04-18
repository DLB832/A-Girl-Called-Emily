# Chapter 2a title page information:
# Date with Sox
# Location: The Grind House
# NPCs Present: varies
label chapter2a:
    # TODO: show Grind House
    "You decided to go see Sox at the Grind House after school."
    "The Grind House is suprisingly warm and cozy, thanks to all the wood furniture, flooring, and accents."
    "It doesn't lean into cabin in the woods though."
    "The gleaming stainless steel appliances, as well as the well lit display case of pastries, 
        keep the Grind House firmly rooted in the 21st century."
    "The pastries come from the attached bakery." 
    "Rumor around town is the owners of the bakery wanted to hop on the coffee trend, 
        but for some reason can't stand the smell. So, they bought the building right next door."
    "As such, a small collection of fresh pastry treats are always available at the Grind House."

    jump ch2a_001

label ch2a_001:
    "The bell jingles as you walk in, but you don't see anyone behind the counter." 
    "The shop is small, only a handful of tables, all currently empty."
    unkown "No one really wants coffee at 4 PM, you know."

    menu enter2a1:      
        "\"Wait, this is a coffee shop? I had no idea!\"":
            $ sox.affection += 1
            jump ch2a_002
        "It's me, [pc.name]":
            jump ch2a_002

label ch2a_002:
    soxNB "Oh, it's you! Thank god - I thought I was going to have to do my job for a minute."
    soxNB "I'll be honest, Emily told me you were swinging by, but I wasn't sure if you'd come. 
        Grab a table, I'll be there in a second."        
    "You hear small clattering noises as Sox ducks back below the counter. Looking around, 
        you spot a nice table by one of the front windows and sit down."
    
    menu table2a2:
        "Look out the window":
            jump ch2a_003
        "Look around the room":
            jump ch2a_004

label ch2a_003:
    "Outside, you see the main street of bustling Cape Bay." 
    "A brief wind kicks up a few soggy leaves, providing a little movement on the otherwise still scene."
    "Down at the far end of the street you see the Pepper's, its neon sign a little too saturated compared 
        to the rest of the street."
    "The lights reflect strangely in the cars parked between it and the Pizza Place, which is directly across 
        Main Street from you."
    "One door to the right gets you to the Buck Stretcher grocery and general store."
    "On the opposite end of the street, you see City Hall and it's neighbor, the small Cape Bay public library. "
    "You know that right next door to the Coffee shop is the old, and now abandoned, arcade, and on the other 
        side the Baxter Family Bakery, which provides the pastries up for sale."
    "On the other side of the old arcade is the Law Office of Demarcus Dillon, with it's large faded blue sign 
        proudly stating \"1-800-DIWORCE.\" Your attention is drawn back to the Grind House as Sox 
        calls out to you."
    jump ch2a_005

label ch2a_004:
    "Inside, you see the familiar sights of the Grind House."
    "You are no stranger to the town's only independent coffee shop, but you do admit the convenience of the 
        Snortbucks has meant you've only been here infrequently recently."
    "With your back to the wall, you can hear the light sounds of a conversation in the bakery next door, 
        behind you."
    "Across the room, the wall shared with the old arcade is covered in art, newspaper clippings, and what 
        seems like a random assortment of gardening tools."
    "You hear, rather than see, Sox scuttling behind the counter in the middle of the room; 
        and the brand new espresso machine gleaming unnaturally compared to the wooden surroundings."
    "A framed portrait hangs on the wall above the coffee bar. To your left the room ends in a space with 
        three doors. One goes to the bakery next door, one to the parking lot outside, and one to the 
        storage room behind the counter area."
    "In the far corner, between the bakery and parking lot doors, a small altar has been lovingly decorated 
        with small floral arrangements."
    "Your attention is drawn back as Sox calls out to you."
    jump ch2a_005

label ch2a_005:
    soxNB "Okay on second thought, you want anything?"
    default ch2a5Order = ""
    default ch2a5Like = ""
    menu coffeOrder2a5:
        "What is your coffee order?"
        "Just a black coffee please!": #Z3R0
            $ ch2a5Order  = "coffee"
            $ ch2a5Like = "Z3R0"
        "Do you have any tea?": #Sox
            $ sox.affection += 1
            $ ch2a5Order  = "tea"
            $ ch2a5Like = "me"
        "How about the Whipped Double Chocolate Mocha, extra chocolate chips, no espresso?": #Neil
            $ ch2a5Order  = "sugary concoction"
            $ ch2a5Like = "Neil"
        "Just a water, thanks.": #Emily
            $ ch2a5Order  = "water"
            $ ch2a5Like = "Emily"
    jump ch2a_006

label ch2a_006:
    soxNB "You sound just like [ch2a5Like]."
    if ch2a5Like == "Z3R0":
        soxNB "Sure thing, hard ass."
    elif ch2a5Like == "me":
        soxNB "We do, actually! It's just the one, but it's my favorite thing on the menu."
    elif ch2a5Like == "Neil":
        soxNB "*Sigh* Didn't I just say I don't want to work? You're lucky I'm the expert on making these...
            one sugar rush coming right up!"
    else: #Emily
        soxNB "Nothing else float your boat? Whatever you say, boss."

    with Pause(1.0)
    "A couple minutes later, Sox sits down across from you, placing your [ch2a5Order] in front of you as 
        they sit with a fresh mug of tea in their hands."
    jump ch2a_007

label ch2a_007:
    soxNB "So... [pc.name]... look I would rather choke on one of Neil's soda fountain concoctions than 
        talk about the weather. But I know Emily really likes you and for that reason and that reason alone 
        I will suffer through some small talk."
    menu smallTalkch2a7:
        "Small talk?"
        "Commiserate on your shared dislike of small talk":
            $ sox.affection += 1
        "Point out that it takes two to tango":
            $ sox.affection -= 1
        "Excitedly bring up the first thing that comes to your mind":
            pc "Have you seen the new episode of \"Brainchasers?\" In it they ..."
        "Tell Sox you've been getting more into instrumental music recently, and ask if they have any recommendations. " if emily.ch1ConversationTopics == True:
            $ emily.affection += 1
            $ sox.affection += 1
        #TODO: flesh out responses.
    jump ch2a_008

label ch2a_008:
    "While you both struggle at first, the small talk eventually finds a natural rhythm."
    "You knew Sox was reserved, but now spending time with them one-on-one, you understand why Emily is so 
        fond of them. Colors of a vibrant personality start to peak through their dark demeanor, adding hues 
        you hadn't expected."
    "Sox is cautious of you, but willing to try and learn more - so long as you don't spook them.
        You keep to safe conversation topics, asking after Neil and any recent updates."
    "Evidently Neil's title as reigning champion of the pizza eating competition was challenged again this 
        past weekend, to no avail. He had been quite proud of himself."
    #TODO: flesh out additional details
        #Additional details are learned about Sox's basic backstory. 
        #No large details, but a few so that players have a general idea about who Sox is. 
        #gender fluid, confirm dating Neil, senior in high school, interested in piano and instrumental music, etc.
    jump ch2a_009

label ch2a_009:
    "After you have both finished your drinks, the door chimes as a customer walks in. 
        It's a group of five freshman, all of them a little too loud for the small space."
    soxNB "Damn it. Sorry about that, [pc.name]. I didn't realize how long we had been chatting."
    "Sox gets up, collecting your cups from the table and turns to the freshman."
    soxNB "I'll be with you in a second!"
    #Sox apologizes quickly to you, and remarks that they hadn't even noticed how long it had been. 
    #They call out to the freshmen that they will be with them shortly, and 
    "They scuttle back to the counter with your empty drinks in hand; leaving you at the table alone."
    jump ch2a_010

label ch2a_010:
    "As you leave the Grind House, Emily texts you:"
    #NOTE: Shoule we have a phone image? or something along those lines?
    emily "Seems like that went well! Thank you so much for taking the time to hang out with Sox, 
        I know they get terribly bored during these weeknight shifts. Where are you going tomorrow?"
    $ ch2charMenu.add("Sox")
    jump chapter2

return
