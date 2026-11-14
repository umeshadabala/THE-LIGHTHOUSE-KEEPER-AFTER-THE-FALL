## ==============================================================================
## THE LIGHTHOUSE KEEPER: AFTER THE FALL
## Global Story Variables & Progression State
## ==============================================================================

# Core thematic and psychological variables
default determination = 0
default curiosity = 0
default trust_in_signal = 0
default lighthouse_condition = 0
default knowledge_of_evelyn = 0
default understanding = 0

# Story progression & discovery flags
default generator_examined = False
default generator_fixed = False
default journal_pages_found = False
default recording_played = False
default map_inspected = False
default transmission_answered = False
default lens_repaired = False
default past_failure_acknowledged = False
default mara_contacted = False
default signal_frequency_tuned = False

init python:
    def reset_story_state():
        global determination, curiosity, trust_in_signal, lighthouse_condition, knowledge_of_evelyn
        global generator_examined, generator_fixed, journal_pages_found, recording_played
        global map_inspected, transmission_answered, lens_repaired, past_failure_acknowledged
        global mara_contacted, signal_frequency_tuned

        determination = 0
        curiosity = 0
        trust_in_signal = 0
        lighthouse_condition = 0
        knowledge_of_evelyn = 0

        generator_examined = False
        generator_fixed = False
        journal_pages_found = False
        recording_played = False
        map_inspected = False
        transmission_answered = False
        lens_repaired = False
        past_failure_acknowledged = False
        mara_contacted = False
        signal_frequency_tuned = False
