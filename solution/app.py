from flask import Flask, request, jsonify
import sqlite3
import json
import re # regular expressions
from pprint import pprint


app = Flask(__name__)
DBPATH = "../database.db"

@app.route("/messages", methods=["GET"])
def messages_route():
    """
    Return all the messages
    """

    with sqlite3.connect(DBPATH) as conn:
        messages_res = conn.execute("select body from messages")
        messages = [m[0] for m in messages_res]
        return jsonify(list(messages)), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
