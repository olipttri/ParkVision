from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import send_from_directory
from werkzeug.utils import secure_filename
import os
from predict import predict_parkinson

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            result = predict_parkinson(filepath)
            print(f"Prediction result: {result}")

            return jsonify({"result": result, "image": filename})
    return render_template('upload.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
