# Chapter 2d title page information:
# Date 2 with Emily
# Day 5: Thursday, April 5th 
# Location: The Abandoned Arcade
# NPCs Present: varies
label chapter2d:
    "You are finally meeting back up with Emily, and instead of doing work in the newspaper room as you usually do, Emily is surprising you with a 
        secretive story lead, and taking you on a trip to a suprise location."
    "You are going to the abandoned arcade."
    default arcadePowerOn = False
    jump ch2d_001

label ch2d_001:
    "As you shut the door to Emily's car in the familiar parking lot, your pulse finally starts to quicken."
    "You check your watch, noting just 30 more minutes until sunset."
    "The school days and newspaper work had all been relatively dull this week, with the exception of a few new smiles from Emily, 
        but now it seemed like things were finally getting interesting."
    "Emily had teased about taking you somewhere old that was actually very new, and had said it would technically count as a work trip, since she was 
        following up on a lead."
    emily "...but like I said, I'm still glad to spend the time with you. Once we've done our researching, I want to hear all about your dates this week."
    emily "Those weirdos mean so much to me, and I just know you're all going to love each other."
    emily "I'm getting ahead of myself - let's head inside!!"
    jump ch2d_002

label ch2d_002:
    "That's when you realize which door Emily is walking to in the small, partially empty parking lot."
    "In front of you are the backs of four buildings, and you knew Main Street was just on the other side of them."
    "The Grind House, and to its right the Baxter Family Bakery, brought some delicious smells into the air, but they mingled strangely with the smell of 
        pavement."
    "On the far left was the Law Office of Demarcus Dillon, its gorgeous, unforgettable signage unfortunately out of sight for the time being."
    "Emily stood at the door to the building between the Law Office and the Grind House, eyes scanning the parking lot subtly but with unmistakable intensity 
        as she fished for something in her bag."
    menu parkinglotLookout2d2:
        "Rush to her side, excited to see what she pulls out of her bag.":
            $ pc.path1points += 1
            jump ch2d_006
        "Keep your pace consistent, lazily scanning the parking lot so Emily can focus on digging through her bag.":
            jump ch2d_003

label ch2d_003:
    "Nothing looks out of place in the parking lot, nor in the surrounding small alleys connecting back to Main Street and Creek Drive. The sleepy town is just 
        that, drowsing on the edge of darkness, waiting patiently for the sun to go down."
    "You can hear cars driving past, and even some pulling in to the Pepper's and Pizza Place parking lot, but the buildings in front of you block 
        the line of sight."
    "Across a small alley to the left is the dentist office, and too the far right of all the buildings sat the Bank, perched on the corner of Main and Creek."
    "Beyond that, City Hall sat, cold and altogether lifeless at this time of day. If there was ever an absolutely perfect time to break in to the abandoned 
        arcade, it was right now."
    menu parkinglotLookout2d3:
        "Satisfied with your investigation, catch up with Emily to head inside":
            $ pc.path2points += 1
            jump ch2d_006
        "Confident that you won't be seen, slow your pace and focus your gaze on Emily":
            jump ch2d_004

label ch2d_004:
    "Your eyes meet briefly, and for just that moment Emily looks very…unlike herself."
    "There's a hunted expression in her eyes, matched by the cautious set of her shoulders and hips."
    menu parkinglotLookout2d4:
        "Take one last scan around the lot, making sure you aren't spotted breaking into the arcade.":
            $ pc.path2points += 1
            jump ch2d_006
        "Scared by her expression, demand an explanation before you commit to breaking into the arcade.":
            $ pc.path3points += 1
            jump ch2d_005

label ch2d_005:
    emily "Oh come on, [pc.nickname], just trust me! I promise the wait will be worth it, and we're not going to get in trouble. My dad is the sheriff, remember?"
    "There's a smile on Emily's face as she says this, but she can't hide the slight annoyance creeping into her tone. 
        Had she really been expecting more trust from you? Embarrassment rolls over you as you catch up with her."
    jump ch2d_006

