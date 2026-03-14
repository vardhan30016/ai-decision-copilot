import pandas as pd
import PyPDF2

def load_data(file):

    filename = file.name

    # CSV
    if filename.endswith(".csv"):
        df = pd.read_csv(file)
        return df

    # Excel
    elif filename.endswith(".xlsx"):
        df = pd.read_excel(file)
        return df

    # TXT
    elif filename.endswith(".txt"):
        text = file.read().decode("utf-8")
        return text

    # PDF
    elif filename.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text()

        return text

    else:
        return "Unsupported file type"