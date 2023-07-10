from flask import Flask, request
import bidding as BiddingScore
from flask import jsonify
from flask_cors import CORS
import numpy as np
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app, resources=r"/bidding")

@app.route('/', methods=['GET'])
def index():
    return "Hello Napier"


@app.route('/bidding', methods=[ 'POST'])
@cross_origin()
def calculateScore():
    if request.method == 'POST':
        data = request.get_json()
        baselineInterval = BiddingScore.calculateBaselineIntervals(data["bidsNum"], data["bidsRangeLow"], data["bidsRangeHigh"])
        confidenceInterval = "(" +str(baselineInterval[0]) +"," + str(baselineInterval[1]) +")"
        bestInterval ="("+str(baselineInterval[0]) +"," + str(np.average(baselineInterval)) +"),并 靠近 "+ str(np.average(baselineInterval))
        response = jsonify({"baselineInterval": baselineInterval, "bestInterval": bestInterval, "confidenceInterval": confidenceInterval,"status": "success"})
        #response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        return response
    else:
        return "Please use POST"

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8888, debug=True)