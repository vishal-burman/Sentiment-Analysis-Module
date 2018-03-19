#Author-Vishal Burman
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sentiment_mod as s
import random

question_words = ["what", "when", "why", "which", "who", "how", "whose", "whom", "?"]

for i in range(0, 3):

    w = input("Enter the sentence:")

    w = w.lower()

    word_token = word_tokenize(w)

    filtered_sentence = []

    flag = 0


    for q in word_token:
        if q not in question_words:
            flag = 0
        else:
            flag = 1
            break


    if flag == 1:
        print("This sentence is interrogative!")
    else:
        print(s.sentiment(w))