from sklearn.metrics.pairwise import linear_kernel
from data_cleaning import cleaning
import pandas as pd
import os
import joblib

# Function to find the document similar to the request
def get_most_similar_documents(query, tfidf_matrix, tfidf_vectorizer, top_n=5):
    """Cleaning of a sentence and use of a model to calculate the similarity
    between the query and PDF's documents"""
    data_path = "../Data/"
    df = pd.read_excel(os.path.join(data_path, "output_all_batches.xlsx"))
    df["Clean text"].fillna("", inplace=True)

    # Clean and vectorize the request
    query = cleaning(query)
    query_vector = tfidf_vectorizer.transform([query])

    # Calculate the similarity between the request and all the documents
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()

    # Sort by similarity
    document_indices = cosine_similarities.argsort()[:-top_n-1:-1]

    # Create a DataFrame with the results
    result_df = df.iloc[document_indices].copy()

    # Add a column for similarity scores
    result_df["Similarity Score"] = cosine_similarities[document_indices]

    return result_df


def chatbot():
    """Chatbot that accept a query as input and document corresponding
    to the query as output"""
    tfidf_matrix = joblib.load("tfidf_matrix.joblib")
    tfidf_vectorizer = joblib.load("tfidf_vectorizer.joblib")
    print("Welcome to this document retrieval chatbot !")
    while True:
        user_query = input("What information do you need (or write 'exit' to quit) ? ")
        if user_query.lower() == 'exit':
            print("Thank you and goodbye !")
            break
        else:
            similar_documents = get_most_similar_documents(user_query, tfidf_matrix, tfidf_vectorizer)
            print("Documents corresponding to the request :")
            print(similar_documents[["Name of the document", "Similarity Score"]])

if __name__ == "__main__":
    chatbot()
