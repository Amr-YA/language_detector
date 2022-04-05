#%%
from tabnanny import verbose
import pandas as pd
import numpy as np
import re
import string

from cleaner import Cleaner

import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#%%
# loading dataset:
data_set = "data/languages.csv"
data = pd.read_csv(data_set)
print(data.head(10))
print(data["Language"].value_counts())

#%%
"""
arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
punctuations_list = arabic_punctuations + english_punctuations
translator = str.maketrans('', '', punctuations_list)
url_pattern = re.compile('https?://\S+|www\.\S+')

def cleaner(sentance):
    text = re.sub(r'[[]]', ' ', sentance)
    text = text.lower()
    text = url_pattern.sub(r'', text) # remove URLs
    text = text.translate(translator) # remove punc
    text = re.sub('[0-9]', '', text)
    return text.strip()
"""
cleaner = Cleaner()
data['Text_clean'] = data['Text'].apply(cleaner.clean)

#%%
# Construct X, y
X_train, X_test, y_train, y_test = train_test_split(data['Text_clean'], data["Language"], 
                                                    random_state=42, 
                                                    test_size=0.1,
                                                    stratify=data["Language"].values)

#%%
cv = CountVectorizer()
X_train_ids = cv.fit_transform(X_train).toarray()
X_test_ids = cv.transform(X_test).toarray()

le = LabelEncoder()
y_train_ids = le.fit_transform(y_train)
y_test_ids = le.transform(y_test)
#%%
print(X_train_ids.shape, y_train_ids.shape)
print(X_test_ids.shape, y_test_ids.shape)
#%%
def print_scores(name, model):
    y_pred = model.predict(X_test_ids)
    y_true = y_test_ids
    print(f"{name} model scores:")
    print("Accuracy: ", accuracy_score(y_true, y_pred))
    print("f1-score: ", f1_score(y_true, y_pred, average='weighted'))
    print("Precision: ", precision_score(y_true, y_pred, average='weighted' ))
    print("Recall: ", recall_score(y_true, y_pred, average='weighted'))
    print("\n")

#%%
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_ids, y_train_ids)
print_scores("Naive-Bayes", naive_bayes)
"""
Naive-Bayes model scores:
Accuracy:  0.970125786163522
f1-score:  0.9700389228748256
Precision:  0.971863757231902
Recall:  0.970125786163522
"""
#%%
bag_mod = BaggingClassifier(n_estimators=200)
bag_mod.fit(X_train_ids, y_train_ids)
print_scores("Bagging", bag_mod)
"""
Bagging model scores:
Accuracy:  0.9182389937106918
f1-score:  0.9172754850099429
Precision:  0.9235551618926304
Recall:  0.9182389937106918
"""
#%%
rf_mod = RandomForestClassifier(n_estimators=200)
rf_mod.fit(X_train_ids, y_train_ids)
print_scores("Random Forest", rf_mod)
"""
Random Forest model scores:
Accuracy:  0.940251572327044
f1-score:  0.9399414469372429
Precision:  0.9448486324921759
Recall:  0.940251572327044
"""
#%%
ada_mod = AdaBoostClassifier(n_estimators=300, learning_rate=0.2)
ada_mod.fit(X_train_ids, y_train_ids)
print_scores("AdaBoost", ada_mod)
"""
AdaBoost model scores:
Accuracy:  0.8244234800838575
f1-score:  0.8177240913789224
Precision:  0.8689477493622644
Recall:  0.8244234800838575
"""
#%%
svm_mod = SVC()
svm_mod.fit(X_train_ids, y_train_ids, verbose=1)
print_scores("SVM Classifier", svm_mod)
"""
SVM Classifier model scores:
Accuracy:  0.899895178197065
f1-score:  0.8983032910057367
Precision:  0.9140863505429896
Recall:  0.899895178197065
"""
#%%
def save_model(model):
    pickle.dump(model, open('models/detector.sav', 'wb'))
    pickle.dump(le, open('models/map.sav', 'wb'))
    pickle.dump(cv, open('models/tokenizer.sav', 'wb'))

save_model(naive_bayes)
#%%
def predict(text, model):
    text = cleaner.clean(text)
    x = cv.transform([text]).toarray()
    lang = model.predict(x)
    lang = le.inverse_transform(lang)
    print("langauge:", lang[0])

text = "مين انت"
predict(text, naive_bayes)
    

# %%
