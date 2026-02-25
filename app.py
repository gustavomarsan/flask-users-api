from flask import Flask
from routes.user_routes import users_bp


def create_app():
    app = Flask(__name__)

    # Register routes here
    @app.route("/")
    def home():
        return {"message": "API is running"}, 200

    # 🔥 Register Blueprint
    app.register_blueprint(users_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
