# Import required libraries

import csv
import os
import re
import nltk
import scipy
import sklearn.metrics
import sentiment
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#Generating the Training and testing vectors

def getTrainingAndTestData():
	X = []
	y = []

		#Training data 1: Sentiment 140
	f=open(r'./training_test.csv','r', encoding='ISO-8859-1')
	reader = csv.reader(f)

	for row in reader:
		X.append(row[5])
		y.append(1 if (row[0]=='4') else 0)


	X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y,test_size=0.20, random_state=42)
	return X_train, X_test, y_train, y_test

#Process Tweets (Stemming+Pre-processing)

def processTweets(X_train, X_test):
	X_train = [sentiment.stem(sentiment.preprocessTweets(tweet)) for tweet in X_train]
	X_test = [sentiment.stem(sentiment.preprocessTweets(tweet)) for tweet in X_test]
	return X_train,X_test

# SVM classifier

def classifier(X_train,y_train):
	vec = TfidfVectorizer(min_df=5, max_df=0.95, sublinear_tf = True,use_idf = True,ngram_range=(1, 2))
	X_train
	svm_clf =svm.LinearSVC(C=0.1,loss='l2')
	vec_clf = Pipeline([('vectorizer', vec), ('pac', svm_clf)])
	vec_clf.fit(X_train,y_train)
	joblib.dump(vec_clf, 'svmClassifier.pkl')
	return vec_clf

# Main function

def main():
	X_train, X_test, y_train, y_test = getTrainingAndTestData()
	X_train, X_test = processTweets(X_train, X_test)
	vec = TfidfVectorizer()#min_df=5, max_df=0.95, sublinear_tf = True,use_idf = True,ngram_range=(1, 2))
	X_train=vec.fit_transform(X_train)
	X_test=vec.fit_transform(X_test)
	lb=LabelEncoder()
	y=lb.fit_transform(y_train)
	y_train=vec.fit_transform(y)
	y1=lb.fit_transform(y_test)
	y_test=vec.fit_transform(y1)
	svm_clf =svm.LinearSVC(C=0.1,loss='l2')
	vec_clf = Pipeline([('vectorizer', vec), ('pac', svm_clf)])
	svm_clf.fit(X_train,y_train)
	joblib.dump(vec_clf, 'svmClassifier.pkl')
	y_pred = svm_clf.predict(X_test)
	print(sklearn.metrics.classification_report(y, y_pred))

if __name__ == "__main__":
	main()
