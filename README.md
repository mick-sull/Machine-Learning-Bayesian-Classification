# Machine-Learning-Bayesian-Classification
Naive Bayes classifiers are among the most successful known algorithms for learning to classify text documents. The primary technical objective of this assignment is to provide an implementation of a Multinomial Naive Bayes learning algorithm in Python for document classification.
The dataset you will be using consists of movie reviews from IMDB (Internet Movie Database). It contains two folders. One called neg, which contains negative movie reviews and the other called pos which contains positive movie reviews. The objective of your Naïve Bayes algorithm is to correctly classify unseen movie reviews as positive or negative.

# Stage 1 – File Parsing and Vocabulary Composition
Develop code for reading all files from both the positive and negative subfolders. You should store all unique words in a vocabulary. You should also record the frequency with which words occur in both the positive and negative movie reviews.

# Stage 2 – Calculating Word Probability Calculations
You must work out the conditional probabilities for all words in the vocabulary for each class. In other words for each word w you should work out the P(w|positive) and P(w|negative). These are the required probabilistic components of the Naïve Bayes classifier. Again this information can be stored in a dictionary data structure.

# Stage 3 – Classifying Unseen Documents and Basic Evaluation
The final section of your code will take as input a new document (a movie review that has not been used for training the algorithm) and classify the document as a positive or negative review. You will need to read all words from the document and determine the probability of that document being a positive review and negative review using the multinomial model.
