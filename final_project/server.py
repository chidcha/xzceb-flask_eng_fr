from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    english_to_frenchtext= translator.english_to_french(textToTranslate)
    return english_to_frenchtext

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    french_to_englishtext= translator.french_to_english(textToTranslate)
    return french_to_englishtext

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
