## ==============================================================================
## CHAPTER 3 — THE IMPOSSIBLE COAST
## ==============================================================================

label chapter_03_start:

    scene bg black with fade
    pause 0.6

    centered "{size=36}{b}{color=#f2bc6a}CHAPTER 03{/color}{/b}{/size}\n\n{size=24}{color=#c4d5e2}THE IMPOSSIBLE COAST{/color}{/size}"
    pause 1.8

    scene bg staircase with dissolve
    play sound footsteps
    play sfx machinery loop fadein 1.5

    narrator "Arthur leaped up the narrow stone stairway. The cold draft from below met an intense blast of heated air pouring from the summit."

    narrator "He shoved open the iron hatch into the summit lantern room."

    # Summit Lantern Room
    scene bg lantern_room with dissolve
    play music decision_theme loop fadein 2.5

    narrator "The massive Fresnel lens was shuddering on its mercury bath. One of the brass rotation gears was jammed with carbon slag from Ward's failed welding attempt."

    show arthur concerned at char_center with dissolve

    thought "The generator power is feeding into the carriage, but the mechanical drive is locked. If I don't clear the gear teeth immediately, the motor will burn out!"

    # CHOICE 5: Mechanical repair under pressure
    menu:
        "Risk your hands to manually pry the seized gear loose with a cold chisel.":
            $ determination += 3
            $ lighthouse_condition += 20
            $ lens_repaired = True
            show arthur determined at char_center with dissolve

            thought "No hesitation. Don't freeze up like you did in Halifax."

            narrator "Arthur wedged the hardened steel chisel between the snarled gear teeth and hammered the butt with a brass mallet."

            play sound switch_click
            pause 0.4

            narrator "With a sharp metallic snap, the obstruction sheared away. The massive three-ton crystal carousel broke free and began rotating smoothly."

            narrator "The pressurized kerosene mantle flared into brilliant white incandescence!"

            hide arthur with dissolve

        "Dampen the electrical throttle to clear the jam safely from a distance.":
            $ curiosity += 2
            $ lighthouse_condition += 10
            show arthur suspicious at char_center with dissolve

            thought "Steady. Brute force will only crack the cast bronze housing."

            narrator "Arthur stepped to the electrical bypass panel and eased the rheostat lever back."

            narrator "The torque relaxed just enough for the jammed gear to slip past the burr. The mantle sputtered, then caught, casting a warm amber glow through the prisms."

            hide arthur with dissolve

    # The Light sweeps across the ocean
    scene bg storm_ocean with flash_beam

    narrator "For the first time in six months, the beacon of Tarn Rock cut through the Atlantic night."

    narrator "A concentrated pencil of white light sliced into the swirling wall of fog."

    narrator "Then the beam swept across 340 degrees north-northwest."

    scene bg impossible_coastline with flash_beam

    narrator "Arthur froze. His breath fogged against the curved glass."

    show arthur shocked at char_center with dissolve

    a "Merciful God..."

    narrator "Where only empty, deep ocean should have stretched for thousands of miles, a colossal, impossible shoreline materialized in the beam."

    narrator "Sheer basalt cliffs rose from the froth like cathedral buttresses. Along their ledges stood towering Victorian stone terraces, arched aqueducts, and empty iron piers."

    narrator "Pale, greenish gaslamps flickered along cobblestone promenades that ended abruptly over the abyss."

    thought "It isn't a mirage. It has texture, shadow, mass."

    thought "The lighthouse beam isn't just revealing that coast... the light is literally projecting it into existence."

    hide arthur with dissolve

    # Ghost ship appears
    scene bg ghost_ship with dissolve

    narrator "And out of the unnatural still water beneath those phantom cliffs, gliding toward the edge of the light, came the ship."

    narrator "The SS Evelyn. Two raked funnels belching silent grey smoke. Her black iron hull streaked with thirty-eight years of ocean rust."

    narrator "Her decks were lined with the faint, silhouetted forms of passengers, standing motionless at the teak railings."

    show arthur shocked at char_center with dissolve

    thought "She didn't sink. She crossed over when the light struck her thirty-eight years ago."

    thought "Elias Ward didn't die of exposure on the rocks. He opened the light, saw that world, and stepped into it."

    hide arthur with dissolve

    # Radio speaks personally to Arthur
    play sound radio_static loop
    show evelyn signal at signal_display with dissolve

    narrator "The brass speaking tube on the lantern frame shuddered. The radio transmission roared into the room."

    radio "“Arthur... you fixed the gear. You made the light return.”"

    show arthur concerned at char_left with dissolve

    thought "The voice. It's so clear now."

    radio "“Elias gave up, Arthur. After six months of darkness, he stopped believing he could finish what he started. He let the failure break him.”"

    radio "“He abandoned the lighthouse just as you abandoned your ship in Halifax.”"

    show arthur shocked at char_left

    a "How do you know about Halifax?!"

    radio "“The sea that holds us is made of all the things men leave behind. Broken promises. Ruined works. Unfinished lives.”"

    radio "“You don't belong to the living shore anymore, Arthur. Bring the light to bear. Anchor us to the stone... and cross over.”"

    # CHOICE 6: Confronting the transmission
    menu:
        "Defiantly reject the ghost's appeal; declare your allegiance to the living world.":
            $ determination += 3
            $ trust_in_signal -= 2
            show arthur determined at char_left

            a "No! Halifax was a disaster, but I am not running away again!"

            a "I was sent here to protect real mariners on real water. I will not trade my life for a city of ghosts!"

            radio "“...a brave voice, Arthur... but the second storm is already upon you... let us see if your light survives the gale...”"

        "Acknowledge the sorrow of the Evelyn; question what happened to Elias Ward.":
            $ curiosity += 2
            $ knowledge_of_evelyn += 2
            $ trust_in_signal += 1
            show arthur concerned at char_left

            a "Where is Elias Ward? Did he find peace on that shore, or is he trapped like the rest of you?"

            radio "“Elias sits on the pier every evening, Arthur. Waiting for the light to bring someone strong enough to join him...”"

            radio "“He couldn't finish the work. Can you?”"

    stop sound fadeout 1.5
    hide evelyn
    hide arthur
    with dissolve

    narrator "The transmission dissolved into static as the gale outside intensified into a violent screech."

    play sound thunder
    scene bg evelyn_final with dissolve

    narrator "Through the glass, the towering black bow of the Evelyn was now less than a hundred yards away, riding the edge of the phantom beam."

    narrator "The true test of the lighthouse keeper was about to begin."

    scene bg black with fade
    pause 1.2

    jump chapter_04_start
