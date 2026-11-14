## ==============================================================================
## THE LIGHTHOUSE KEEPER: AFTER THE FALL
## Character, Image, and Audio Definitions
## ==============================================================================

# ------------------------------------------------------------------------------
# Character Definitions
# ------------------------------------------------------------------------------
define narrator = Character(None)
define a = Character("Arthur", color="#8bb5d6", image="arthur")
define thought = Character("Arthur (Internal)", color="#729ec2", what_italic=True, image="arthur")
define e = Character("Elias Ward", color="#d4aa6a", image="elias")
define journal = Character("Ward's Journal", color="#c29b63", what_italic=True)
define logbook = Character("Lighthouse Log", color="#a3b8c2", what_italic=True)
define radio = Character("Radio Transmission", color="#48e0a0", what_italic=True, image="evelyn")
define evelyn = Character("Evelyn", color="#5fe0ad", what_italic=True, image="evelyn")
define mara = Character("Mara (Archivist)", color="#d89e78")

# ------------------------------------------------------------------------------
# Audio Definitions
# ------------------------------------------------------------------------------
init python:
    renpy.music.register_channel("sfx", mixer="sound", loop=True)
    renpy.music.register_channel("ambience", mixer="sound", loop=True)

define audio.radio_static = "audio/sfx/radio_static.wav"
define audio.radio_tuning = "audio/sfx/radio_tuning.wav"
define audio.foghorn = "audio/sfx/distant_foghorn.wav"
define audio.ocean_waves = "audio/sfx/ocean_waves.wav"
define audio.heavy_wind = "audio/sfx/heavy_wind.wav"
define audio.switch_click = "audio/sfx/switch_click.wav"
define audio.door_close = "audio/sfx/door_close.wav"
define audio.footsteps = "audio/sfx/footsteps.wav"
define audio.thunder = "audio/sfx/thunder.wav"
define audio.machinery = "audio/sfx/machinery.wav"

define audio.menu_theme = "audio/music/menu_theme.wav"
define audio.exploration_theme = "audio/music/exploration_theme.wav"
define audio.mystery_theme = "audio/music/mystery_theme.wav"
define audio.decision_theme = "audio/music/decision_theme.wav"
define audio.ending_theme = "audio/music/ending_theme.wav"
define audio.storm_ambience = "audio/ambience/storm_ambience.wav"
define audio.interior_ambience = "audio/ambience/interior_ambience.wav"

# ------------------------------------------------------------------------------
# Background Images
# ------------------------------------------------------------------------------
image bg main_menu = "images/backgrounds/main_menu.png"
image bg island_arrival = "images/backgrounds/island_arrival.png"
image bg lighthouse_exterior = "images/backgrounds/lighthouse_exterior.png"
image bg keeper_room = "images/backgrounds/keeper_room.png"
image bg radio_room = "images/backgrounds/radio_room.png"
image bg staircase = "images/backgrounds/staircase.png"
image bg lantern_room = "images/backgrounds/lantern_room.png"
image bg storm_ocean = "images/backgrounds/storm_ocean.png"
image bg ghost_ship = "images/backgrounds/ghost_ship.png"
image bg impossible_coastline = "images/backgrounds/impossible_coastline.png"
image bg evelyn_final = "images/backgrounds/evelyn_final.png"
image bg beacon_ending = "images/backgrounds/beacon_ending.png"
image bg crossing_ending = "images/backgrounds/crossing_ending.png"
image bg keeper_ending = "images/backgrounds/keeper_ending.png"
image bg black = Solid("#05080c")

# ------------------------------------------------------------------------------
# Character Sprites & Transforms
# ------------------------------------------------------------------------------
transform char_left:
    xalign 0.15
    yalign 1.0
    zoom 0.72

transform char_center:
    xalign 0.5
    yalign 1.0
    zoom 0.72

transform char_right:
    xalign 0.85
    yalign 1.0
    zoom 0.72

transform signal_display:
    xalign 0.5
    yalign 0.85
    zoom 0.65

image arthur neutral = Transform("images/characters/arthur_neutral.png", zoom=0.72, yalign=1.0)
image arthur concerned = Transform("images/characters/arthur_concerned.png", zoom=0.72, yalign=1.0)
image arthur suspicious = Transform("images/characters/arthur_suspicious.png", zoom=0.72, yalign=1.0)
image arthur shocked = Transform("images/characters/arthur_shocked.png", zoom=0.72, yalign=1.0)
image arthur exhausted = Transform("images/characters/arthur_exhausted.png", zoom=0.72, yalign=1.0)
image arthur determined = Transform("images/characters/arthur_determined.png", zoom=0.72, yalign=1.0)

image elias neutral = Transform("images/characters/elias_neutral.png", zoom=0.72, yalign=1.0)
image elias serious = Transform("images/characters/elias_serious.png", zoom=0.72, yalign=1.0)
image elias distressed = Transform("images/characters/elias_distressed.png", zoom=0.72, yalign=1.0)

image evelyn signal = Transform("images/characters/evelyn_signal.png", zoom=0.65, yalign=0.85)

# Visual transitions & camera pulses
define flash_beam = Fade(0.1, 0.0, 0.5, color="#fefbe8")
define radio_glitch = Dissolve(0.15)
