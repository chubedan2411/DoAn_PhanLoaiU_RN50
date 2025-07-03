from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import numpy as np 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
from PIL import Image

# Configuration
UPLOAD_FOLDER = 'static/Uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model
MODEL_PATH = 'model/fine_tuned_resnet50.h5'
model = load_model(MODEL_PATH)

# Classes 
CLASS_NAMES = ['glioma', 'menigioma', 'notumor', 'pituitary']

# Ensure upload and other static folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok = True)

# Helper function to check if a file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    img_path = None
    prediction = None

    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Save the file to the upload folder
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Image Processing
            img = Image.open(filepath).convert('RGB')
            img = img.resize((256, 256))
            x = img_to_array(img)
            x = preprocess_input(x)
            x = np.expand_dims(x, axis=0)

            # Predict
            preds = model.predict(x)[0]
            best_idx = np.argmax(preds)
            prediction = CLASS_NAMES[best_idx]

            # URL to display in template
            img_path = url_for('static', filename=f'Uploads/{filename}')

    return render_template('index.html',
                           img_path=img_path,
                           prediction=prediction)

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)



