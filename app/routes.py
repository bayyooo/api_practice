from flask import Blueprint, jsonify, request

# Create a Blueprint for routes
main = Blueprint("main", __name__)

@main.route("/") # required:  this defines the route, the / is for home but it can be any other one 
def home():
    data = {  #defining a python dictionary - flask can convert directly to JSON
        "message":"Welcome to the API",
        "status":"success",
        "items": ["item1","item2", "item3"]
    }
    return jsonify(data) #convert python dictionary data to JSON format & sets the appropriate HTTP response headers

@main.route("/greet", methods=["POST"]) #tells Flask that when someone accesses /greet using the POST method, it should run the greet function.
def greet():
    try: 
        data = request.json #Access JSON data sent in request 
        if not data:
            raise ValueError("No JSON provided")
        name = data.get("name", "Guest") #Get 'name' value and default it to 'Guest'
        return jsonify({"message":f"Hello, {name}!"})
    except ValueError as e:  #handle invalid JSON
        return jsonify({"error": str(e)}), 400 #will return error with status code 400
    except Exception as e:
        return jsonify({"error": "idk unexpected error happened" }),500
    
    
@main.route("/items", methods = ["POST"])
def things():
    try:
        data = request.json #Access JSON data sent in request 
        if not data:
            raise ValueError("No JSON provided")
        things = data.get("things", [])
        return jsonify({"items": f"This is the list: {things}"})
    except ValueError as e:  #handle invalid JSON
        return jsonify({"error": str(e)}), 400 #will return error with status code 400
    except Exception as e:
        return jsonify({"error": "idk unexpected error happened" }),500

@main.errorhandler(404)
def not_found(error):
    return jsonify({"error":"resource not found"}), 404