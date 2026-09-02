define c = Character("cat", color="#873D00", 
    ctc="ctc_blink",
    ctc_position="nestled")
define d = Character("dog", color="#0E7509", 
    ctc="ctc_blink",
    ctc_position="nestled")
    
define a = Character(" ",     
    ctc="ctc_blink",
    ctc_position="nestled")

#lil arrow thing
image ctc_blink:
    "arrow.png"
    linear 0.50 alpha 1.0
    linear 0.50 alpha 0.0
    repeat 

#dimentions: 1280x720. 

#butterfly ending talley thing
default butterfly = 0

#red shoes green shoes thing
default red = 0

#fade timing
define slow_dissolve = Dissolve(1.4)

#jumping
transform sprite_jump:
    # Use easein and easeout to smooth out gravity acceleration
    easein 0.15 yoffset -30   # Moves up 30 pixels over 0.15 seconds
    easeout 0.15 yoffset 0    # Returns down to the base position over 0.15 seconds


#starting scene
label start:
    scene black

play music "u_5v7tonufva-melts-all-your-memories-249351.mp3" fadein 1.5

menu:
    "Wake up":
        show butterfly at center with slow_dissolve
        $ preferences.text_cps = 20
        a "This action will have consequences."
        scene waking_up with slow_dissolve
        scene waking_up2 with slow_dissolve
        pause 2.0
        scene waking_up3 with slow_dissolve
        pause 2.0
        jump senario1
    "Stay asleep":
        scene catinbed
        a "zzzzzzzz..."
        a "zzzzzzzzz..."
        menu:
            "wake up":
                scene black with dissolve
                show butterfly at center with slow_dissolve
                $ preferences.text_cps = 20
                a "This action will have consequences."
                scene waking_up with slow_dissolve
                scene waking_up2 with slow_dissolve
                pause 2.0
                scene waking_up3 with slow_dissolve
                pause 2.0
                jump senario1

#senario1
label senario1:
scene bathroomwithcatinmirror with slow_dissolve
pause 1.5
c "guhhh"

menu:
    "Brush teeth":
        scene brushingteethcat with slow_dissolve
        play sound "teeth.mp3"
        pause 2.0
        scene washingfacecat with slow_dissolve
        play sound "water.mp3"
        pause 2.0
        with dissolve
        jump senario2
    "Don't brush teeth":
        c "I don't feel like it :P"
        scene washingfacecat with slow_dissolve
        play sound "water.mp3"
        pause 2.0
        with dissolve
        jump senario2 

#senario2
label senario2:
scene kitchen with slow_dissolve
pause 1.5
show defaultcat at right with slow_dissolve
c "hmm, should I eat breakfast or skip it?"
hide defaultcat with dissolve
menu:
        "Eat breakfast":
            show thinkingcat at right with slow_dissolve
            c "hmm, should I eat fish or chicken?"
            menu:
                "Fish":
                    scene fishinplate with slow_dissolve
                    pause 1.0
                    show happycat at right with slow_dissolve
                    play sound "eating.mp3"
                    c "yum!"
    
                    pause 1.0
                "Chicken":
                    scene chickeninplate with slow_dissolve
                    pause 1.0
                    show happycat at right with slow_dissolve
                    play sound "eating.mp3"
                    c "yum!"
                    pause 1.0
                    with dissolve
            jump senario3

        "Skip breakfast":
            show defaultcat at right with slow_dissolve
            c "yah I'm not that hungry :P"
            with dissolve
            jump senario3

#senario3
label senario3: 
    scene hallwaytodoor with slow_dissolve
    show defaultcat at right with slow_dissolve
    pause 0.5
    c "I want to go outside for a walk!"
    $ preferences.text_cps = 5
    c "but..."
    $ preferences.text_cps = 60
    hide defaultcat
    show thinkingcat at right with slow_dissolve
    pause 1.5
    hide thinkingcat
    scene shoes with slow_dissolve
    pause 1.0
    c "Should I wear the {color=#870000}red{/color} shoes {w=1}or {w=0.5}the {color=#0D7509}green{/color} shoes?"
    pause 1.0
    menu:
        "Red shoes": 
            scene catwithredshoes with slow_dissolve
            pause 1.0
            show happycat at right with slow_dissolve
            c "I love these shoes!"
            c "time to go outside!"
            with dissolve
            jump senario4
        "Green shoes":
            scene catwithgreenshoes with slow_dissolve
            pause 1.0
            show happycat at right with slow_dissolve
            c "I love these shoes!"
            c "time to go outside!"
            with dissolve
            jump senario4

