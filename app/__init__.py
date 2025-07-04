from flask import Flask
from app.extensions import mongo
from app.webhooks.routes import webhook_bp
import os


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    mongo.init_app(app)
    app.register_blueprint(webhook_bp)
    return app
