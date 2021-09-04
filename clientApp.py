from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin
from wsgiref import simple_server
import textToSPeech

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json['data']
    result = textToSPeech.text2Speech(data)from wsgiref import simple_server
    return {"data" : result.decode("utf-8")}


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host,port=port, app=app)
    httpd.serve_forever()

#My name is John Paul Jones. I live in New York, United States. I love to play baseball.
