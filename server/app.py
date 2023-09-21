#!/usr/bin/env python3
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_mail import Mail 
from bson import json_util


# initialize/connect to  mongodb storage database
DBstorage = __import__("storage").DBStorage
storage = DBstorage()

# initialize mail service from Email module
Email = __import__("mail").Email
mail = Email()

# initialize flask app
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('../web_app/dist/index.html')


@app.route('/api/submit', methods=['POST'])
def submit():
    """
    Inserts a new submission into the database
    """
    name = request.form.get("name", None)
    email = request.form.get("email", None)
    subject = request.form.get("subject", None)
    message = request.form.get("message", None)

    params = {
            "name": name, "email": email,
            "subject": subject, "message": message
        }
    
    try:
        storage.insert_submission(params)
        params.pop("_id")
        mail.send(params)
    except Exception as e:
        return jsonify({"error": str(e)}, 400)
    
    
    return jsonify({"success": True})

@app.route('/api/submissions', methods=['GET'])
def get_submissions():
    """
    Retrieves a list of all stored submissions
    """
    submissions = storage.get_all_submissions()
    
    return json_util.dumps(submissions)

if __name__ == '__main__':
    app.run(debug=True)