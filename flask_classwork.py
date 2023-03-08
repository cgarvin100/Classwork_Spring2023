from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_status():
    return "I knew da perc wuz fake, but I still ate it cuz im a gremlin"

if __name__ == '__main__':
    app.run()
