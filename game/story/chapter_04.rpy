## ==============================================================================
## CHAPTER 4 — THE LAST ATTEMPT
## ==============================================================================

label chapter_04_start:

    scene bg black with fade
    pause 0.6

    centered "{size=36}{b}{color=#f2bc6a}CHAPTER 04{/color}{/b}{/size}\n\n{size=24}{color=#c4d5e2}THE LAST ATTEMPT{/color}{/size}"
    pause 1.8

    scene bg lantern_room with dissolve
    play music decision_theme loop fadein 2.0

    narrator "03:15 AM."

    narrator "The second storm struck Tarn Rock with the force of an artillery barrage."

    narrator "Giant breakers shattered against the base of the tower, sending tremors through one hundred and forty feet of granite masonry."

    show arthur exhausted at char_center with dissolve

    thought "The wind speed is clocking over eighty knots. The glass panes are flexing inward with every gust."

    thought "In my pocket is the final page torn from Elias Ward's desk ledger. The page he wrote minutes before he vanished."

    hide arthur with dissolve

    # Final words of Elias Ward
    narrator "Arthur pulled the creased parchment into the light of the mantle."

    journal "“November 2nd, 03:00. I understand now. The lighthouse is a regulator between two states of being.”"

    journal "“When the beam sweeps constantly, the barrier holds. But if the lens is aligned to 340 degrees and the mantle pressure raised to maximum, the light creates a bridge of solid ether.”"

    journal "“I spent six months trying to repair this tower for the Department. Every failure made me feel smaller, more worthless, more abandoned.”"

    journal "“The Evelyn offered me an escape. A place where my failures wouldn't follow me. I am locking the wheel now. God forgive me for leaving the light behind.”"

    show arthur concerned at char_center with dissolve

    thought "Ward didn't die by accident. He chose to walk away."

    thought "He let repeated failure convince him that he had no value left in the world of the living."

    thought "That is the exact same lie I told myself in Halifax when I packed my bags in the dark."

    hide arthur with dissolve

    # CHOICE 7: How Arthur views his purpose
    narrator "Arthur stood before the massive brass control wheel of the Fresnel assembly."

    menu:
        "Realize that failure is not the end, but the price of learning how to stand back up.":
            $ determination += 4
            $ lighthouse_condition += 15
            show arthur determined at char_center with dissolve

            thought "Ward gave in to despair. He thought one season of broken gears meant he was broken forever."

            thought "He was wrong. And I was wrong in Halifax."

            thought "Resilience isn't pretending you never made a mistake. Resilience is standing in the ruins, picking up the wrench, and building it right."

            hide arthur with dissolve

        "Feel the seductive pull of leaving your regrets and history behind forever.":
            $ trust_in_signal += 4
            show arthur exhausted at char_center with dissolve

            thought "Who can blame Ward? Thirty years of cold wind and salt spray, and when he needed help, they sent him broken scrap."

            thought "Out there on that phantom ship, no one asks about Halifax. No one asks why the light went out."

            hide arthur with dissolve

    # Climax transmission
    play sound radio_tuning
    pause 1.0
    play sound radio_static loop
    show evelyn signal at signal_display with dissolve

    radio "“Arthur... the storm is tearing the lantern roof away...”"

    radio "“The sea will swallow the island before dawn. Lock the wheel to three-forty. Cross over to us. We have a berth waiting for you.”"

    show arthur concerned at char_left with dissolve

    a "And what happens to the ships in the living Atlantic when another storm hits this rock?"

    radio "“They will find their own way... or they will join us. Let go of the burden, Arthur. You have failed enough for one lifetime.”"

    hide arthur
    hide evelyn
    stop sound fadeout 1.5

    # CHOICE 8: The Ultimate Fate of the Beacon
    scene bg lantern_room with dissolve

    narrator "The final moment arrived. The clockwork ticked down to zero three hundred."

    narrator "Between Arthur's hands lay the brass governance wheel, the emergency disconnect knife-switch, and the rain-slicked doorway to the outer catwalk."

    menu:
        "ENGAGE THE FULL SWEEP: Lock the regulator into normal rotation, restore the beacon for all living ships, and break the spectral connection.":
            $ determination += 5
            show arthur determined at char_center with dissolve

            thought "No. The light does not run away from the dark."

            thought "I am Arthur Hale, Keeper of Tarn Rock. And tonight, this light shines for the living!"

            hide arthur with dissolve
            jump ending_a_beacon

        "ALIGN THE BEAM TO THE SUNKEN SHORE: Lock the focal axis at 340 degrees and cross over to the Evelyn.":
            $ trust_in_signal += 5
            show arthur concerned at char_center with dissolve

            thought "Perhaps some falls cannot be undone. Perhaps peace is only found on the other side of the mist."

            thought "I will see what lies beyond the charts."

            hide arthur with dissolve
            jump ending_b_crossing

        "CUT THE BEACON AND MAINTAIN THE VIGIL: Extinguish the lens, sit at the radio, and become the permanent watcher between worlds.":
            $ knowledge_of_evelyn += 5
            $ determination += 2
            show arthur exhausted at char_center with dissolve

            thought "Neither world should be destroyed. But neither can cross."

            thought "Someone must sit in the dark and keep watch over both shores."

            thought "I will stay."

            hide arthur with dissolve
            jump ending_c_keeper
