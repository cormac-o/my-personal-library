from flask import Flask, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return make_response("<h1>Welcome to My Personal Media Library!</h1>", 200)

if __name__ == '__main__':
    app.run(debug=True) #Port can be specified here if needed, e.g., app.run(debug=True, port=5000)