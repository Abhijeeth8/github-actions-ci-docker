from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def Hello():
  return "Hellow from the docker container. This message is from the tutorial of git hub actions CI to push a docker image to Dockerhub."

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=5111)