label ch2d_006:
    "With a final rustle, Emily closes her bag quickly and turns to the door."
    "She enters something into the keypad, and the lock opens with a small BEEP."
    "As she turns the handle and opens the door, she steps to the side with a mischievous grin."
    emily "After you, beautiful!"
    "You are most definitely NOT flustered by this at all, just nervous and excited to see inside the old arcade. 
        That's why your laugh comes out just a bit too loud."
    jump ch2d_007

label ch2d_007:
    "As the door swings shut behind you, your eyes struggle for a moment to adjust to the dark room."
    "For one moment, you're standing in a galaxy of green, blue, and orange flecks of light."
    "You focus your vision, and see the glowing lights come from the assorted luminescent patterns scattered across the carpet covering the entire floor,
        with matching patterns on the ceiling and walls."
    "You hear a click behind you, right before the bright beam of a flashlight fills the room."
    emily "I haven't been here since I was a kid... It looks just like it did the last day we were here. Not a thing out of place..."
    jump ch2d_008

label ch2d_008:
    "You turn towards Emily, and see a soft, childish smile this time."
    "There is a look of wonder on her face, and you can almost picture a younger Emily, more than five years ago now. Notebook in hand, alternating between the 
        pinball machines and interviewing local tweens on their preferred video game genres, Emily would have been at home here."
    "You can see the nostalgia resting for a moment on her face."
    menu insideArcade2d8:
        "Bring her back to the present, reminding her why you're here. The nostalgia can wait, but the anticipation is killing you!":
            $ emily.affection += 1
        "Give her a moment to soak it all in. This place was important to her, after all.":
            jump ch2d_009
    jump ch2d_009

label ch2d_009:
    "Emily's attention focuses back on you."
    emily "Okay [pc.name], you know the old gossip, right? I'm sure you've read some of my older work on the subject."
    "While a small part of you resents Emily's cocksure attitude and assumption that you, practically an adult, would have read articles written and published 
        by a then-middle schooler, you have in fact read all of Emily's work."
    "What else was there to do in this town, anyway? It was decent investigative journalism, all things considered."
    "You know the facts: the owner of the arcade, Shellie Diedeme, disappeared five years ago after leaving a note saying she was taking \"time off\" to travel 
        after the loss of her brother."
    "In the note, she said he died in a car accident in California, and after the funeral she wouldn't be back for a while. Shellie had not come back, and that 
        left the arcade vacant, with ownership still rightfully belonging to her."
    emily "Well, recently Demarcus Dillon has been asking around in court about squatters rights to this building. It sounds like someone is making a move to 
        claim the place, and I want to know why."
    emily "Getting the code to the place was child's play, and with you here as my extra eyes and ears, I want to see for myself who is squatting in 
        the old arcade."
    "As you have been talking, moving past the bathroom and handful of tables, Emily's flashlight has swept across the room. A long line of pinball machines 
        cover the far left wall, then rows and rows of arcade games fill the middle of the building."
    "To your right is prize and concessions counter, with more games beyond it covering the far right wall."
    "Emily has brought you to a door labeled \"Employees Only.\""
    jump ch2d_010

label ch2d_010:
    emily "Dad says they sweep this place often, since it has such high traffic nearby and would be a prime target for break-ins."
    emily "Considering there hasn't been a break-in in Cape Bay in recent memory, and the only person that ever comes here is Kyle to check the locks, 
        we should be alone. Let's look around!"
    "From the eerie quiet of the place and stillness of the air, you believe no one else is in the arcade with the two of you."
    menu insideArcade2d10:
        "Where should you start in your investigation?"
        "Investigate the room":
            jump ch2d_011
        "Investigate the door labeled \"Employees Only\"":
            jump ch2d_012
        
label ch2d_011:
    "Looking around the old arcade, you start to realize what Emily meant by \"something old that was very new\" - the place looked absolutely stopped in time.
        It looked like it had just been closed for the night, rather than shuttered for five years."
    "The only difference being the concessions stand, as someone had been thoughtful enough to remove anything that could expire. That left the stand just a 
        little over halfway fully stocked, with bags of candy and chips hanging down long clip chains from the ceiling."
    "On the far wall you can see the extensive collection of pinball machines, all ready for the next customer to step up and take their rightful place. 
        Everything looks like it has been cared for, except for the small layer of dust coating everything."
    "After looking around, Emily calls you back over to look at the \"Employees Only\" door."
    jump ch2d_012

