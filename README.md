Students: Tal Yitzhak, Amal Abo Gush
Github Repository: https://github.com/talitz/Detecting-Cyber-Attacks-Kaggle-Callenge

Feature Engineering
We used CountVectorizer to convert a collection of text documents to a matrix of token counts (for 2 and 5 commands that come as one after another).
We used TFIDF to reflect how unique a command is (we looked at 2 and 5 commands that come as one after another).
Command’s length as a feature - didn’t work that well

Fitting Algorithms
We used 2-Class Classification Algorithms, and tried fitting & tuning them to the user’s data.

We tried the following models:
KNeighbors Classifier - implementing the k-nearest neighbors vote.
C-Support Vector Classification:
SVC (kernel = linear, C=0.025).
SVC (gamma=2).
SVC (gamma=auto, kernel=linear) - received the best results! :)
Gaussian Process Classifier (based on Laplace approximation).
Decision Tree Classifier.
Random Forest Classifier.
MLP Classifier (Multi-layer Perceptron Classifier).
AdaBoostClassifier.
Gaussian Naive Bayes.
Quadratic Discriminant Analysis.
