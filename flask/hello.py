# Heroku endpoint found here https://homedataflask.herokuapp.com/
from flask import Flask, render_template, json, request
# Flask Documentation here http://flask.pocoo.org/docs/1.0/api/#flask.Flask
# Flask quickstart here http://flask.pocoo.org/docs/1.0/quickstart/

# Create an instance of this class (First Parameter)
# If you are using a single module, __name__ is always the correct value.
# If you however are using a package, it’s usually recommended to hardcode the name of your package there.
app = Flask(__name__)
# use the route() decorator to tell Flask what URL should trigger our function

# the main app route, goes to home at the default "/" url endpoint
@app.route('/')
def home():
    # render the template with render_template
    # this hosts the site using the template we saved at index.html
    return render_template('index.html')

# for debug mode
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
