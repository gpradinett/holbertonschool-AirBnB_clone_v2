#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
* /: display “Hello HBNB!”
- You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

# Creando una instancia de flask con el nombre del archivo nuestro
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Function hello, that return a prompt saying: Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """
    Set host IP addres and port
    Info: https://www.codegrepper.com/code-examples/python/flask+set+listen+
    address+port
    """
    app.run(host="0.0.0.0", port=5000)
