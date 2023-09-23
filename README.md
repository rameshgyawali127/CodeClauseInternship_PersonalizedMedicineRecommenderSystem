# Personalized-Medicine-Recommender-System
### RAMESH GYAWALI


Objective :
The objective of this code is to create a graphical user interface (GUI) application for recommending medicines based on text data. It leverages natural language processing (NLP) and machine learning techniques to provide recommendations to users. The code reads a dataset of medicines from a CSV file, preprocesses the text data, computes cosine similarity between medicines based on their descriptions and reasons, and allows users to input a medicine name in the GUI to get recommendations for similar medicines.

Summary:

The code begins by importing necessary libraries, including NumPy, Pandas, Tkinter (for GUI), NLTK (Natural Language Toolkit), and scikit-learn modules.
It loads a dataset from a CSV file called 'medicine.csv' and drops rows with missing values which i took from Kaggle.
Text data in the 'Reason' and 'Description' columns is tokenized, preprocessed, and combined into a single 'tags' column.
Text data is converted to lowercase, and stemming is applied to reduce words to their base form.
A new DataFrame ('new_df') is created with relevant columns: 'index', 'Drug_Name', and 'tags'.
CountVectorizer is used to convert the text data into numerical vectors, and cosine similarity is calculated between medicines based on these vectors.
A recommendation function ('recommend') is defined to provide the top 5 recommended medicines for a given medicine name.
A GUI window is created using Tkinter, allowing users to input a medicine name.
Upon clicking the "Recommend" button, the code displays the recommended medicines based on similarity in the GUI.
Overall, this code combines text preprocessing, NLP, and machine learning to build a medicine recommendation system with a user-friendly GUI. Users can input a medicine name, and the system suggests similar medicines based on textual information from the dataset.
