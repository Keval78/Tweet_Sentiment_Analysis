# Tweet_Sentiment_Analysis
**Update**(13 Oct. 2019): I don't actively maintain this repository. This work was done for a course project and the dataset cannot be released because I don't own the copyright.

## Dataset Information

We use and Support Vector Machine(SVM) for sentiment analysis on tweets (a binary classification problem). The training dataset is expected to be a csv file of type `tweet,sentiment` where `sentiment` is either `1` (positive) or `0` (negative), and `tweet` is the tweet enclosed in `""`. Similarly, the test dataset 20% part of same csv file. Please note that csv headers are not expected and should be removed from the training and test datasets.  

## Requirements

There are some general library requirements for the project and some which are specific to individual methods. The general requirements are as follows.  
* `numpy`
* `scikit-learn`
* `scipy`
* `nltk`
* `Django`
* `tweepy.API`
* `tweepy.Cursor`
* `googletrans`
* `TfidfVectorizer`

**-------Make Analysis Model(SVM) First-------**

### Preprocessing 

We have applied a set of pre-processing steps to make tweets suitable for SVM algorithm and improve performance. The following pre-processing has been done on the tweets:

i. Lower Case - Convert the tweets to lower case

ii. URLs - Convert www.* or https?://* to 'URL'

iii. @username - Convert username to '__HANDLE'

iv. #hashtag - Hash tags can give us some useful information, so we replace them with the exact same word without the hash. E.g. #Apple replaced with 'Apple'

v. Trimming the tweet

vi. Repeating words: People often use repeating characters while using colloquial language, such as "I’m happyyyyy". We replace characters repeating more than twice with just two characters, so that the result for above would be "I'm happyy"

**Stemming**
Stemming algorithms are used to find the “root word” or stem of a given word. We have used the Porter Stemmer.

**-------Creating Django Project-------**

**-------Create UI and Code for Downloading Tweets and Sentiment using Model-------**

Twitter allows us to mine the data of any user using Twitter API or Tweepy. The data will be tweets extracted from the user. The first thing to do is get the consumer key, consumer secret, access key and access secret from twitter developer available easily for each user. These keys will help the API for authentication.

Steps to obtain keys:
– Login to twitter developer section
– Go to “Create an App”
– Fill the details of the application.
– Click on Create your Twitter Application
– Details of your new app will be shown along with consumer key and consumer secret.
– For access token, click ” Create my access token”. The page will refresh and generate access token.

Tweepy is one of the library that should be installed using pip. Now in order to authorize our app to access Twitter on our behalf, we need to use the OAuth Interface. Tweepy provides the convenient Cursor interface to iterate through different types of objects. Twitter allows a maximum of 200 tweets for extraction.for next 200 tweets passed last tweet id to next request and continue downloading...

Load SVM pickel file and use it for classification of tweets.

If you want to use already generated pickel file you can download it from below link, it is generated using the same code that i have uploaded here.

https://drive.google.com/file/d/1PyeHdd8AJH5W9eJisltv2Zlba1zTBoNI/view


