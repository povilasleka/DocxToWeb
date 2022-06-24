from flask import Flask
from services.convert_service import ConvertService

app = Flask(__name__)

@app.route('/convert')
def hello():
    return ConvertService("input_path", "output_path").run()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8080')
