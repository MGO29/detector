from api.save_image_api import *
from api.check_pattern_api import *
from PIL import Image
from flask import Flask,request,jsonify
# app reference
app = Flask(__name__)

# This method executes before any API request
@app.before_request
def before_request():
    print('before API request')


@app.route("/register", methods=["POST"])
def process_image():
    file = request.files['file']
    # Read the image via file.stream
    img = Image.open(file.stream)
    isSaved = save_pattern_image(img,file.filename)
    return jsonify({'msg': 'success', 'size': [img.width, img.height], 'isSaved':isSaved})



@app.route("/check", methods=["POST"])
def check_image():
    file = request.files['file']
    # Read the image via file.stream
    img = Image.open(file.stream)
    isSaved = check_pattern(img)
    return jsonify({'msg': 'success', 'size': [img.width, img.height], 'isSaved':isSaved})


@app.after_request
def after_request(response):
    return response