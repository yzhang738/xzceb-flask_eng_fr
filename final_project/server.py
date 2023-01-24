from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request
#from machinetranslation import english_to_french, french_to_english, convert_dic_to_str
import json 

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    fr_translated_text = english_to_french(textToTranslate)
    return fr_translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    en_translated_text = french_to_english(textToTranslate)
    return en_translated_text

@app.route("/index")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
