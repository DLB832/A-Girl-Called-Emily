# defines a more complex image?
# @see file:///Users/derekcampbell/Documents/Game%20stuffs/renpy-8.2.1-sdk/doc/displaying_images.html#scene-statement
image emily happy question = VBox(
    "question.png",
    "emily happy.png",
    )

label testspace:
    '[get_day(date)]'
    $ date += 1
    '[get_day(date)]'
return
