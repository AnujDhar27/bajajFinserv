from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the BFHL Challenge API!"

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        data = request.json.get('data', [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [item for item in alphabets if item.islower()]
        
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None
        
        response = {
            "is_success": True,
            "user_id": "anuj_dhar_27052003",  
            "email": "dhar.anuj2003@gmail.com",  
            "roll_number": "21BCE1997",  
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)
    
    elif request.method == 'GET':
        response = {
            "operation_code": 1
        }
        return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("0.0.0.0", 3000, app)
