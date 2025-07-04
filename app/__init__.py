from flask import Flask
from app.extensions import mongo
from app.webhooks.routes import webhook_bp


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://bussinessa144:webhookthepassword00@web.8nbzp3t.mongodb.net/?retryWrites=true&w=majority&appName=web"
    mongo.init_app(app)
    app.register_blueprint(webhook_bp)
    return app
