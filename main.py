from flask import Flask, request
from services.convert_service import ConvertService
from services.image_service import ImageService
import base64
import json
import os
from zipfile import ZipFile
from glob import glob

app = Flask(__name__)
app.debug = True

if not os.path.isdir('tmp'):
    try:
        os.mkdir('tmp')
    except OSError as error:
        print(error)

@app.route('/convert', methods=["POST"])
def convert():
    # get file in base64
    file_base64 = request.get_json()["file"]

    # write file to pdf file
    with open('tmp/input.pdf', 'wb') as f:
        f.write(base64.b64decode(file_base64))

    # convert pdf to html and images
    ConvertService(f"{os.getcwd()}/tmp/input.pdf", "./tmp/download.zip").run()

    # unzip html source
    with ZipFile("./tmp/download.zip", 'r') as zip_ref:
        zip_ref.extractall("./tmp/download")

    # resize images
    for path in glob(f"{os.getcwd()}/tmp/download/images/*.*"):
        ImageService(path).resize(1200)

    remove_tmp_files()

    return 'done!'

def remove_tmp_files():
    if os.path.isfile('./tmp/download.zip'):
        os.remove('./tmp/download.zip')

    if os.path.isfile('./tmp/input.pdf'):
        os.remove('./tmp/input.pdf')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8080')