from flask import Flask, request
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = r'C:\Users\best\Desktop\Projectfinallll\React\traveler\databasephoto'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image part in the request', 400

    image = request.files['image']
    if image.filename == '':
        return 'No selected image', 400

    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    return 'Image uploaded successfully', 200



if __name__ == '__main__':
    app.run(debug=True)
