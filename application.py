from flask import Flask, render_template

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html is in a 'templates' folder

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
