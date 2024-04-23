from flask import Flask, jsonify
from uszipcode import SearchEngine

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_zip(zip):
    engine = SearchEngine()
    place = engine.by_zipcode(zip)
    location_info = {"zipcode":place.zipcode, "city":place.major_city, "state":place.state_abbr}
    return jsonify(location_info)

if __name__ == "__main__":
    app.run(port=8003)