from flask import Flask, render_template, request
from deepface import DeepFace
import cv2
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        file = request.files['image']
        path = os.path.join('static', file.filename)
        file.save(path)

        img = cv2.imread(path)
        analysis = DeepFace.analyze(img, actions=['age', 'gender'])

        age = analysis[0]['age']
        gender = analysis[0]['dominant_gender']

        result = f"Gender: {gender}, Age: {age}"

        return render_template('index.html', result=result, image=path)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)