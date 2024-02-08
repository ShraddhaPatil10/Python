from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and a function to handle requests to that route
@app.route('/')
def home():
    return 'Hello, Flask!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
