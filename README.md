# Document Retrieval Chatbot

## Description

This project is a document retrieval chatbot that helps users find relevant
materials among a collection of documents. It uses a TF-IDF-based similarity
model to return the most relevant documents for a user query.

## General information

### Problem Statement

In our daily work and life, we often accumulate a large number of materials and
data. Organizing and finding these materials efficiently can be challenging.
The goal is to create a chatbot that allows users, especially office workers in
large companies who create many documents, to search for specific materials
using keywords they can remember.

### Data

- Exactly 997 documents as PDF files

### Librairies

- Please see the "requirements.txt" file

### Usage

1. Run the main script: `python chatbot.py`
2. Enter your user query when prompted.
3. View the documents corresponding to the query.


## Project Summary

### 1. Data Preparation

- Extraction of zip files
*(see Notebooks/data cleaning and preprocessing.ipynb and Application/data_cleaning.py)*

- Data mining and visualization *(see Notebooks/exploration.ipynb)*

- Cleaned the text data (Remove numbers, characters, tokenize, remove stopwords, etc...)
*(see Notebooks/data cleaning and preprocessing.ipynb and Application/data_cleaning.py)*

- Loaded the clean dataset in 10 Excel files and merged them
*(see Notebooks/Construct model.ipynb)*


### 2. Model Building - TF-IDF Approach
*(see Notebooks/Construct model.ipynb and Application/chatbot.py)*

- Utilized the TF-IDF (Term Frequency-Inverse Document Frequency) approach to vectorize the text data.
- Implemented a function, `get_most_similar_documents`, which calculates the similarity between a user query and documents in the dataset using linear kernel and returns the most similar documents.

### 3. Saving Models
*(see Notebooks/Construct model.ipynb)*

- Saved the TF-IDF vectorizer and matrix using joblib for later reuse.

### 4. Chatbot Implementation
*(see Application/chatbot.py)*

- Developed a simple chatbot script using the TF-IDF model.
- Loaded the TF-IDF vectorizer and matrix in the chatbot script.
- The chatbot prompts the user for information needs, and based on the user's query, it returns the most similar documents.

### 5. Testing the Chatbot

- Tested the chatbot by querying information like "How to use an oven."
- Observed the output, including document names, clean text, and similarity scores.

### 6. Possible Improvements

- Perform preprocessing for various languages to enhance multilingual support.
- Implement a feature to provide direct access links to the relevant documents for user convenience.



**Feel free to contribute and suggest further improvements to enhance the functionality and user experience of the chatbot.**
