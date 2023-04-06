from os import getenv
from app import app

if __name__ == "__main__":
    app.run(port=int(getenv("PORT", 2034)), host="0.0.0.0")
