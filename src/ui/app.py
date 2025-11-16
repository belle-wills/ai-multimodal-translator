import sys
from pathlib import Path

# Ensure project root is on sys.path so "import src..." works
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # AI-Project root
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from src.core.translation_dictionary import PHRASES, TEXT_TO_ID, LANG_LABELS


st.set_page_config(page_title="AI Multimodal Translator – Text Prototype")

st.title("AI Multimodal Translator")
st.subheader("Step 1: Text-only prototype (no ML yet)")

st.write(
    "Type a supported phrase in **English, Welsh or Arabic** "
    "(e.g. 'hello', 'helo', 'shwmae', 'help me', 'diolch', 'مرحبا', 'مساعدة')."
)

user_text = st.text_input("Input phrase:")

if st.button("Translate") and user_text:
    key = user_text.strip().lower()

    phrase_id = TEXT_TO_ID.get(key)

    if phrase_id is None:
        st.error("I don't recognise that phrase yet. Try 'hello', 'helo', 'help me', 'diolch', 'مساعدة', etc.")
    else:
        phrase = PHRASES[phrase_id]
        translations = phrase["translations"]
        phonetics = phrase.get("phonetics", {})

        st.success(f"Recognised phrase ID: **{phrase_id}**")

        st.write("### Text translations")
        for lang_code, text in translations.items():
            label = LANG_LABELS.get(lang_code, lang_code)
            st.write(f"- **{label}:** {text}")
            if lang_code in phonetics:
                st.write(f"  - _phonetic_: {phonetics[lang_code]}")

        # Placeholder for sign language – later this will trigger video / animation
        sign_desc = phrase.get("sign")
        if sign_desc:
            st.write("### Sign language (placeholder)")
            st.write(sign_desc)
