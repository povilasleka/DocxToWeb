from flask import Flask, request
from services.convert_service import ConvertService
import base64
import json
import os

app = Flask(__name__)
app.debug = True

@app.route('/convert', methods=["POST"])
def convert():
    file_base64 = request.get_json()["file"]

    with open('input.pdf', 'wb') as f:
        f.write(base64.b64decode(file_base64))

    ConvertService(f"{os.getcwd()}/input.pdf", "download.zip").run()

    return 'done!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8080')