from flask import Flask, request, redirect, abort, jsonify
# i changed my index.hmtl during testing & had to use install & use CORS to resolve
# see https://stackoverflow.com/a/27280939
from flask_cors import CORS
from flask.helpers import url_for
from ToysDAO import toysDAO

# PROJECT SERVER
# in the venv enviiornment (which you have already activated) run the server: 
# note to run server in terminal python server.py
# or 1. in terminal export FLASK_APP=server
#  2. flask run
# see week8 for further @app.route 

# setting static url path = route, and static folder = this folder
# app = Flask(__name__, static_url_path='', static_folder='.')

app = Flask(__name__, static_url_path='', static_folder='staticpages')
# see from flask_cors import for explanation.
CORS(app)

@app.route('/')
def index():
    return "Hello fiona world"

# // get all 
# CURL -X GET http://127.0.0.1:5000/toys
@app.route('/toys')
def getAll():

    return jsonify(toysDAO.getAll())

# // get all 
# CURL -X GET http://127.0.0.1:5000/toys
@app.route('/toynames')
def getAllToyNames():

    return jsonify(toysDAO.getAllToyNames())





# // get all 
# CURL -X GET http://127.0.0.1:5000/dispatches

@app.route('/dispatches')
def getAllDispatches():

    return jsonify(toysDAO.getAllDispatches())

# test getToybyId using curl:
# URL -X GET http://127.0.0.1:5000/toys/5
#  find by id / Get by id
@app.route('/toys/<int:id>')
def findByID(id):

    return jsonify(toysDAO.findByID(id))



# test getToybyId using curl:
# URL -X GET http://127.0.0.1:5000/dispatches/1
#  find by id / Get by id
@app.route('/dispatches/<int:dispatch_id>')
def findDispatchByID(dispatch_id):

    return jsonify(toysDAO.findDispatchByID(dispatch_id))

# testing post a toy using curl
# CURL -X POST -H "content-type:application/json" -d "{\"name\": \"Dolls House 3 Story\", \"maker\": \"Stettheimer\", \"model\": \"KML9999\", \"colour\": \"rosewood\", \"quantity\": 13500}" http://127.0.0.1:5000/toys
# end testing post a toy using curl
# Post a toy
@app.route('/toys', methods=['POST'])
def create():
    if not request.json:
        abort(404)
       
    toy = { "name": request.json["name"], 
            "maker": request.json["maker"], 
            "model": request.json["model"],
            "colour": request.json["colour"],
            "quantity": request.json["quantity"]
            }
    return  jsonify(toysDAO.create(toy))

# CURL -X POST -H "content-type:application/json" -d "{\"name\": \"Harry Walsh\", \"address\": \"Cork\", \"product_id\": \"1\"}" http://127.0.0.1:5000/toys
@app.route('/dispatches', methods=['POST'])
def createDispatches():
    if not request.json:
        abort(404)
       
    dispatches = { "name": request.json["name"], 
            "address": request.json["address"], 
            "toyname": request.json["toyname"]
            }
    print(dispatches);
    return  jsonify(toysDAO.createDispatches(dispatches))

# Put / Update  a  toy by  id.
# this will update in the array.
# use curl to test
# CURL -X PUT -d "{\"model\": \"KLM2160\", \"quantity\": 998}" -H "Content-type:application/json" http://127.0.0.1:5000/toys/1
@app.route('/toys/<int:id>', methods=['PUT'])
def update(id):
    foundtoy = toysDAO.findByID(id)
    
    if foundtoy == {}:
        return jsonify({}), 404
    currenttoy = foundtoy
    if 'name' in request.json:
        currenttoy['name'] = request.json['name']
    if 'maker' in request.json:
        currenttoy['maker'] = request.json['maker']
    if 'model' in request.json:
        currenttoy['model'] = request.json['model']
    if 'color' in request.json:
        currenttoy['colour'] = request.json['colour']
    if 'quantity' in request.json:
        currenttoy['quantity'] = request.json['quantity']
    
    values =(foundtoy['maker'], foundtoy['model'], foundtoy['colour'],foundtoy['quantity'], foundtoy['id'])
    toysDAO.update(values)

    return  jsonify(currenttoy)
# CURL -X PUT -d "{ \"id\":1, \"quantity\": 998}" -H "Content-type:application/json" http://127.0.0.1:5000/stock/1
@app.route('/stock/<int:dispatch_id>', methods=['PUT'])

def updateStock(dispatch_id):
   
    toysDAO.updateStock(dispatch_id)

    return  jsonify({"done":True})

# Delete a toy by id
# CURL -X DELETE http://127.0.0.1:5000/toys/1
@app.route('/toys/<int:id>', methods=['DELETE'])
def deleteToy(id):
    foundtoy = toysDAO.findByID(id)
    if foundtoy == {}:
        return "Sorry that Toy was not found"
        404
    toysDAO.delete(id) 
    return  jsonify({"done":True})




if __name__ == "__main__":
    print("in if")
    # // run flask with debug on.
    app.run(debug=True)
