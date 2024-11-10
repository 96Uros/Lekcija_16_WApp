from flask import Flask, render_template

# create new Flask object
app = Flask(__name__)


#to je osnovna koda za flask

#to je kontroler handler
#ROOT
@app.route("/")
def index():
    return render_template("index.html")

#
@app.route("/galerie")
def galerie():
    return render_template("galerie.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run(use_reloader=True)
    #reloader je osvezovanje strani



