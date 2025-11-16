
# Human-friendly labels for language codes
LANG_LABELS = {
    "en": "English",
    "cy": "Welsh",
    "ar": "Arabic",
    # add more languages later, e.g. "fr": "French"
}

# Core phrase dictionary
# Each phrase has:
# - translations:  language_code -> written phrase
# - phonetics:     language_code -> phonetic helper (optional)
# - sign:          description or ID for a sign animation (placeholder for now)
PHRASES = {
    "HELLO": {
        "translations": {
            "en": "Hello",
            "cy": "Helo",
            "ar": "مرحبا",
        },
        "phonetics": {
            "cy": "helo",
            "ar": "marhaban",
        },
        "sign": "Standard greeting wave (👋)",
    },
    "HELP_ME": {
        "translations": {
            "en": "Help me",
            "cy": "Helpa fi",        
            "ar": "ساعدني",  
        },
        "phonetics": {
            "cy": "helpa fie",
            "ar": "say-edni",           
        },
        "sign": "Both hands raised slightly, palms forward (HELP)",
    },
    "THANK_YOU": {
        "translations": {
            "en": "Thank you",
            "cy": "Diolch",
            "ar": "شكرا",
        },
        "phonetics": {
            "cy": "dee-olch",
            "ar": "shukran",
        },
        "sign": "Flat hand from chin moving outwards (THANK YOU)",
    },
    "THANK_YOU_VERY_MUCH": {     # FIXED: new required entry
        "translations": {
            "en": "Thank you very much",
            "cy": "Diolch yn fawr iawn",
            "ar": "شكرا جزيلا",
        },
        "phonetics": {
            "cy": "dee-olch un vowr yah-un",
            "ar": "shukran jazeelan",
        },
        "sign": "Start with a flat hand at the chin (standard THANK YOU), move it forward. Repeat the movement with a larger, more expressive motion to show “very much”.",
    },
}

# Map raw user text → phrase ID.
# You can keep extending this with more synonyms in any language.
TEXT_TO_ID = {
    # HELLO
    "hello": "HELLO",      # Eng greeting
    "hi": "HELLO",        # Eng greeting 
    "helo": "HELLO",      # Welsh spelling
    "shwmae": "HELLO",    # Welsh greeting
    "مرحبا": "HELLO",      # Arabic hello 

    # HELP
    "help me": "HELP_ME",        # Eng "help"
    "helpa fi": "HELP_ME",    # Welsh "help"
    "ساعدني": "HELP_ME",     # Arabic help

    # THANK YOU
    "thank you": "THANK_YOU",  # Eng
    "thanks": "THANK_YOU",  # Eng
    "cheers": "THANK_YOU",  # Eng
    "diolch": "THANK_YOU",  #Welsh 
    "شكرا": "THANK_YOU", #Arabic
    
    # THANK YOU VERY MUCH
    "thank you very much": "THANK_YOU_VERY_MUCH",
    "diolch yn fawr iawn": "THANK_YOU_VERY_MUCH",  # Welsh
    "شكرا جزيلا": "THANK_YOU_VERY_MUCH",          # Arabic
}

