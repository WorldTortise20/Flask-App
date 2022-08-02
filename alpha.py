from asyncio import tasks
from flask import Flask, jsonify
from requests import request

list =[
    {
        "id": 1,
        "Name": u"Jack",
        "Contact": u"7723938567",
        "done": False
    },

    {
        "id": 2,
        "Name": u"Ryan",
        "Contact": u"9871237045",
        "done": False
    }
]

app = Flask(__name__)
@app.route('/')

def start():
    return "Welcome back. You know what to do."

@app.route('/add-data', methods = ["POST"])

def task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)
    
    contact = {
        'id': tasks[-1]['id'] +1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }

    list.append(contact)

    return jsonify({"status": "success", "message": "Contact added, over"})

@app.route("/get-data")

def get_task():
    return jsonify({
        "data": list
    })

if __name__ == "__main__":
    app.run(debug= True)
    