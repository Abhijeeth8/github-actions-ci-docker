from app import app

def test_home():
  response = app.test_client().get('/')

  assert response.status_code==200
  assert response.data==b"Hellow from the docker container. This message is from the tutorial of git hub actions CI to push a docker image to Dockerhub."