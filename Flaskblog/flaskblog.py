from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'edb02fb6bc7e05f3d1caa37874ea10c4'

posts = [
    {
        'author':"Drsims",
        'title': "Blog Post 1",
        'content':"First post content",
        'date_created': "February 27, 2024.",
        'quote': "I LOVE YOU."
    },
    {
        'author':"Simon",
        'title': "Blog Post 2",
        'content':"Second post content",
        'date_created': "March 1, 2024.",
        'quote': "Nigeria will be great again."
    },
    {
        'author':"Timi",
        'title':"Blog Post 3",
        'content':"Third post content",
        'date_created':"March 30, 2024.",
        'quote':"I am a great man of valor"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__== '__main__':
    app.run(debug=True)