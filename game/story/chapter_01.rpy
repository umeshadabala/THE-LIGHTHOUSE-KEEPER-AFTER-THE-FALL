## ==============================================================================
## CHAPTER 1 — THE FALL
## ==============================================================================

label chapter_01_start:

    scene bg black with fade
    pause 0.6

    centered "{size=36}{b}{color=#f2bc6a}CHAPTER 01{/color}{/b}{/size}\n\n{size=24}{color=#c4d5e2}THE FALL{/color}{/size}"
    pause 1.8

    scene bg keeper_room with dissolve
    play music exploration_theme loop fadein 2.5

    narrator "04:15 AM."

    narrator "Arthur sat at the wooden desk, staring at the blueprints spread out before him."

    narrator "His hands were black with machine grease. Beside him lay a cracked brass governor valve and an unfinished wiring schematic penciled in Elias Ward's unsteady hand."

    show arthur exhausted at char_center with dissolve

    thought "The generator in the lower cellar is a disaster. The primary rotor shaft is scored, the copper commutators are oxidized, and the drive belts are frayed to ribbons."

    thought "Ward tried to rebuild it at least four times. Every time, he pushed the machine too hard, blew the bypass valve, and had to start from scratch."

    thought "I know that feeling. The suffocating weight of watching your work crumble right in front of your eyes."

    hide arthur with dissolve

    # Flashback / Introspection on Past Failure
    scene bg black with dissolve

    narrator "Arthur closed his eyes. The memory of Halifax returned with razor sharpness."

    narrator "The boiler test on the cargo carrier {i}SS Laurentian{/i}. He had noticed the pressure relief gauge fluctuating at dusk. He was tired. He had convinced himself it was merely a faulty spring."

    narrator "At midnight, the main steam header ruptured. Scalding vapor tore through the lower engineering deck. Two stokers barely escaped with third-degree burns. The ship's engine room was gutted."

    show arthur concerned at char_center with dissolve

    thought "The board called it gross negligence. They were right. But what hurt worse was what I did next."

    thought "I didn't stay to rebuild the plant. I didn't face the men in the hospital. I packed my sea chest and disappeared into the night."

    thought "For twelve months, I hid in boarding houses, convinced that any machine I touched would break. Convinced that I was a coward who folds under pressure."

    hide arthur with dissolve

    # Return to the present
    scene bg keeper_room with dissolve

    show arthur neutral at char_center with dissolve

    thought "Now here I am on an island where the light has been dead for six months. With a ghost ship calling on a dead frequency."

    thought "If I fail here, ships will continue to vanish on these shoals. And I will have proven that running away is the only thing I know how to do."

    hide arthur with dissolve

    # Investigation & Choice 2
    narrator "On the desk lay two things: the station's emergency telegraph transmitter to the Cape Race Coast Guard station, and Ward's heavy steel tool kit."

    narrator "Arthur faced the defining crossroad of his first night."

    menu:
        "Commit to rebuilding the generator; refuse to give up or abandon the station.":
            $ determination += 3
            $ lighthouse_condition += 15
            $ past_failure_acknowledged = True
            show arthur determined at char_center with dissolve

            thought "No. Not this time. I am not walking away."

            thought "If Ward's rotor commutators are oxidized, I'll sand them down with emery paper. If the governor valve is cracked, I'll re-seat the brass sleeve."

            thought "A fall only becomes permanent when you refuse to get back on your feet."

            narrator "Arthur grabbed a pair of iron pliers and the soldering iron. For the next three hours, he worked without stopping."

            narrator "He stripped the fouled copper leads, recalibrated the fuel injector, and re-poured the babbitt bearing by the light of a single tallow candle."

            play sound machinery
            pause 1.5

            narrator "Deep in the stone cellar, the heavy diesel engine coughed, spat black smoke, and settled into a steady, resonant thrum."

            thought "One system restored. The heart of the lighthouse is beating again."

            hide arthur with dissolve

        "Call Cape Race to report the lighthouse unserviceable and request immediate evacuation.":
            $ determination -= 2
            $ trust_in_signal += 1
            show arthur exhausted at char_center with dissolve

            thought "Who am I trying to fool? I am one man with broken tools. Ward had thirty years of experience and he couldn't fix it."

            thought "Why should I succeed where a master keeper failed?"

            narrator "Arthur powered the Cape Race auxiliary crystal on the Marconi bench."

            play sound radio_tuning
            pause 1.2

            a "Cape Race, this is Tarn Rock Light. Station condition critical. Generator ruined, lantern mechanism seized. I am requesting emergency relief."

            narrator "The speaker hissed with static, then Mara's sharp, incredulous voice responded."

            mara "“Tarn Rock, say again? Hale, your cutter left six hours ago. There is a Force 9 blizzard bearing down from Labrador. No vessel can reach that rock for at least four days.”"

            mara "“Ward said the exact same words before he went silent. If you don't get that generator turning, your water pipes will freeze and you won't survive the week. Do you hear me, Arthur? You have to fix it yourself.””"

            thought "No rescue. No escape boat. The world has shut the door behind me."

            thought "If I want to survive... I have no choice but to rebuild it anyway."

            $ determination += 1
            $ lighthouse_condition += 10
            hide arthur with dissolve

        "Investigate Ward's personal living quarters for hidden spare parts and answers.":
            $ curiosity += 3
            $ knowledge_of_evelyn += 1
            $ lighthouse_condition += 5
            show arthur suspicious at char_center with dissolve

            thought "Before I burn out my strength on stripped bolts, I need to know why Ward's repairs failed."

            thought "A seasoned keeper doesn't blow four generators in a row unless something else is interfering with the load."

            narrator "Arthur picked up his storm lantern and approached the heavy oak door leading to Ward's private quarters."

            hide arthur with dissolve

    # Transition to Ward's quarters
    play sound door_close
    scene bg black with fade
    pause 1.0

    jump chapter_02_start