label ch2d_012:
    "As you look closer at the door, you hear Emily rummaging through her bag again. The door has a keypad just like the one on the back door, but other than 
        that it is plain and unadorned."
    emily "Okay, got it! Step back for a second. Oh, and hold this!"
    "Emily hands you the flashlight as she moves toward the keypad."
    "A second later you hear the BEEP of the lock, and a click as Emily swings the door open on silent hinges."
    "You sweep the room with the flashlight, seeing mostly old brown cardboard boxes full of concession stand supplies, a large standing tool box littered 
        with loose machinery, a door in the far right corner of the room, and on the far wall a row of what looks like utility equipment."
    jump ch2d_012a

label ch2d_012a: #NOTE: Seperated decision from scene so scene doesn't repeat when jumping back.
    default ch2emplyeesOnlyInvestigationMenu = set()
    menu employeesOnlyRoom2d12:
        set ch2emplyeesOnlyInvestigationMenu
        "You choose to..."
        "Head towards the standing tool box":
            jump ch2d_013
        "Pull down a cardboard box labeled \"CUPS\"":
            jump ch2d_014
        "Go investigate the door":
            jump ch2d_015
        "Walk to the back wall of the utility equipment":
            jump ch2d_016
        "Go back out to the arcade floor" if arcadePowerOn:
            jump ch2d_017
        
label ch2d_013:
    "It's a tool box covered in supplies, several drawers still open. Fresh oil has gotten on a few of the tools."
    emily "So, someone has been using the tools here, working on the arcade games maybe? That's weird...where to next?"
    $ ch2emplyeesOnlyInvestigationMenu.add("Head towards the standing tool box")
    jump ch2d_012a
        
label ch2d_014:
    if arcadePowerOn:  
        "You reach up to grab the box off the shelf above you. It feels fairly light, so you try to pull it down with one hand, feeling Emily's eyes on your back."
        "Unfortunately, as your athletic skills lag behind your investigation skills, you pull too hard and almost drop everything."
        "After a quick staggering step to steady yourself and the 5lb box, you place the box on the ground and open the lid, taking a long look at your prize."  
    else:
        "As you reach up to grab the box, you realize you'll need two hands."
        "Rather than pass the flashlight to Emily, you decide to put the flashlight between your teeth, just like they did on Brainchasers. 
            Unfortunately, they must use the world's smallest flashlights on tv shows."
        "Instead of holding it cleanly between your teeth, you get a decent amount of spit on the handle as you hold a mouthful of metal. But now you've committed, 
            so you hold the flashlight awkwardly in your mouth while pulling down the 5lb cardboard box."
        "Once on the ground, you quickly spit out the flashlight and open the lid, taking a long look at your prize."

    emily "Cups! How...interesting. Where to next?"
    $ ch2emplyeesOnlyInvestigationMenu.add("Pull down a cardboard box labeled \"CUPS\"")
    jump ch2d_012a

label ch2d_015:
    "You approach the door, and see another keypad lock, just like the previous two doors."
    "This door is wooden, or maybe faux-wooden, with a brass door knob instead of an extended metal handle like the others."

    emily "Another entry code? Unfortunately I don't know this one, but that's definitely worth noting. Where to next?"
    $ ch2emplyeesOnlyInvestigationMenu.add("Go investigate the door")
    jump ch2d_012a

label ch2d_016:
    "As you near the wall, Emily steps forward, grabbing the flashlight from your hands without a backwards glance."
    emily "No way! I think I can get the power back on! Let's see here... if I can just get to that switch... got it!"
    $ arcadePowerOn = True
    "With a loud whirring sound, the room thrums to life after Emily flips the main breaker."
    "In the other room, you hear a cacophony of jingles and bells. The arcade has come back to life!"
    emily "That's really strange, there shouldn't be any power to this building right now. Unless there's anything else you want to look at, 
        let's head back out to the main room."
    $ ch2emplyeesOnlyInvestigationMenu.add("Walk to the back wall of the utility equipment")
    jump ch2d_012a

