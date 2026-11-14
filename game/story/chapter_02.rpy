## ==============================================================================
## CHAPTER 2 — THE KEEPER BEFORE HIM
## ==============================================================================

label chapter_02_start:

    scene bg black with fade
    pause 0.6

    centered "{size=36}{b}{color=#f2bc6a}CHAPTER 02{/color}{/b}{/size}\n\n{size=24}{color=#c4d5e2}THE KEEPER BEFORE HIM{/color}{/size}"
    pause 1.8

    scene bg keeper_room with dissolve
    play music exploration_theme loop fadein 2.5

    narrator "06:40 AM."

    narrator "A pale, lifeless daylight seeped through the sea-facing window, illuminating the dust motes hanging in Elias Ward's private chambers."

    narrator "The room was an intimate museum of one man's slow descent into obsession."

    show arthur neutral at char_center with dissolve

    thought "Ward wasn't just a mechanic. He was a scholar of this rock."

    thought "Bookshelves lined with nineteenth-century meteorological treatises, tide tables, and leather-bound journals spanning three decades."

    hide arthur with dissolve

    narrator "Behind a row of Admiralty gazetteers, Arthur discovered a concealed drawer in the wainscoting."

    narrator "Inside rested Ward's final journal, an envelope of aged monochrome photographs, a reel-to-reel magnetic tape player, and a hand-drawn nautical chart."

    show arthur concerned at char_center with dissolve

    # CHOICE 3: What to examine
    narrator "Arthur paused, weighing what clue to inspect first."

    menu:
        "Read Ward's personal handwritten journal from the beginning.":
            $ journal_pages_found = True
            $ determination += 1
            $ curiosity += 2
            $ knowledge_of_evelyn += 2

            thought "Let's see the mind of the man who held this post before me."

            narrator "Arthur flipped back to the early pages, dated five months ago, immediately following the catastrophic storm."

            journal "“May 2nd. The storm broke three gear-teeth on the revolving carriage. The lamp is dead. But I have weathered fifty gales on Tarn Rock. I will cast new teeth from bronze stock. A keeper does not despair.”"

            narrator "The handwriting was firm, steady, professional. But thirty pages later, in July, the script began to fray."

            journal "“July 14th. The third casting cracked under heat. I failed again. Every time I fail, the sea feels wider. At night, the radio clicks on 142 kHz. Static whispers. I heard a ship's bell ring four times in the speaker.”"

            journal "“September 28th. It is not my mechanical failure that keeps the lamp dark. The sea doesn't want the light to return. The Evelyn is out there in the fog, waiting for the seam to open.”"

            show arthur shocked at char_center

            thought "He tried and failed so many times that failure stopped being a mechanical problem. It became a haunting."

            hide arthur with dissolve

        "Listen to the reel-to-reel audio tape in the dispatch tin.":
            $ recording_played = True
            $ curiosity += 2
            $ trust_in_signal += 2
            $ knowledge_of_evelyn += 1

            thought "Ward left a tape ready on the spools. His own voice might tell the truth his pen couldn't."

            play sound switch_click
            pause 0.4
            play sound radio_static loop

            narrator "The magnetic tape dragged across the playback head. Elias Ward's voice filled the chilly room—gravelly, exhausted, trembling with suppressed dread."

            show elias serious at char_center with dissolve

            e "“October 22nd. If the Department is listening to this... you sent me broken parts because you thought I was slipping. You were wrong.”"

            e "“I was a young assistant keeper when the Evelyn went down in October '48. I remember the captain's distress call: {i}‘We see a white coast that is not Canada.’{/i}”"

            show elias distressed at char_center

            e "“For thirty-eight years, I thought it was sea madness. But six months ago, when our lantern died, the signal returned. The Evelyn didn't sink into the seabed. She slipped through the tear in the fog.”"

            e "“The lighthouse was never just a guide. It was the bolt on the door. Every time I try to repair the mechanism, she begs me to let her come through.”"

            stop sound fadeout 1.2
            hide elias with dissolve
            show arthur concerned at char_center with dissolve

            thought "The lighthouse as a bolt on a door... holding back something outside our reality."

            hide arthur with dissolve

        "Unroll the strange nautical chart with the unexplained coastline.":
            $ map_inspected = True
            $ knowledge_of_evelyn += 2
            $ curiosity += 2
            $ lighthouse_condition += 5

            thought "The map. Ward spent weeks measuring something with brass dividers."

            narrator "The parchment depicted Tarn Rock surrounded by concentric circles representing the Fresnel beam's radial sweep."

            narrator "To the north-northwest, sketched in fine violet ink, was a massive landmass titled {i}The Sunken Shore — Reach of St. Jude{/i}."

            show arthur suspicious at char_center with dissolve

            thought "Look at his marginal notes: {i}‘Focal convergence at 340 degrees true. When the power reaches 240 volts, the beam resonates at the water-line. The coast materializes.’{/i}"

            thought "He wasn't failing to fix the lighthouse. He was deliberately modifying the lens to project at an unnatural frequency!"

            hide arthur with dissolve

    # CHOICE 4: Psychological reflection on failure and resilience
    scene bg keeper_room with dissolve

    narrator "Arthur leaned back against the stone fireplace. Elias Ward's life on this rock had mirrored his own."

    narrator "Two men who had encountered a devastating failure. One had let the failure consume him until reality fractured; the other was standing at the edge of the same abyss."

    show arthur neutral at char_center with dissolve

    menu:
        "Refuse to repeat Ward's mistake; vow to ground yourself in reality and duty.":
            $ determination += 3
            $ trust_in_signal -= 1
            $ lighthouse_condition += 10
            show arthur determined at char_center with dissolve

            thought "Ward gave in to despair. When he couldn't fix the machinery, he invented a ghost ship to explain his helplessness."

            thought "I did the same thing in Halifax—I blamed the gauges and the boiler inspectors instead of owning my mistake."

            thought "I am not following him into madness. I will repair this lighthouse for the living, not the dead."

            hide arthur with dissolve

        "Recognize that Ward discovered a genuine mystery, and prepare to confront whatever lies in the fog.":
            $ curiosity += 2
            $ trust_in_signal += 2
            $ determination += 1
            show arthur concerned at char_center with dissolve

            thought "Ward wasn't just hallucinating. The radio signal spoke my name before I touched a single tool."

            thought "If there really is a fold in the ocean—if the Evelyn is trapped out there—then fixing this lighthouse means more than just turning on a lamp."

            thought "It means facing the impossible without running away."

            hide arthur with dissolve

    # Escalation from the tower summit
    play sound thunder
    play sfx machinery loop fadein 2.0

    narrator "High above in the tower, the heavy iron counterweights of the lantern room dropped with a shuddering crash."

    narrator "The auxiliary circuits Arthur had repaired in the cellar surged with sudden electrical power."

    thought "The power grid! The current is flowing upstairs to the lantern carriage!"

    narrator "Arthur snatched his heavy coat and raced toward the spiral stairway."

    scene bg black with fade
    pause 1.0

    jump chapter_03_start
