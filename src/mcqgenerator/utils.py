import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.page:
                text += page.extract_text()
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            raise Exception("Error reading the PDF file.")
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception("Unsupported file format")


def get_table_data(quiz_str):
    try:
        #quiz_str = """{"1": {"no": "1", "mcq": "What is machine learning?", "options": {"a": "A discipline of artificial intelligence that enables machines to learn from data and make predictions", "b": "The process of explicitly programming machines to perform tasks", "c": "A method of training computers to imitate natural human traits", "d": "The ability to apply complex mathematical calculations to available data"}, "correct": "a"}, "2": {"no": "2", "mcq": "How do machine learning methods enable computers to operate autonomously?", "options": {"a": "By relying on predetermined equations as models", "b": "By leveraging algorithms to identify patterns and learn from data", "c": "By imitating natural human traits like learning from examples", "d": "By using deep learning algorithms"}, "correct": "b"}, "3": {"no": "3", "mcq": "What is the sub-domain of machine learning that offers better performance parameters than conventional ML algorithms?", "options": {"a": "Deep learning", "b": "Natural language processing", "c": "Computational finance", "d": "Computer vision"}, "correct": "a"}, "4": {"no": "4", "mcq": "What is one of the main reasons why machine learning has become essential today?", "options": {"a": "The rise of big data, IoT, and ubiquitous computing", "b": "The ability to apply complex mathematical calculations automatically", "c": "The use of machine learning during World War II", "d": "The development of the Enigma Machine"}, "correct": "a"}, "5": {"no": "5", "mcq": "In which field can machine learning be used for predictive maintenance?", "options": {"a": "Computational finance", "b": "Computer vision", "c": "Automotive, aerospace, and manufacturing", "d": "Natural language processing"}, "correct": "c"}}"""
        # convert the quiz from a str to dict
        # print(quiz_str)
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append(
                {"MCQ": mcq, "Choices": options, "Correct": correct})
        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False


print(get_table_data(""))