label ch2d_017:    
    "The overlapping sounds of title screen music fills the arcade."
    "Most of the noise is absorbed by the carpeting, which you can now see has not been cleaned since the day it was installed."
    "The pinball machines glimmer and shine with varying hues on the far wall, all with a vibrancy typically reserved for brand new machinery."
    
    emily "Okay I do have to admit, I had no idea this would turn out so cool."
    emily "We now have more questions than answers... an exciting feeling, don't you think?"
    
    menu feelings2d17:
        "Since we're admitting things, I'm really just happy to be here with you.":
            $ pc.path1points += 1
            $ emily.affection += 1
        "As frustrating as it is, I admit it's an exciting feeling.":
            $ pc.path2points += 1
        "Exciting? More like frustrating... Can we skip to the part where you tell me everything you know?":
            $ pc.path3points += 1
            $ emily.affection -= 1
    jump ch2d_018

label ch2d_018:
    "Emily tilts her head back and laughs whimsically, her shoulders relaxing."
    emily "How did I KNOW you were going to say that? I feel like I know you better than myself sometimes..."
    emily "But I digress. It's time to \"dish the deets\", as Neil would say."
    emily "Why don't you grab us some snacks from the concession stand, and we'll debrief."
    "The concession stand isn't what it used to be, but it is still a stand with concessions!"
    "The lights flicker faintly as you approach, illuminating
    old price signs, and a handful of questionable snack remains that would give a health inspector nightmares. There are, however, still a few non-perishables
    worth salvaging!"

    menu concessionStand2d18:
        "What do you gather to bring back to Emily?"
        "A collection of assorted Dazzles candies catch your eye.":
            $ concessionChoice = "Dazzles"
        "Some packs of brightly colored, rainbow Rittles sounds good to you.":
            $ concessionChoice = "Rittles"
        "The delicious mounds of finely powdered sugar calls your name. A few packets of Fun Plunge slip into your pockets, and a few more go with you to share with Emily.":
            $ concessionChoice = "Fun Plunge"
        "A family size package of red Tizzlers should be plenty for the two of you.":
            $ concessionChoice = "Tizzlers"
            $ emily.affection += 1
    jump ch2d_019

label ch2d_019:
    "Emily has moved towards the collection of tables near the back door that you had used to get inside. 
    She looks up as you slide the package of [concessionChoice] toward her on the table."
    if concessionChoice == "Dazzles":
        emily "Dazzles? You and Z3R0 really have a lot in common."
    elif concessionChoice == "Rittles":
        emily "You know, I always think of Sox when I see these."
    elif concessionChoice == "Fun Plunge":
        emily "Sugar coma, here we come! Neil would be proud."
    else:
        emily "Oh, these are perfect! I was just craving some of these earlier!"    
    jump ch2d_020

label ch2d_020:
    "Snacks secured, you are ready to know what Emily has learned about the old arcade. She pulls out a notebook from her bag, scanning it quickly."
    emily "Okay, so now already know my earlier research on the building, and how at the time of Shellie's disappearance no one knew she had a brother."
    emily "At that time, I didn't have the know-how to dig any further. Or rather, Z3R0 didn't. But with the recent movement from Demarcus on trying to get the building, we tried again."
    emily "Z3R0 found Shellie's brother from California, and he did die in a car accident, but it was 12 years ago!!! Before she even arrived in Cape Bay!"
    
    "While Emily kept her tone and body language as professional as possible, she could not hide the girlish glee in her eyes."
    
    emily "So either Ms. Diedeme lied about her sibling and is out there somewhere, having abandoned her precious arcade to the ravages of time and vacancy, or she did not write that note."
    emily "Those machines were her life, and she loved the arcade kids like family. You never got to meet her, but believe me when I say that woman would have rather died than leave this store."
    emily "Unfortunately, I think that may in fact be the case."
    
    "Your eyes widen - died?! Hold on, you thought we were investigating a potential squatter?"
    
    emily "Before we jump to any conclusions, I'm unsure if Shellie's demise is related to whoever is attempting to get control of this building. But after looking around here, I'm quite sure there is no squatter of 5 years hanging out in the back room."
    emily "Demarcus must be making some quasi-legal claim to ownership since his law office is attached to the building and he pays for the plumbing still. That bozo can't afford to fix his 1-800-DIWORCE back to \"DIVORCE,\" so I'm sure he's looking for an easy cash grab."
    
    "You nod in agreement. Your limited interactions with Mr. Demarcus Dillon involved helping peel him off of the bar at Pepper's after a particularly rowdy $1 tequila night when you happened to be leaving at the right moment."
    "Oh, and a run-in at Snortbucks when he thought they had gotten his order wrong but he had really just grabbed yours."
    
    emily "All of this would be interesting in and of itself, but something has…changed recently."
    "Emily's glee never falters as she looks at you, eyes full of intensity and excitement."
    jump ch2d_021

