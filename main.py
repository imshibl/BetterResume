import re

import spacy
import streamlit as st

from app import check_name, extract_human_languages, extract_resume
from app.utils import page_count_messages
from app.utils.regex_patterns import RegexPatterns as patterns

st.set_page_config(page_title="Better Resume", page_icon=":memo:", layout="wide")

# Check if the English language model is already installed
if "en_core_web_md" not in spacy.util.get_installed_models():
    # If it's not installed, download and install it
    spacy.cli.download("en_core_web_md")
    # Load the model after installation
    nlp = spacy.load("en_core_web_md")
else:
    # If it's already installed, you can simply load it
    nlp = spacy.load("en_core_web_md")


def app():
    st.title("Better Resume - CV Analyzer")
    st.subheader("Make sure your Resume is complete and ready to go!")

    st.markdown(
        """
        <div style="width: 100%; overflow-x: auto;">
            <p>Better Resume - CV Analyzer empowers job seekers to craft optimized CVs while aiding recruiters in efficiently analyzing candidates' qualifications. Leveraging advanced NLP techniques, it extracts key information from resumes, enabling better matches between job seekers and opportunities. With its intuitive interface and powerful algorithms, Better Resume transforms the hiring process, benefiting both candidates and recruiters alike.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    pdf_file = st.file_uploader("Select your Resume", type=["pdf"], key="resume")

    if pdf_file is not None:
        scan_button = st.button("Scan Resume")
        resume_uploaded_message = st.success("Uploaded Resume Successfully!")

        if scan_button:
            resume_uploaded_message.empty()
            resume_data, page_count = extract_resume.pdf_reader(pdf_file.getvalue())

            ### NAME
            name_match = re.search(patterns.name_pattern, resume_data)

            name = name_match.group(1) if name_match else None

            if name:
                is_name_an_english_word = check_name.check_name_is_not_english_word(
                    name, nlp
                )
                if is_name_an_english_word:
                    name = None
                else:
                    name = check_name.clean_name(name)
                    if name is not None:
                        st.subheader(f"Name : {name}")

            ### PAGE COUNT
            st.subheader(f"Page Count : {page_count}")
            page_count_info = page_count_messages.about_page_number_message()

            page_count_info_expand_button = st.expander(
                "How many pages do I need for my resume?"
            )
            with page_count_info_expand_button:
                for key, value in page_count_info.items():
                    st.write(f"{key} : {value}")

            ### LANGUAGES
            languages_match = re.search(patterns.languages_pattern, resume_data)
            has_language_section = bool(languages_match)

            if has_language_section:
                language_section_in_resume = resume_data[languages_match.end() :]
                languages, language_message = extract_human_languages.extract_languages(
                    language_section_in_resume
                )
                if len(languages) > 0:
                    st.subheader("Human Languages")

                    for lang in languages:
                        st.write(f"- {lang}")
                    st.write(language_message)
                else:
                    has_language_section = False
                    st.subheader("No Human Languages Found!")
                    st.text(language_message)

            st.success("Resume Scanned Successfully!")

    st.divider()

    st.markdown(
        """
        <style>
        .footer {
            position: absolute;
            width: 100%; 
            text-align: center;
           

        }
        .footer p {
            margin-bottom: 0;
        }
        </style>
        <div class="footer">
            <p>Developed By <a href="https://github.com/imshibl">BilCodes</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    app()
