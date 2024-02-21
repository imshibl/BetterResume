import re

import streamlit as st

from app import check_name, extract_human_languages, extract_resume
from app.utils.regex_patterns import RegexPatterns as patterns

st.set_page_config(page_title="Better Resume", page_icon=":memo:", layout="wide")


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

            name_match = re.search(patterns.name_pattern, resume_data)
            name = name_match.group(1) if name_match else None

            if name:
                name = check_name.clean_name(name)
                st.subheader(f"Name : {name}")
            else:
                st.subheader("Name : Unknown")

            st.subheader(f"Page Count : {page_count}")

            languages, message = extract_human_languages.extract_languages(resume_data)
            st.subheader("Human Languages")
            for lang in languages:
                st.write(f"- {lang}")
            st.write(message)

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
