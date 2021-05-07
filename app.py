from flask import Flask, request, jsonify

from CustomApp import CustomApp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def mainEntry():
    
    # POST -- data must be in json format
    if request.method == 'POST':
        data = request.get_json()
        
        postObj = CustomApp()
        rtnMsg = postObj.handlePost(data)
        
        return rtnMsg
        
    # GET
    elif request.method == 'GET':
        
        getObj = CustomApp()
        rtnMsg = getObj.handleGet()

        return rtnMsg
        
    # PUT
    elif request.method == 'PUT':
        # future place holder
        return "No Handler In Place For PUT"
        
    # DELETE
    else:
        return "No Handler In Place For DELETE"
    
