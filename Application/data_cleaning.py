import re
import os
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import PyPDF2

def cleaning(sentence):
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
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_number in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_number].extract_text()
    return text

def process_pdfs_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            pdf_text = extract_text_from_pdf(pdf_path)
            cleaned_text = cleaning(pdf_text)
            print(f"Cleaned Text for {pdf_path}:\n{cleaned_text}\n")
