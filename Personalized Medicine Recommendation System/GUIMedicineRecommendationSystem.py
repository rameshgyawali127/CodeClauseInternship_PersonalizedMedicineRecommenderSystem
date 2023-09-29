import numpy as np
import pandas as pd
import pickle
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from warnings import filterwarnings
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Suppress warnings
filterwarnings("ignore")

# Load the dataset
df = pd.read_csv('medicine.csv')

# Drop rows with missing values
df.dropna(inplace=True)

# Tokenize and preprocess text data
df['Reason'] = df['Reason'].apply(lambda x: x.split())
df['Description'] = df['Description'].apply(lambda x: x.split())
df['Description'] = df['Description'].apply(lambda x: [i.replace(" ", "") for i in x])#if descriptionn had a word like "anti inflammatory, it would be transformed into "antiinflammatory.
df['tags'] = df['Description'] + df['Reason']

# Combine tokens into a single string
df['tags'] = df['tags'].apply(lambda x: " ".join(x))

# Convert to lowercase
df['tags'] = df['tags'].apply(lambda x: x.lower())

# Initialize Porter Stemmer
ps = PorterStemmer()

# Stem text data
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

df['tags'] = df['tags'].apply(stem)

# Create a new DataFrame with relevant columns
new_df = df[['index', 'Drug_Name', 'tags']]

# Initialize CountVectorizer
cv = CountVectorizer(stop_words='english', max_features=5000)

# Fit and transform text data
vectors = cv.fit_transform(new_df['tags']).toarray()

# Calculate cosine similarity
similarity = cosine_similarity(vectors)

# Function to recommend medicines
def recommend(medicine):
    try:
        medicine_index = new_df[new_df['Drug_Name'] == medicine].index[0]
        distances = similarity[medicine_index]
        medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_meds = [new_df.iloc[i[0]].Drug_Name for i in medicines_list]
        return recommended_meds
    except IndexError:
        return ["No recommendations found. Please enter a valid medicine name."]


# Create a GUI window
root = tk.Tk()
root.title("Medicine Recommender")

# Function to display recommendations in the GUI
def show_recommendations():
    medicine_name = entry.get()
    if not medicine_name:
        messagebox.showerror("Error", "Please enter a medicine name.")
    else:
        recommendations = recommend(medicine_name)
        result_label.config(text="Recommended Medications:")
        for i, med in enumerate(recommendations):
            result_label.config(text=result_label.cget("text") + f"\n{i+1}. {med}")

# Create and configure GUI elements
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

label = ttk.Label(frame, text="Enter a Medicine:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = ttk.Entry(frame)
entry.grid(row=0, column=1, padx=5, pady=5)

recommend_button = ttk.Button(frame, text="Recommend", command=show_recommendations)
recommend_button.grid(row=0, column=2, padx=5, pady=5)

result_label = ttk.Label(frame, text="")
result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
