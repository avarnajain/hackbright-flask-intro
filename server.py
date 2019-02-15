"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
    <body>
    <h1>Hi! This is the home page</h1>
    <a href="http://0.0.0.0:5000/hello">hello</a>
    </body>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="POST">
           What's your name? <input type="text" name="person"><br>
          <input type="radio" name="options" id="smart" value="smart"> Smart </input><br>
          <input type="radio" name="options" id="pretty" value="pretty"> Pretty </input><br>
          <input type="radio" name="options" id="funny" value="funny"> Funny </input><br>
          <input type="submit" value="Submit"><br><br>
        </form>

        <form action="/diss" method="POST">
           What's your name? <input type="text" name="person"><br>
          <input type="radio" name="diss_options" id="messy" value="messy"> Messy </input><br>
          <input type="radio" name="diss_options" id="stupid" value="stupid"> Stupid </input><br>
          <input type="radio" name="diss_options" id="smelly" value="smelly"> Smelly </input><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet", methods=["POST"])
def greet_person():
    """Get user by name."""
    print('>>>in greet method')
    
    player = request.form.get("person")
    compliment = request.form.get('options')
    

    # y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/diss", methods=["POST"])
def diss_person():
    """Get user by name."""
    print('>>>in diss method')

    player = request.form.get("person")
    diss = request.form.get('diss_options')

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
