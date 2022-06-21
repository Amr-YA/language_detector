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


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    text = "test if i'm working"

    try:
        lang = predict_model(text)
        if lang == "English":
            success= "true"
            status_code= 200
        else:
            success= "prediction error"
            status_code= 426            
    except Exception as e:
        success= "false"
        status_code= 500
        print(e)

    # obj = {"success": success, "status_code": status_code}
    obj = {"success": success}
    return jsonify(obj), status_code


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


    app.run(host="0.0.0.0", port="3000")

# %%