stop music fadeout 0.5

#senario4

label senario4:
    play music "slow-2021-08-17_-_8_Bit_Nostalgia_-_www.FesliyanStudios.com.mp3" fadein 1.5 
    play sound "door.mp3"

    if red == 1:
        scene outsidehousewithcat with slow_dissolve #red shoes
        pause 2.3
        scene parkwithcat with slow_dissolve
    else:
        scene outsidehousewithcat with slow_dissolve #green shoes
        pause 2.3
        scene parkwithcat with slow_dissolve
    
    pause 1.5 
    show surprisedcat at right, sprite_jump
    c "What's that?"
    scene butterflyontheground with slow_dissolve
    pause 2.3
    scene park with slow_dissolve
    pause 1.0

    show worriedcat at right with slow_dissolve
    pause 0.4
    c "I think it's hurt, I should help it!"
    hide worriedcat with slow_dissolve
    scene butterflyontheground with slow_dissolve
    pause 1.0
    menu:
        "Help the buterfly":
            show bravecat at right with slow_dissolve
            c "I gochu lil bro"
            scene catwithbutterfly with slow_dissolve
            pause 1.0
            scene butterflyfliesaway with slow_dissolve
            pause 0.7
            $ butterfly = 1
            with dissolve
            jump senario5
        "Leave the buterfly alone":
            show moreworriedcat at right with slow_dissolve
            c "I have a bad feeling about this..."
            c "should I, {w=1} ... {w=1} help it?"
            hide moreworriedcat
            menu: 
                "Help the butterfly":
                    show bravecat at right with slow_dissolve
                    c "I gochu lil bro"
                    scene catwithbutterfly with slow_dissolve
                    pause 1.0
                    scene butterflyfliesaway with slow_dissolve
                    pause 0.7
                    $ butterfly = 1
                    with dissolve
                    jump senario5
                "Leave the butterfly alone":
                    show worriedcat at right with slow_dissolve
                    c "I should just leave..."
                    with dissolve
                    jump senario5

#senario5
label senario5:
    if red == 1:
        scene parkwithcat with slow_dissolve #red
        pause 1.0

    else:
        scene parkwithcat with slow_dissolve #green
        pause 1.0

show defaultcat at right with slow_dissolve
c "Hey!"
c "Who's that?"

show dogblack at left with dissolve
c "Oh! {w=1} Dog!"
show dogdefault at left with slow_dissolve
hide dogblack
d "Hello Cat!"
c "Hello!!"
d "do you want to go on a walk with me?"
menu:
    "Go on a walk with Dog":
        hide defaultcat with dissolve
        show happycat at right with slow_dissolve
        c "Yah! Let's go!"
        hide dogdefault
        show happydog at left with dissolve
        d "yay!"
        scene parkwalkingwithcatanddog with slow_dissolve
        play sound "grass.mp3"
        pause 2.0
        scene catsaygoodbyetodog with slow_dissolve
        pause 1.0
        if butterfly == 1:
            show butterflyfade
            with dissolve
            jump senario6
        else:
            with dissolve
            jump senario6
    "Don't go on a walk with Dog":
        show defaultcat at right with slow_dissolve
        c "Nah, maybe next time :3"
        show happydog at left with slow_dissolve
        d "alg!"
        scene parkwithcat with slow_dissolve
        if butterfly == 1:
            show butterflyfade
            jump senario6
        else:
            jump senario6

#senario6
label senario6:
scene catonsidewalk with slow_dissolve
pause 1.0
scene sidewalk with slow_dissolve
pause 0.7
show defaultcat at right with dissolve
c "wow I should really eat lunch..."
hide defaultcat with dissolve
scene leftandrightresturant with slow_dissolve
pause 0.5
show thinkingcat at right with slow_dissolve
c "which one should I go to?"
hide thinkingcat with dissolve
pause 0.3
menu: 
    "Left restaurant":
        scene catinleftresturant with slow_dissolve
        pause 1.5
        show happycat at right with dissolve
        c "Yum! pizza!!"
        with dissolve
        jump senario7
    "Right restaurant":
        scene catinrightresturant with slow_dissolve
        pause 1.5
        show happycat at right with dissolve
        c "Yum! sushi!!"
        with dissolve
        jump senario7

