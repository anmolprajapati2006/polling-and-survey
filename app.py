from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    
    # Convert form data to JSON format
    form_json = json.dumps(form_data, indent=2)

    # Save form data to a file
    with open('form_data.json', 'a') as file:
        file.write(form_json + '\n')

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
