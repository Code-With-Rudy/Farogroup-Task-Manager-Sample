from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route for the main dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Optional: Example of a backend API route if you want to expand backend logic later
@app.route('/api/status')
def status():
    return jsonify({"status": "online", "service": "Farogroup Task Manager"})

if __name__ == '__main__':
    app.run(debug=True)
