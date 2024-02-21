import streamlit as st

st.set_page_config(page_title="Better Resume", page_icon=":memo:", layout="wide")
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)


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
