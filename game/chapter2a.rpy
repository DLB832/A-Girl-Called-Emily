# Chapter 2a title page information:
# Date with Sox
# Location: The Grind House
# NPCs Present: varies
label chapter2a:
    $ date += 1  # NOTE: The day of the week is variable based off of the order you go on the dates.
    '[get_day(date)]' 
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

label ch02a_004:
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

return
