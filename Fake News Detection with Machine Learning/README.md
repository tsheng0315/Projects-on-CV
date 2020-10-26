# Fake News Detection Using NLP and Machine Learning

* This project aims at detecting fake new using a Recurrent Neural Network. 

* Train a Long Short Term Memory (LSTM) network to detect fake news from a given news corpus. 

* This could be practically used by media companies to automatically predict whether the circulating news is fake or not. 

## Task 1: Understand the Problem Statement and business case

* Right now we are in a world of mis-information and fake news. This project aims at detecting fake news with Recurrent Neural Networks and LSTM (a type of Recurrent Neural Networks)

* Natural Language Processing (NLP) work by converting words(text) into numbers. 

* These numbers are then used to train an AI/ML model to make predictions.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Fake%20News%20Detection%20with%20Machine%20Learning/graphs/task%201%20intro.png)

It is like I'm going to make a binary classification to tell whether the input news is True/ Fake. 
 
## Task 2: Import libraries and datasets

* In this project, I'm going to use `Pandas` for dataframe manipulation, `Numpy` for numerical analysis, `Seaborn` and `matplotlib` for data visualisation, `nltk` and `gensim` for natural languages processing, on `tensorflow`(`keras`) platform.

* Import and check data: 

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%202%20true%20news.png)

* I find the number of record of our two dataset(fake news and true news) are almost same( 23481 and 21417 seperately). 
* This means I have balanced datasets. And there is no Null element(`isnull()` checking).

## Task 3: Perform Exploratory Data Analysis 

* For better data manipulation, I add a column `isfake` to indicate whether the news is real or fake. 

* Then I concatenate Real and Fake News to form a new table.

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%203%20concat%20two%20table%20into%20one%20table%20.png)

* Next, I combine `title` and `text` to create a new column together.

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%203%20title%2Btext.png)

## Task 4: Perform text data cleaning such as removing punctuation and stop words

* First, I add some stop words (stop words are words that occur in abundance, hence providing little to no unique information that can be used for classification or clustering and should be filtered out before processing of natural language data)

* Source of stopwords:

1. pre-defined stop words from `nltk` library
2. self-defined stop words
3. pre-defined stop words from `gensim` library

* Second, I remove stopwords from the content of `text`.

## Task 5: Perform exploratory data analysis and plot word-cloud for better visualization

* Visulalize the distribution of subjects of news

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%205%20show%20subject.png)

* Use word cloud to show the impotance of words in fake news

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%205%20fake%20news%20word%20cloud.png)


* Use word cloud to show the impotance of words in true news

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%205%20true%20new%20word%20cloud.png)

* Use a histograph to show the distribution of the length of a doc.

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%205%20length%20of%20one%20doc.png)

## Task 6: Perform tokenizing and padding on text corpus to feed the deep learning model.

* In this part I use tokenizing techniques to turn words into numbers for training and testing.

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%206%20token.png)

* Divide news data into training data set and testing data set.

* Create a tokenizer to tokenize the words and create sequences of tokenized words.

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%206%20encoding%20text%20.png)

* Add padding to make all news with the same length (either be maxlen = 4406 or smaller number maxlen = 40 ) seems to work well based on results.

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%206%20padding.png)

## Task 7: Understand the theory and intuition behind Recurrent Neural Networks and LSTM

#### Structure of RNN

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%207%20RNN%20into%201.png)

* The output will be feed back as input. 
* The output will not only depend on inputs but also depend on what happened in previous time, so we have some sort of memory effects

#### RNN works good with sequence of text 

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%207%20RNN%202%20architecture%20.png)

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%207%20rnn%203%20why%20special.png)

#### The Difference of input-output Networks

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%207%20rnn%204%20why%20special.png)

#### Gradient Descent

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%207%20rnn%205%20gradient%20descent.png)

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%207%20rnn%206%20gradient%20descent.png)

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%207%20rnn%207%20gradient%20descent.png)

#### Vanishing Gradient

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%207%20rnn%208%20vanishing%20gradient.png)

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%207%20rnn%209%20vanishing%20gradient.png)

## LSTM 

* RNN fails to hold long time memory, due to the vanishing gradient problem.
* If there are multiple layers inside a Recurrent Neural Network, in back-propagation we will find parameters stop to change at a point. 
* So turn to LSTM for help.

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%208%20LSTM.png)

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%208%20lstm%202.png)

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%208%20lstm%203.png)

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%208%20lstm%204.png)

## PCA technique to embed data

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%209%20-1.png)

## Task 8: Build and train the model

* Use TensorFlow 2.0 and keras to build our model. 

* The data is actually divided into several parts: 

|     Data   |               |                          |
|------------|---------------|--------------------------|
|  total data| training data | real training data       |
|            |               |crossing validation data  |
|            | testing data  |                          |

* Apply cross-validation to ensure the model to be generalised and is not overfitting. 

* The error on training data is decreasing , the error on validation data is decreasing, this means the model is not overfitting on training data. 

![](https://github.com/Gravel-yard/FakeNewsDetector-data/blob/main/graphs/task%209%20training%20result.png)

## Task 9: Assess the performance of trained model

My model reached an accuracy of on testing data set.  


