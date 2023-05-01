from flask import Flask, jsonify

app = Flask(__name__)

trains = {
    "Express-365": {
        "category": "Express",
        "number": 365,
        "timetable": [
            {
                "StationA": {
                    "arrival": "10:00",
                    "departure": "10:05"
                }
            }
        ],
        "delay": 0,
        "lastSeen": "StationA"
    }
}

@app.route('/trains')
def get_trains():
    return jsonify(trains)

if __name__ == '__main__':
    app.run(host='192.168.1.1', port=5000)
