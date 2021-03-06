# -*- coding: utf-8 -*-
"""FakeNewsClassification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mQuVrcvQ5FPwWVHyAUdaQww8XimloS-U

# TASK 2: IMPORT LIBRARIES AND DATASETS
"""

!pip install --upgrade tensorflow-gpu==2.0

!pip install plotly
!pip install --upgrade nbformat
!pip install nltk
!pip install spacy   # spaCy is an open-source software library for advanced natural language processing
!pip install WordCloud
!pip install gensim  # Gensim is an open-source library for unsupervised topic modeling and natural language processing
import nltk # natural language tool
nltk.download('punkt')

import tensorflow as tf
import pandas as pd # dataframe manipulation
import numpy as np  # numerical analysis 
import matplotlib.pyplot as plt # data visualisation 
import seaborn as sns           # data visualisation 

from wordcloud import WordCloud, STOPWORDS
import nltk
import re
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

# import keras
from tensorflow.keras.preprocessing.text import one_hot, Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Embedding, Input, LSTM, Conv1D, MaxPool1D, Bidirectional
from tensorflow.keras.models import Model

# from jupyterthemes import jtplot
# jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False) 
# setting the style of the notebook to be monokai theme  
# this line of code is important to ensure that we are able to see the x and y axes clearly
# If you don't run this code line, you will notice that the xlabel and ylabel on any plot is black on black and it will be hard to see them.

# load the data
df_fake = pd.read_csv("https://raw.githubusercontent.com/Gravel-yard/FakeNewsDetector-data/main/data/Fake.csv")
df_true = pd.read_csv("https://raw.githubusercontent.com/Gravel-yard/FakeNewsDetector-data/main/data/True.csv")

df_fake

df_true

"""MINI CHALLENGE #1: 
- Indicate how many data samples do we have per class (i.e.: Fake and True)
- List how many Null element are present 
- List the memory usage for each dataframe
"""

df_true.isnull().sum()

df_fake.isnull().sum()

df_true.info() # memory usage

"""# TASK 3: PERFORM EXPLORATORY DATA ANALYSIS"""

# add a target class column to indicate whether the news is real or fake
df_true['isfake'] = 0
df_true.head()

df_fake['isfake'] = 1
df_fake.head()

# Concatenate Real and Fake News
df = pd.concat([df_true, df_fake]).reset_index(drop = True)
# drop original index
df

df.drop(columns = ['date'], inplace = True)

# create a new column for combined content from "title" and "text" 
df['original'] = df['title'] + ' ' + df['text']
df.head()

df['original'][0]

"""# TASK 4: PERFORM DATA CLEANING"""

# download stopwords
nltk.download("stopwords")

# Obtain additional stopwords from nltk
from nltk.corpus import stopwords
stop_words = stopwords.words('english') # stopwords in English
# stop_words -> list
stop_words.extend(['from', 'subject', 're', 'edu', 'use']) # add my own stopwords

# Remove stopwords and remove words with 2 or less characters
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text,min_len=2): # split doc into tokens,ignore token < 2 characters
        if token not in gensim.parsing.preprocessing.STOPWORDS and token not in stop_words and len(token) > 3:
            result.append(token)            
    return result

# Apply the function to the dataframe
df['clean_text'] = df['original'].apply(preprocess)

# Show original news
df['original'][0]

# Show cleaned up news after removing stopwords
print(df['clean_text'][0])

df

# Obtain the total words present in the dataset
list_of_words = []
for row in df.clean_text:
    for element in row:
        list_of_words.append(element)

list_of_words

len(list_of_words)

# Obtain the total number of unique words
total_words_len = len( list (  set(list_of_words)  ) )
total_words_len

# join the words into a string
# Join all items in x into a string, using a space character as separator
df['clean_string'] = df['clean_text'].apply(lambda x: " ".join(x))
# df.apply()

df

df['clean_string'][0]

"""# TASK 5: VISUALIZE CLEANED UP DATASET"""

df

# plot the number of samples in 'subject'
# plt.figure(figsize = (7, 7))
sns.countplot(y = "subject", data = df)
plt.show()

"""- Plot the count plot for fake vs. true news"""

# plot the number of samples in 'subject'
# plt.figure(figsize = (7, 7))
sns.countplot(y = "isfake", data = df)
plt.show()

