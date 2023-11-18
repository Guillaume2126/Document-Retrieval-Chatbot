import re
import os
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import PyPDF2


def cleaning(sentence):
    """Explain function"""
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
    """Explain function"""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        num_pages = len(pdf_reader.pages)

        for page_number in range(num_pages):
            if page_number < num_pages:
                text += pdf_reader.pages[page_number].extract_text()

        return text

def process_pdfs_and_build_dictionary(directory_path):
    """Explain function"""
    document_texts = {}
    i=0

    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            pdf_text = extract_text_from_pdf(pdf_path)
            cleaned_text = cleaning(pdf_text)

            # Add the filename and cleaned text in a dictionnary
            document_texts[filename] = cleaned_text
            print(i)
            i += 1

    return document_texts
