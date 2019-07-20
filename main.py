__name__ = "__main__"

from flask import (
    Flask,
    render_template
)

# create app instance
app = Flask(__name__, template_folder="templates")

# create URL route in app for "/"
@app.route('/')
def home():
    """
    responds to URL localhost:5000/
    :return: rendered template 'home.html'
    """
    return render_template('home.html')

# if in standalone mode, run app
if __name__ == "__main__":
    app.run(debug=True)