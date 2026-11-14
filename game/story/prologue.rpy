## ==============================================================================
## PROLOGUE — THE ARRIVAL
## ==============================================================================

label prologue_start:

    scene bg black with fade
    pause 0.8

    centered "{size=36}{b}{color=#f2bc6a}PROLOGUE{/color}{/b}{/size}\n\n{size=24}{color=#c4d5e2}THE ARRIVAL{/color}{/size}"
    pause 1.8

    # Arrival at Tarn Rock
    play ambience storm_ambience fadein 2.5
    play sfx heavy_wind loop fadein 2.0
    scene bg island_arrival with dissolve

    narrator "November 14th."

    narrator "The North Atlantic does not forgive weakness. It merely waits for it."

    narrator "Forty miles off the Newfoundland coast, Tarn Rock rises from the icy black swells like an abandoned monolith."

    narrator "At its summit stands the lighthouse. For three generations, its sweeping beam kept ships off the jagged granite teeth below."

    play sound foghorn
    pause 2.5

    narrator "Six months ago, a catastrophic gale struck the island. The storm tore the copper roof from the lantern gallery, shattered the drive gears, and flooded the generator hall."

    narrator "For six months, the tower has stood completely dark."

    narrator "In those six months, four commercial freighters have vanished within twenty nautical miles of this rock. No wreckage. No oil slicks. No bodies."

    show arthur neutral at char_center with dissolve

    a "Six months of darkness... and now they expect one man to put it right."

    thought "The previous keeper, Elias Ward, spent thirty-two years on this station. After the storm, the Department sent replacement parts twice."

    thought "Ward tried repeatedly to rebuild the generator. He tried to rebuild the clockwork. Every attempt broke down. Every report he radioed to the mainland grew more despondent."

    thought "Three weeks ago, his transmissions stopped entirely. When the cutter arrived, the lighthouse was empty. Elias Ward had disappeared."

    hide arthur with dissolve

    # Move to exterior base
    play sound thunder
    scene bg lighthouse_exterior with fade

    narrator "Arthur stepped onto the slippery granite landing. The sea spray tasted of winter brine and iron."

    show arthur neutral at char_center with dissolve

    thought "I didn't take this posting because I was the best candidate. I took it because no one else was desperate enough to accept it."

    thought "A year ago, I was an assistant maritime engineer in Halifax. One critical miscalculation on a dry-dock boiler system, and an entire cargo vessel was condemned."

    show arthur concerned at char_center

    thought "I walked away. I couldn't face the inquiry, the ruined careers, the whispering in the halls. I ran."

    thought "Now, I am here. If I can restore this light—if I can bring fire back to this dead tower—maybe I can prove to myself that a fall isn't where a man's story has to end."

    hide arthur with dissolve

    # Enter the lighthouse
    play sound door_close
    stop sfx fadeout 2.0
    stop ambience fadeout 2.0

    scene bg keeper_room with dissolve
    play music exploration_theme loop fadein 3.0

    narrator "Inside, the air smelled of stale fuel, damp peat, and cold soot."

    narrator "On the keeper's drafting table lay tools, half-disassembled brass valves, and scribbled mechanical diagrams."

    show arthur neutral at char_center with dissolve

    thought "Ward was working right up until the moment he went missing."

    # CHOICE 1
    narrator "Arthur looked between the worktable, the mechanical log, and the dark hallway."

    menu:
        "Examine Ward's maintenance notes on the failed generator repairs.":
            $ curiosity += 1
            $ determination += 1
            $ knowledge_of_evelyn += 1
            show arthur concerned at char_center with dissolve

            logbook "“August 18th. Second replacement armature installed. Voltage spiked and melted the stator coils within twenty minutes. The generator rejects modern windings. It needs manual balancing.”"

            logbook "“October 4th. The problem isn't the copper or the fuel. The current leaks into the tower stone itself. Whenever the needle touches two hundred volts, the radio in the fourth alcove starts chattering.”"

            thought "Current leaking into the stone? That defies every principle of electrical grounding."

            hide arthur with dissolve

        "Check the fuel reserves and emergency survival supplies.":
            $ determination += 2
            $ lighthouse_condition += 5
            show arthur determined at char_center with dissolve

            thought "Focus on the basics first. If the fuel lines are contaminated, no generator will ever start."

            thought "The kerosene tanks in the cellar are intact. Sixty gallons of refined oil. Enough to run the auxiliary pumps if I can clear the sediment."

            thought "I won't let this station defeat me before I've even turned a wrench."

            hide arthur with dissolve

        "Ascend directly to the radio room to check the mainland link.":
            $ curiosity += 2
            $ trust_in_signal += 1
            show arthur suspicious at char_center with dissolve

            thought "If Ward disappeared without leaving a distress call, the communications gear might tell me what happened in his final hours."

            hide arthur with dissolve

    # Ascending to Radio Room
    scene bg staircase with dissolve
    play sound footsteps

    narrator "Arthur climbed the spiral iron stairway toward the mid-level communications room."

    scene bg radio_room with dissolve
    stop music fadeout 1.5
    play music mystery_theme loop fadein 2.5

    narrator "The radio room was freezing. The heavy Marconi transceiver sat on an oak workbench, its glass vacuum tubes cold and dark."

    show arthur neutral at char_center with dissolve

    thought "The mainland maritime relay operates on 2182 kHz. But the dial here is locked firmly at 142.80 kHz."

    hide arthur with dissolve

    # Sudden radio activation
    narrator "Without a hand touching the switches, the copper contacts inside the radio snapped shut."

    play sound switch_click
    pause 0.3
    play sound radio_static loop
    pause 1.0

    show evelyn signal at signal_display with dissolve

    narrator "A burst of electrical static hissed from the perforated brass speaker grille."

    play sound radio_tuning
    pause 1.5

    radio "“Mayday. Mayday. This is the Evelyn. We are approaching the coast. Can anyone hear us?”"

    show arthur shocked at char_left with dissolve

    a "What in God's name...?"

    thought "The Evelyn? The passenger liner that foundered in the great storm of 1948?"

    radio "“...Tarn Rock Light... our steering is compromised... we are running blind in the banks... please ignite the beacon... we cannot find the shore...”"

    thought "That ship went to the bottom thirty-eight years ago. There are no survivors. There is no ship!"

    narrator "The voice was not hysterical. It possessed a calm, terrifying intimacy that echoed through the stone chamber."

    radio "“...Arthur... the water is rising... do not leave the tower dark...”"

    stop sound fadeout 1.0
    hide evelyn
    hide arthur
    with dissolve

    narrator "The vacuum tubes died. The room plunged back into heavy, suffocating silence."

    thought "She spoke my name. I have been on this island for less than three hours."

    narrator "Outside, the wind shrieked against the dark tower, waiting to see if Arthur would run again."

    scene bg black with fade
    pause 1.2

    jump chapter_01_start
