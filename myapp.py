from flask import Flask

# server_port = 5000
app = Flask(__name__)


@app.route('/')
def test_locust():
    return 'Locust run!'


if __name__ == '__main__':
    app.run()
