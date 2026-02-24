from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello() -> tuple[str, int]:
    return "Ahoj z Python + Docker appky!", 200


@app.get("/health")
def health() -> tuple[str, int]:
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
