#AIM : To Build Personalized-Medicine-Recommender-System
### AURTHOR -> RAMESH GYAWALI

Objective :
    The objective of this code is to create a graphical user interface (GUI) application for recommending medicines based on text data. It leverages natural 
    language processing (NLP) and machine learning techniques to provide recommendations to users. The code reads a dataset of medicines from a CSV file, 
    preprocesses the text data, computes cosine similarity between medicines based on their descriptions and reasons, and allows users to input a medicine name in 
    the GUI to get recommendations for similar medicines.

    
The algorithms used in this Recommender-System are :
1. Feature Extraction:

     The code uses the scikit-learn library's CountVectorizer to convert the preprocessed text data (medicine descriptions) into numerical vectors.
     Each medicine's textual information is transformed into a numerical vector that represents the frequency of words in the text. This vectorization process is a 
     common step in NLP and machine learning.
2. Cosine Similarity Calculation:

     After vectorizing the textual data, the code calculates Cosine Similarity between the vectors representing different medicines.
     Cosine Similarity measures the cosine of the angle between two vectors and is commonly used to measure the similarity between documents or items in a high- 
     dimensional space.
     In this code, the Cosine Similarity matrix is computed, where each cell (i, j) represents the similarity score between medicine i and medicine j based on 
     their 
     textual descriptions.
3. Recommendation Function:

     The recommend function uses the Cosine Similarity matrix to find the most similar medicines to a given medicine.
     It calculates the similarity scores (distances) between the input medicine and all other medicines in the dataset.
     It then sorts the medicines based on their similarity scores in descending order.
     The top 5 most similar medicines (excluding the input medicine itself) are recommended based on these scores.

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
    Overall, this code combines text preprocessing, NLP, and machine learning to build a medicine recommendation system with a user-friendly GUI. Users can input a 
    medicine name, and the system suggests similar medicines based on textual information from the dataset.
