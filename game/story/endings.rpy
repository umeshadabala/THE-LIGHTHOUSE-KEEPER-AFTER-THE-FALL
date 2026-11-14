## ==============================================================================
## EPILOGUE — THREE ENDINGS
## ==============================================================================

# ==============================================================================
# ENDING A: THE BEACON (The Bounce Back)
# ==============================================================================
label ending_a_beacon:

    stop music fadeout 2.0
    scene bg black with fade
    pause 1.0

    centered "{size=36}{b}{color=#f2bc6a}ENDING A{/color}{/b}{/size}\n\n{size=26}{color=#c4d5e2}THE BEACON{/color}{/size}\n\n{size=20}{i}{color=#8ea4b8}“Even after the darkest night, the light can return.”{/color}{/i}{/size}"
    pause 2.5

    scene bg lantern_room with dissolve
    play music ending_theme loop fadein 3.0
    play sfx machinery loop fadein 2.0

    narrator "Arthur stepped to the governing mechanism with steady, unwavering hands."

    narrator "He seized the brass handwheel, wrenched it clear of the 340-degree lock pin, and dropped the governor weights into their balanced slots."

    play sound switch_click
    pause 0.5

    narrator "The massive three-ton Fresnel carousel swung into its true, rhythmic sweep: one revolution every fifteen seconds."

    scene bg storm_ocean with dissolve

    narrator "As the brilliant white beam fanned across the boiling black swells, its focal intensity broadened. It no longer pierced into another reality."

    narrator "It illuminated the Atlantic Ocean—violent, perilous, but profoundly real."

    play sound radio_static
    show evelyn signal at signal_display with dissolve

    radio "“...Arthur... the light is turning... we cannot hold our footing...”"

    show arthur determined at char_left with dissolve

    a "Rest now, Evelyn. The living need this light."

    radio "“...you did not run, keeper... you stayed... you put the pieces back together...”"

    radio "“...we will sleep now... in the deep...”"

    stop sound fadeout 3.0
    hide evelyn with dissolve
    hide arthur with dissolve

    narrator "The radio gave one final, gentle click and went completely silent."

    narrator "Outside, the spectral towers, the impossible docks, and the ghost ship Evelyn dissolved like salt in water, swallowed by the ocean spray."

    pause 1.5

    # Dawn breaks over the Atlantic
    scene bg beacon_ending with fade

    narrator "06:45 AM."

    narrator "Dawn broke over the North Atlantic in streaks of pale gold, amber, and steel blue."

    narrator "For the first time in six months, the beacon of Tarn Rock had burned through the night without failing."

    show arthur neutral at char_center with dissolve

    thought "At 08:00, the radio on the Cape Race channel buzzed to life. Mara's voice came through, clear and astonished."

    thought "She told me that a coastal freighter caught in the storm had spotted our light twenty miles out, changed course, and skirted the reef safely."

    thought "She asked me how I managed to rebuild the generator and unseize the lens in a Force 9 blizzard alone."

    show arthur determined at char_center

    thought "I picked up the microphone. I told her the truth: that when a machine falls, you don't curse the dark. You get back on your feet and turn the wrench."

    thought "Halifax is behind me now. Not forgotten, but redeemed."

    thought "I am Arthur Hale. And as long as I draw breath, the light on this rock will never go out again."

    hide arthur with dissolve

    pause 2.0
    scene bg black with fade

    centered "{size=32}{color=#f2bc6a}A fall is only the beginning of standing up.{/color}{/size}\n\n{size=26}{color=#c4d5e2}The beacon shines once more over the living sea.{/color}{/size}\n\n\n{size=20}{color=#8ea4b8}— ENDING A: THE BEACON (COMPLETED) —{/color}{/size}"

    pause 3.5
    stop music fadeout 2.5

    return


