from flask import Flask, request
import requests

app = Flask(__name__)

INFERENCE_URL = "http://inference_service:5000/generate-text"

@app.route('/', methods=['GET', 'POST'])
def index():
    prompt = "hh"
    prediction = "No"
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            try:
                # Create the JSON payload
                payload = {
                    "input_text": prompt,
                    "max_length": 50,
                }
                # Send the POST request with JSON data
                response = requests.post(INFERENCE_URL, json=payload)
                response.raise_for_status()  # Raise an error for bad responses
                
                # Check if the response is JSON
                if response.ok: 
                    {"generated_text" : "value"}
                    
                    

                    prediction = response.json()['generated_text']
                else:
                    prediction = "Error: Unexpected response"

            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
                if 'response' in locals():
                    print("Response content:", response.content)
                prediction = e

    return f'''
       <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Generation</title>
    <style>
        body{{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #0d0d17;
            overflow: hidden;
        }}
        h1 {{
            color: #42b89e;
        }}
        form {{
            background-color: #fff;
            overflow: hidden;
            padding: 20px;
            border-radius: 5px;
            padding : 10px 15px;
            display : flex;
            flex-direction : column;
            width: 50%;
            gap : 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }}
        textarea {{
            width: 100%;
            border: 1px solid #ccc;
            border-radius: 4px;
            resize: none; /* Disable resizing */
        }}
        input[type="submit"] {{
            background-color: #28a745;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            width: 58%;
            cursor: pointer;
        }}
        input[type="submit"]:hover {{
            background-color: #218838;
        }}
        input[type="reset"] {{
            background-color: #616863;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 40%;
        }}
        input[type="reset"]:hover {{
            background-color: #a1b8a6;
        }}
        
        p {{
            background-color: #fff;
            padding: 10px;
            width:50%;
            border-radius: 4px;
            border: 1px solid #ccc;
            margin: 0;
        }}
        .container_input {{
            height: 100%;
            display: flex;
            width: 100%;
            gap : 10px;
        }}
        .container_output{{
            height: 50%;
            display: flex;
            flex-direction: column;
            width: 100%;
            padding: 0px 15px;
            gap: 2px;
        }}
        .container{{
            display: flex;
            width: 100%;
            gap : 10px;
        }}
        h4{{
            color: white;
        }}
        .output{{
            width: 100%;
            padding: 10px 10px;
        }}
    </style>
</head>
<body>
    <h1>Text Generation</h1>
    <div class="container">
        <form method="post" class ="container_input">
            <textarea name="prompt" rows="4" cols="50">{prompt}</textarea>
            <br>
            <div>
                <input type="reset" value="Clear">
                <input type="submit" value="Generate">
            </div>
        </form>
        <div class="container_output">
            <h4>Output</h4>
            <p class="output">{prediction}</p>
        </div>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
