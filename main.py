from flask import Flask
from services.convert_service import ConvertService

app = Flask(__name__)

@app.route('/convert', methods=["GET"])
def convert():
    args = request.args
    ConvertService(args.get("input_path"), args.get("output_path")).run()
    return 'done!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8080')