#senario7
label senario7: 
scene leftandrightresturant with slow_dissolve
pause 1.5
show defaultcat at right with dissolve
c "where should I go now?"
menu:
    "Go to the waterside":
        hide defaultcat with dissolve
        scene watersidewithcat with slow_dissolve
        pause 1.7
        scene waterside with dissolve
        pause 0.3
        show defaultcat at right with dissolve
        pause 0.3
        $ preferences.text_cps = 5
        c "so relaxing..."
        hide defaultcat with dissolve
        scene watersidewithcat with slow_dissolve
        $ preferences.text_cps = 60
        c "so pretty too..."
        menu: 
            "stay a bit longer":
                show happycat with dissolve
                c "I could stay here forever..."
                hide happycat with dissolve
                scene watersidewithcat with slow_dissolve
                pause 2.0
                menu: 
                    "head back":
                            if butterfly == 1:
                                show butterflyfade with dissolve
                                with dissolve
                                jump senario8
                            else:
                                with dissolve
                                jump senario8
            "Go back":
                scene waterside with slow_dissolve
                show defaultcat with dissolve
                c "Maybe I should head back"
                hide defaultcat with dissolve
                if butterfly == 1:
                    show butterflyfade with dissolve
                    with slow_dissolve
                    jump senario8
                else:
                    with slow_dissolve
                    jump senario8

    "Go to the forest":
        scene forestwithcat with slow_dissolve
        pause 1.5
        scene forest with slow_dissolve
        pause 1.5
        scene birdontree1 with slow_dissolve
        pause 1.5
        scene birdonetree2 with slow_dissolve
        pause 1.5
        scene forest with slow_dissolve
        show happycat at right with dissolve
        c "I love the forest!"
        pause 0.5
        menu: 
            "stay a bit longer":
                c "I could stay here forever..."
                hide happycat with dissolve
                scene forestwithcat with slow_dissolve
                menu: 
                    "head back":
                            if butterfly == 1:
                                show butterflyfade with dissolve
                                with dissolve
                                jump senario8
                            else:
                                with dissolve
                                jump senario8
            "Go back":
                c "Maybe I should head back"
                if butterfly == 1:
                    show butterflyfade with dissolve
                    with dissolve
                    jump senario8
                else:
                    with dissolve
                    jump senario8


#senario8
label senario8:
    scene sunsetwithcat with slow_dissolve
    pause 1.5
    scene sunsetwithcat2 with slow_dissolve
    c "what a pretty sunset"
    if butterfly == 1:
        with dissolve
        jump ending3 #don't forget to fade it
    else:
        with dissolve
        jump ending2

#endings

label ending1:
    scene sleeping_with_sun_up with dissolve
    "zzzzzzzzz..."
    pause 1.0
    menu:
        "Return to Main Menu":
            with dissolve
            return

#normal ending ig
label ending2:
    stop music fadeout 2.0
    play music "u_5v7tonufva-melts-all-your-memories-249351.mp3" fadein 1.5

    scene sunsetwithcat2 with slow_dissolve
    pause 1.5
    scene outsidehousewithcatsunset with slow_dissolve
    pause 1.5
    scene catinhouse2 with slow_dissolve
    pause 1.5
    show defaultcat at right with dissolve
    c "What a good, perfect day..."
    hide defaultcat with dissolve
    show catyawn at right with dissolve
    c "*yawn*"
    hide catyawn with dissolve
    pause 0.5
    scene catinbed with slow_dissolve
    pause 1.0
    scene black with dissolve
    #fade to black
    jump credits

#this is the one where he gets hit by a CAR!!!
label ending3:
    stop music fadeout 2.0
    play music "ending3.mp3" fadein 1.5

    scene sunsetwithcat2 with slow_dissolve
    pause 1.2
    scene carhitcat1 with slow_dissolve
    pause 1.2
    scene carhitcat2 with slow_dissolve
    pause 1.2
    scene carhitcat3 with slow_dissolve
    pause 1.2
    with dissolve
    scene carhitcat4 with dissolve
    pause 1.7
    
    scene black with dissolve
    jump credits

#credits
label credits:
    stop music fadeout 2.0
    play music "ending.mp3" fadein 1.5

    scene black with dissolve
    centered "Thank you for playing!\nCreated by: Chuqi and Margarita\n:P"
    return