# plot the word cloud for text that is Real
plt.figure(figsize = (20,20)) 
wc = WordCloud(max_words = 2000 , width = 1600 , height = 800 , stopwords = stop_words).generate(" ".join(df[df.isfake == 0].clean_string))
plt.imshow(wc, interpolation = 'bilinear')

# plot the word cloud for text that is Fake
plt.figure(figsize = (20,20)) 
wc = WordCloud(max_words = 2000 , width = 1600 , height = 800 , stopwords = stop_words).generate(" ".join(df[df.isfake == 1].clean_string))
plt.imshow(wc, interpolation = 'bilinear')

# length of maximum document will be needed to create word embeddings 
maxlen = -1
for doc in df.clean_string:
    tokens = nltk.word_tokenize(doc)
    if(maxlen<len(tokens)):
        maxlen = len(tokens)
print("The maximum number of words in any document is =", maxlen)

# visualize the distribution of number of words in a text
import plotly.express as px
fig = px.histogram(x = [len(nltk.word_tokenize(x)) for x in df.clean_string], nbins = 100)
fig.show()

"""# TASK 6: PREPARE THE DATA BY PERFORMING TOKENIZATION AND PADDING"""

# split data into test and train 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df.clean_string, df.isfake, test_size = 0.2)
# input and output of model

from nltk import word_tokenize

# Create a tokenizer to tokenize the words and create sequences of tokenized words
tokenizer = Tokenizer(num_words = total_words_len)
tokenizer.fit_on_texts(x_train) 
# encoding based on training data
train_sequences = tokenizer.texts_to_sequences(x_train)
# convert text into number
test_sequences = tokenizer.texts_to_sequences(x_test)
# convert text into number

print("The encoding for document\n", df.clean_string[0], "\n is : ",train_sequences[0])

len(train_sequences)

len(test_sequences)

# Add padding can either be maxlen = 4406 or smaller number maxlen = 40 seems to work well based on results
padded_train = pad_sequences(train_sequences, maxlen = 4405, padding = 'post', truncating = 'post')
padded_test = pad_sequences(test_sequences, maxlen = 4405,  padding = 'post', truncating = 'post') 
padded_test[:2]

for index, doc in enumerate(padded_train[:2]):
  # line 1& line 2
     print("The padded encoding for document",index+1," is : ", doc)

"""# TASK 9: BUILD AND TRAIN THE MODEL"""

# Sequential Model
model = Sequential()

# embeddidng layer
model.add(Embedding(total_words_len, output_dim = 128))
# model.add(Embedding(total_words, output_dim = 240))


# Bi-Directional RNN and LSTM
model.add(Bidirectional(LSTM(128)))

# Dense layers
model.add(Dense(128, activation = 'relu'))
model.add(Dense(1,activation= 'sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.summary()

total_words_len

y_train = np.asarray(y_train)
# convert an given input to an array.

# train the model
model.fit(padded_train, y_train, batch_size = 64, validation_split = 0.1, epochs = 5)

"""- Change the embedding output dimension and print out the model summary
- How many trainable parameters are there?
"""

# Change the embedding size to 240 for example and print out the summary

"""# TASK 10: ASSESS TRAINED MODEL PERFORMANCE"""

# make prediction
pred = model.predict(padded_test)
# result is a probabilty as we used sigmod as activation function

pred

# set threshold: if the predicted value is >0.5 it is real else it is fake
prediction = []
for i in range(len(pred)):
    if pred[i].item() > 0.5:
        prediction.append(1)
    else:
        prediction.append(0)

# getting the accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(list(y_test), prediction)

print("Model Accuracy : ", accuracy)

# get the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(list(y_test), prediction)
plt.figure(figsize = (5, 5))
sns.heatmap(cm, annot = True)
plt.show()

# category dict
category = { 0: 'Fake News', 1 : "Real News"}

"""# CONGRATULATIONS!

MINI CHALLENGE #1
"""

# data containing real news
df_true
# data containing fake news
df_fake
# dataframe information
df_true.info()
# dataframe information
df_fake.info()
# check for null values
df_true.isnull().sum()
# check for null values
df_fake.isnull().sum()

"""MINI CHALLENGE #2:
- Perform sanity check on the prepocessing stage by visualizing at least 3 sample news
"""

df['original'][5]
df['clean_joined'][5]

"""MINI CHALLENGE #3: 
- Plot the count plot for fake vs. real news
"""

# plot the number of samples per each class
plt.figure(figsize = (8, 8))
sns.countplot(y = "isfake", data = df)