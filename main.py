# Libraries Import
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import re
import nltk
from nltk.util import pr
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string
stop_word = set(stopwords.words("english"))

# Dataset Definition
try:
    df = pd.read_csv("twitterdata.csv")
    df['labels'] = df['class'].map({0: "Hate Speech Detected", 1: "Offensive Language Detected", 2: "No Hate Speech or Offensive Language"})
    df = df[['tweet', 'labels']]
except FileNotFoundError:
    print("Error: The file 'twitterdata.csv' was not found.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: The file 'twitterdata.csv' is empty.")
    exit()
except pd.errors.ParserError:
    print("Error: The file 'twitterdata.csv' could not be parsed.")
    exit()

# Function to clean the dataset
def clean(text_data):
    try:
        text_data = str(text_data).lower()
        text_data = re.sub('\[.*?\]', '', text_data)
        text_data = re.sub('https?://\S+|www\.\S+', '', text_data)
        text_data = re.sub('<.*?>+', '', text_data)
        text_data = re.sub('[%s]' % re.escape(string.punctuation), '', text_data)
        text_data = re.sub('\n', '', text_data)
        text_data = re.sub('\w*\d\w*', '', text_data)
        text_data = [word for word in text_data.split(' ') if word not in stop_word]
        text_data = " ".join(text_data)
        text_data = [stemmer.stem(word) for word in text_data.split(' ')]
        text_data = " ".join(text_data)
        return text_data
    except Exception as e:
        print(f"Error cleaning text data: {e}")
        return ""

# Creating Classifier
try:
    df["tweet"] = df["tweet"].apply(clean)
    df.dropna(inplace=True)
    x = np.array(df["tweet"])
    y = np.array(df["labels"])
    countv = CountVectorizer()
    x = countv.fit_transform(x)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)
except Exception as e:
    print(f"Error during model training: {e}")
    exit()

# Function to return output
def scanner(testdata):
    try:
        df = countv.transform([testdata]).toarray()
        return classifier.predict(df)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return ["Error"]
