import os
from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd
from PIL import Image
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelBinarizer

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
app = Flask(__name__)

model = load_model("final_model.h5")
csv_filename = "combined_labels.csv"
df = pd.read_csv(csv_filename)
label_mapping = {
    1: "అ", 2: "ఆ", 3: "ఇ", 4: "ఈ", 5: "ఉ", 6: "ఊ", 7: "ఋ", 8: "ఋూ", 9: "ఎ", 10: "ఏ",
    11: "ఐ", 12: "ఒ", 13: "ఓ", 14: "ఔ", 15: "అం", 16: "అః", 17: "క", 18: "ఖ", 19: "గ", 20: "ఘ",
    21: "ఙ", 22: "చ", 23: "ఛ", 24: "జ", 25: "ఝ", 26: "ఞ", 27: "ట", 28: "ఠ", 29: "డ", 30: "ఢ",
    31: "ణ", 32: "త", 33: "థ", 34: "ద", 35: "ధ", 36: "న", 37: "ప", 38: "ఫ", 39: "బ", 40: "భ",
    41: "మ", 42: "య", 43: "ర", 44: "ల", 45: "వ", 46: "శ", 47: "ష", 48: "స", 49: "హ", 50: "ళ",
    51: "క్ష", 52: "ఱ"
}
df['class'] = df['class'].map(label_mapping)
label_binarizer = LabelBinarizer()
label_binarizer.fit(df['class'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        image = Image.open(file).convert('L')
        image = image.resize((28, 28))
        image_array = np.array(image).reshape(1, 28, 28, 1) / 255.0
        
        prediction = model.predict(image_array)
        predicted_label_index = np.argmax(prediction, axis=1)[0]
        predicted_vowel = label_binarizer.classes_[predicted_label_index]

        return render_template('index.html', predicted_vowel=predicted_vowel)

if __name__ == '__main__':
    app.run(debug=True)
