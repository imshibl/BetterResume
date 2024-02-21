from .utils import human_languages


def extract_languages(resume_text):
    extracted_languages = [
        lang
        for lang in human_languages.languages
        if lang.lower() in "".join(resume_text.split()).lower()
    ]

    if len(extracted_languages) > 1:
        message = "Impressive! Your resume indicates proficiency in multiple languages. Highlighting diverse language skills can be a valuable asset."
    elif len(extracted_languages) == 1:
        message = "Your resume indicates proficiency in only one language. Consider adding more language skills to enhance your profile."
    else:
        message = "Your resume does not indicate any language skills. Consider adding language skills to enhance your profile."

    languages = list(set(extracted_languages))

    return languages, message
