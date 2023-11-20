import re
import os
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pypdfium2 as pdfium
import pandas as pd

def cleaning(sentence):
    """Function to clean a text"""
    # Basic cleaning
    sentence = re.sub(r'<.*?>', '', sentence)
    sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)  # Remove numbers and characters
    sentence = sentence.strip()  # Remove whitespaces
    sentence = sentence.lower()  # Lowercase

    # Advanced cleaning
    for punctuation in string.punctuation:
        sentence = sentence.replace(punctuation, '')  # Remove punctuation

    tokenized_sentence = word_tokenize(sentence)  # Tokenize
    stop_words = set(stopwords.words('english'))  # Define stopwords

    tokenized_sentence_cleaned = [w for w in tokenized_sentence if w not in stop_words]

    lemmatized = [WordNetLemmatizer().lemmatize(word) for word in tokenized_sentence_cleaned]

    cleaned_sentence = ' '.join(word for word in lemmatized)
    cleaned_sentence = re.sub(r'\s+', ' ', cleaned_sentence)  # Remove multiple spaces

    return cleaned_sentence


def extract_text_from_pdf(pdf_path):
    """Function to extract the text from a pdf"""
    # Open the PDF document
    pdf = pdfium.PdfDocument(pdf_path)

    # Initialize an empty string to store the extracted text
    extracted_text = ""

    # Iterate through each page in the PDF
    for page_number in range(len(pdf)):
        # Get the current page
        page = pdf[page_number]

        # Load the page's text content
        text_page = page.get_textpage()

        # Extract text from the whole page
        text_all = text_page.get_text_range()

        # Append the extracted text to the overall text
        extracted_text += text_all

    return extracted_text


def process_pdfs_and_build_dataframe(directory_path, start_index=0, end_index=None):
    document_texts = {"Name of the document": [], "Clean text": []}

    # List of files in the repository
    pdf_files = [filename for filename in os.listdir(directory_path) if filename.endswith(".pdf")]

    if end_index is None:
        end_index = len(pdf_files)
    else:
        end_index = min(end_index, len(pdf_files))

    for i in range(start_index, end_index):
        filename = pdf_files[i]
        pdf_path = os.path.join(directory_path, filename)
        pdf_text = extract_text_from_pdf(pdf_path)
        cleaned_text = cleaning(pdf_text)

        document_texts["Name of the document"].append(filename)
        document_texts["Clean text"].append(cleaned_text)
        print(f"Document {i + 1}")

    document_df = pd.DataFrame(document_texts)

    document_df["Clean text"] = document_df["Clean text"].apply(cleaning)

    return document_df
