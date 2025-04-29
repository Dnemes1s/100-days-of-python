print('''                                              _____________
                                  ..---:::::::-----------. ::::;;.
                               .'""""""                  ;;   \  ":.
                            .''                          ;     \   "\__.
                          .'                            ;;      ;   \";
                        .'                              ;   _____;   \/
                      .'                               :; ;"     \ ___:'.
                    .'--...........................    : =   ____:"    \ 
               ..-""                               """'  o"""     ;     ; :
          .--""  .----- ..----...    _.-    --.  ..-"     ;       ;     ; ;
       .""_-     "--""-----'""    _-"        .-""         ;        ;    .-.
    .'  .'                      ."         ."              ;       ;   /. |
   /-./'                      ."          /           _..  ;       ;   ;;;|
  :  ;-.______               /       _________==.    /_  \ ;       ;   ;;;;
  ;  / |      """"""""""".---."""""""          :    /" ". |;       ; _; ;;;
 /"-/  |                /   /                  /   /     ;|;      ;-" | ;';
:-  :   """----______  /   /              ____.   .  ."'. ;;   .-"..T"   .
'. "  ___            "":   '""""""""""""""    .   ; ;    ;; ;." ."   '--"
 ",   __ """  ""---... :- - - - - - - - - ' '  ; ;  ;    ;;"  ."
  /. ;  """---___                             ;  ; ;     ;|.""
 :  ":           """----.    .-------.       ;   ; ;     ;:
  \  '--__               \   \        \     /    | ;     ;;
   '-..   """"---___      :   .______..\ __/..-""|  ;   ; ;
       ""--..       """--"        m l s         .   ". . ;
             ""------...                  ..--""      " :
                        """"""""""""""""""    \        /
                                               "------"''')
print("Welcome to the choose your own adventure game!")

print("Your in a garage with 2 cars infront of you. You can choose the Mitsubishi or the BMW.")
car = input("Which car do you want to drive? (Mitsubishi, BMW): ")

if car == "Mitsubishi" or car == "mitsubishi":
    print("You turned on the car and it started. You hear the sound of the car rumble to life")
    print("you drive out of the garage and you see a fork in the road.")
    print("You can go left or right.")

    road = input("Which way do you want to go? (left, right): ")
    if road == "Right" or road == "right":
        print("You drove right and saw a mountain pass to drive")

        print("You drive up the mountain pass and someone comes up behind you to challenge you to a race")
        print("You can choose to cruise down the mountain pass, Speed up and run away or accept the challenge.")
        challenge = input("What do you want to do? (cruise, speed, challenge): ")
        if challenge == "challenge" or challenge == "Challenge":
            print("You accepted the challenge and you race the person down the mountain pass.")
            print("You win the race and cruise home in style.")

        elif challenge == "cruise" or challenge == "Cruise":
            print("You cruised down the mountain pass and enjoyed the view.")
            print("You get home and park the car.")

        elif challenge == "speed" or challenge == "Speed":
            print("You sped down the mountain pass and lost control of the car.")
            print("You crashed into a tree and the car is wrecked.")
            print("game over")

        else:
            print("You didn't choose any of the options and you crashed into a tree.")
            print("game over")
    

    else:    
        print("You drove left and you see a nice beach front carpark.")
        print("You park the car and get out to take a look.")
        print("You see a nice beach and a enjoy the view.")

else:
    print("You tried to turn on the car and it blew up ! German engineering at its finest.")
    print("game over")






