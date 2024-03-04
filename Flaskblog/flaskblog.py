from flask import Flask, render_template
app = Flask(__name__)

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
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home Page', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About page')


if __name__== '__main__':
    app.run(debug=True)