# ==============================================================================
# ENDING B: THE CROSSING
# ==============================================================================
label ending_b_crossing:

    stop music fadeout 2.0
    scene bg black with fade
    pause 1.0

    centered "{size=36}{b}{color=#f2bc6a}ENDING B{/color}{/b}{/size}\n\n{size=26}{color=#c4d5e2}THE CROSSING{/color}{/size}\n\n{size=20}{i}{color=#8ea4b8}“Leaving the world behind.”{/color}{/i}{/size}"
    pause 2.5

    scene bg lantern_room with dissolve
    play music mystery_theme loop fadein 3.0

    narrator "Arthur gripped the steering wheel and pulled the locking pin home at 340 degrees true."

    play sound switch_click

    narrator "The intense white beam locked dead on the phantom shoreline."

    scene bg impossible_coastline with dissolve

    narrator "The storm outside vanished instantly into a breathless, supernatural hush."

    narrator "The violent waves between Tarn Rock and the impossible city froze into a polished floor of black obsidian glass, reflecting the faint green streetlamps of the phantom piers."

    scene bg evelyn_final with dissolve

    narrator "At the base of the cliffs, the SS Evelyn rested against the stone wharf. Her gangway descended with a gentle ring of brass."

    show arthur concerned at char_center with dissolve

    narrator "Arthur walked down the iron staircase. On the keeper's desk, he laid his brass service badge beside Elias Ward's empty coffee cup."

    hide arthur with dissolve

    scene bg crossing_ending with fade

    narrator "He walked across the glass surface of the sea. Standing by the gangway railing was Elias Ward, a quiet, knowing smile resting beneath his grey beard."

    show elias neutral at char_right with dissolve

    e "“You came, Arthur. You realized the world of men asks for more than a soul can bear.”"

    show arthur neutral at char_left with dissolve

    a "Does the regret stay behind on the island?"

    e "“Nothing crosses this water except what you choose to carry.”"

    hide elias with dissolve
    hide arthur with dissolve

    narrator "Arthur stepped onto the teak deck. Behind them, high on the dark island, the empty lighthouse beam burned out into the night, pinning the gateway open."

    narrator "The Evelyn cast off into the glowing horizon, leaving the centuries behind."

    pause 2.0
    scene bg black with fade

    centered "{size=32}{color=#f2bc6a}They crossed where the sea was no longer water.{/color}{/size}\n\n{size=26}{color=#c4d5e2}And no keeper was ever found on Tarn Rock again.{/color}{/size}\n\n\n{size=20}{color=#8ea4b8}— ENDING B: THE CROSSING (COMPLETED) —{/color}{/size}"

    pause 3.5
    stop music fadeout 2.5

    return


# ==============================================================================
# ENDING C: THE KEEPER
# ==============================================================================
label ending_c_keeper:

    stop music fadeout 2.0
    scene bg black with fade
    pause 1.0

    centered "{size=36}{b}{color=#f2bc6a}ENDING C{/color}{/b}{/size}\n\n{size=26}{color=#c4d5e2}THE KEEPER{/color}{/size}\n\n{size=20}{i}{color=#8ea4b8}“The endless watch.”{/color}{/i}{/size}"
    pause 2.5

    scene bg lantern_room with dissolve
    play music decision_theme loop fadein 2.5

    narrator "Arthur reached up to the main kerosene cut-off lever."

    narrator "He did not let the beam cross into the city of ghosts, nor did he let it shine blindly across the reefs."

    play sound switch_click

    narrator "He yanked the lever down. The white incandescent mantle died."

    scene bg storm_ocean with dissolve

    narrator "Darkness enveloped the Atlantic once more. Outside, the phantom coastline receded into the freezing mist, holding its breath."

    # Radio room vigil
    scene bg radio_room with dissolve
    play music exploration_theme loop fadein 2.5

    narrator "Arthur descended the spiral stairs to the radio room."

    narrator "He sat in the worn oak chair. He slipped the heavy bakelite headphones over his ears."

    show arthur exhausted at char_center with dissolve

    play sound radio_static loop
    show evelyn signal at signal_display with dissolve

    narrator "The static on 142.80 kHz settled into a gentle, rhythmic hum—a pulse that sounded like the breath of the ocean."

    radio "“...Arthur... you chose to stay...”"

    a "Someone has to listen. Someone has to keep the watch between the worlds."

    radio "“...then we will wait together...”"

    hide arthur
    hide evelyn
    stop sound fadeout 2.0
    with dissolve

    scene bg keeper_ending with fade

    narrator "Days blurred into months. Months dissolved into seasons."

    narrator "Arthur never grew tired. The oil in the lamp never dwindled. The ink on his pen never dried."

    narrator "Every night at 02:14, the dials hum."

    narrator "And one day, decades from now, another weary soul will step off a dory onto the black granite, searching for a place to start over after a fall."

    narrator "And Arthur will be waiting at the dials to say his name."

    pause 2.0
    scene bg black with fade

    centered "{size=32}{color=#f2bc6a}The watch has no beginning.{/color}{/size}\n\n{size=26}{color=#c4d5e2}And the watch will have no end.{/color}{/size}\n\n\n{size=20}{color=#8ea4b8}— ENDING C: THE KEEPER (COMPLETED) —{/color}{/size}"

    pause 3.5
    stop music fadeout 2.5

    return
