from flask import Flask, redirect, url_for, session, request, render_template
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "newsblur"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from newsblur.views import posts
    from newsblur.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

@app.route('/about')
def about():
  return render_template('about.html')


if __name__ == '__main__':
    app.run()