label ch2d_021:
    emily "Someone has THREATENED me! ME!"
    emily "I found a note in my library book a week ago, threatening my family, threatening Sox, Neil, and Z3R0! There were so many details in the note, so much information about me that I've only told to a few people..."
    emily "[pc.name], I think I'm being stalked!"
   
    "You can't help but look around the room now, concerned immediately for her safety."
    
    menu happyQuestion2d21:
        "But wait, why did she seem so damn happy?"
        "Why do I get the feeling you're happy about this?":
            jump ch2d_022
        "Please tell me you're not happy about this...":
            jump ch2d_022

label ch2d_022:
    emily "Happy about it? I feel invigorated, alive! Nothing ever happens in this damn town, but now this? I'll be honest, at first I thought it was you who had sent the note. 
            You do keep such a...keen eye on me."
    menu questions2d22:
        "Wait, is that why you invited me to Pepper's? And to spend time with your friends? That's messed up!":
            $ pc.path1points += 1
        "So you set a trap this week, and used your friends to interview me? Clever, if not a little messed up.":
            $ pc.path2points += 2
        "What's that supposed to mean?! You're the one that's been weird here, not me!":
            $ pc.path3points += 3
    jump ch2d_023

label ch2d_023:
    emily "While that may be true, I stand by my methods. I needed to know if I could trust you."
    emily "I was hoping it wasn't you, of course!
        I'd much rather have you in my corner than against me. Although...no...sorry!"
    
    "A brief flush is on Emily's cheeks, but gone again in a flash. Was she... flirting? After accusing you of writing cryptic letters?"

    emily "Anyway, that's about the gist of it. I'm of the opinion that this arcade has a lot more secrets to share, especially now knowing someone is paying the power bill."
    emily "After a little more research, I intend on printing everything in the school paper tomorrow. The article is already done, I just have time for a few more edits depending on what I find here."
    menu paperPrinting2d23:
        "Printing your findings after being threatened? You can't be serious!":
            $ emily.affection += 0
        "Printing your evidence to shake the tree and see what comes out? Pretty dangerous... are you serious?":
            $ emily.affection += 1
    jump ch2d_024

label ch2d_024:
    emily "Deadly serious, if you'll excuse the pun."
    emily "I want to see what this mystery writer does, because based on their letter and what I'm finding through my research, I think I'm starting to get the big picture."

    "At this moment, your phone starts buzzing. Mom is looking for you, wondering if you'll be home for dinner soon."

    emily "Well, I guess that's our cue, huh? Come on cutie, I'll drop you off. Don't want to cause you any more trouble than I already have, ya know?"

    "With a wink, Emily moves away from the table. As she pulls her open notebook into her bag, you catch the very top of the page: 0483 - 3840"
    "As you push back from the table to join her, your eyes can't help but follow Emily."
    "She goes into the \"Employees Only\" room and cuts the generator, dumping the room back into darkness speckled with neon shapes."
    "She remerges with the flashlight on, a grin on her face."

    emily "Ready?"

# NOTE: End of Chapter 2
return
