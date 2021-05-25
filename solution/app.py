
import enum
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
        
        #message select statment 
        messages_res = conn.execute("select body from messages") 
        messages = [m[0] for m in messages_res ] 
        
        statematches = []
        statematches = re.findall('(?<={)[^|]*(?=)',str(messages)) 
       
        #state select statement to find the id to then put into messages 
        output_obj = conn.execute("select * from state") 
        results = output_obj.fetchall()
        test2 =[]
        foundmatchlist = [] 
       # produced the object that holds both id and value of state  
        for row in results: 
            for index, statematch in enumerate(statematches) :
                row_as_dict = {output_obj.description[i][0]:row[i] for i in range(len(row))}  
                if row_as_dict['id'] == statematch: 
                    foundmatchlist.append(row_as_dict)  

        # there is an issue with this part of the replacment that i thought should work. 
        for index, message in enumerate(messages) :  
            for foundmatch in foundmatchlist : 
                messages[index] = messages[index].replace(str(foundmatch['id']),foundmatch['value'])
        
           
            test2 = re.sub('[{}|]','',str(messages)) 

       
        return jsonify(messages), 200   


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# Thought Process 
# i normally write code with camelCasing but i seen the way the code was presented to me and used the methodlogies that were present. 
# so how i went about finding the solution for this was through noticing the messages list and build another a list which made sense 
# to grab the correct id with the correct value which can later be used to replace the strings
# lastly the strings in the message need to be removed {|} and the the values 