from flask import Flask

# Create a Flask appliction 
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return "Hellow, Flask! welcome to your first web app."

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

#Define route# Route to greet user by name using Jinja2 template
@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

# Route to return a welcome message
@app.route('/welcome')
def welcome():
    return "Welcome to our Flask app!"

# Route to return the square of a number
@app.route('/square/<int:number>')
def square(number):
    return jsonify({"square": number ** 2})

# Route to repeat a word specified times
@app.route('/repeat/<string:word>/<int:times>')
def repeat(word, times):
    return word * times

# Route to display current date and time
@app.route('/info')
def info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date and time: {now}"
return if __name__ == '__main__':
    app.run(debug=True)
    