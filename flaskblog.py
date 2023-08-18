from flask import Flask, render_template, url_for

app = Flask(__name__)

#dummy data
posts = [
    {
        'author' : 'Eric Hayes',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'August 18, 2023'
    },
    {
        'author' : 'Barbara Hayes',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'August 19, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)