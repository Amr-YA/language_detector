#%%
import unicodedata
from flask import Flask, request, jsonify
from cleaner import Cleaner

import pickle
# from sklearn.preprocessing import LabelEncoder
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB

import warnings
warnings.simplefilter("ignore")
#%%
def predict_model(text):
    x = cv.transform([text]).toarray()
    lang = model.predict(x)
    lang = le.inverse_transform(lang)
    return(lang[0])


app = Flask(__name__)
@app.route("/predict", methods=["POST"])
def predict():

    text = request.json["message"]
    sender = request.json["sender"]
    text = Cleaner.clean(text)

    text_cleared = text[:10].replace(" ","")
    arabic_score = 0
    for char in text_cleared[:5]:
        if unicodedata.name(char).split()[0] == "ARABIC":
            arabic_score +=1

    lang = predict_model(text)
    if arabic_score > len(text_cleared)*0.5:
        lang = "Arabic"



    obj = {"sender": sender, "lang": lang_map[lang]}
    return jsonify(obj)

    """
    if len(text)<8 :
        text2 = text.replace(" ","")
        score = 0
        for char in text2:
            if unicodedata.name(char).split()[0] == "ARABIC":
                score +=1
        if score > len(text2)*0.5:
            return("Arabic")
        # else:
        #     return(predict_model(text))
    # else:
    #     return(predict_model(text))
    return(predict_model(text))
    """


#%%
if __name__ == "__main__":
    cleaner = Cleaner()
    model = pickle.load(open("models/detector.sav", "rb"))
    le = pickle.load(open("models/map.sav", "rb"))
    cv = pickle.load(open("models/tokenizer.sav", "rb"))
    lang_map = {
                "English": "en",
                "Danish": "da",
                "French": "fr",
                "German": "ge",
                "Hindi": "hi",
                "Italian": "it",
                "Portugeese": "po",
                "Russian": "ru",
                "Spanish": "sp",
                "Sweedish": "sw",
                "Turkish": "tu",
                "Arabic": "ar"
                }


    app.run(host="0.0.0.0", port="5005")

# %%
