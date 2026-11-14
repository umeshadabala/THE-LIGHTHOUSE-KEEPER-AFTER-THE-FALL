## ==============================================================================
## THE LIGHTHOUSE KEEPER: AFTER THE FALL
## Main Entry Point
## ==============================================================================

label start:

    # Reset all story state variables
    $ reset_story_state()

    # Stop any menu music and begin with black silence
    stop music fadeout 1.5
    scene bg black with fade

    pause 1.0

    # Cinematic Title Card
    centered "{size=48}{b}{color=#f2bc6a}THE LIGHTHOUSE KEEPER{/color}{/b}{/size}\n\n{size=28}{color=#c4d5e2}AFTER THE FALL{/color}{/size}\n\n\n{size=20}{i}{color=#8ea4b8}“Even after the darkest night, the light can return.”{/color}{/i}{/size}"

    pause 2.5

    # Jump to Prologue
    jump prologue_start
