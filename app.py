from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Home route for CI/CD demo."""
    return (
        "<h1>Hello from Flask CI/CD Demo v1!</h1>"
        "<p>Automatic Build → Test → Deploy via GitHub Actions.</p>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
