from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger

app = Flask(__name__)

# Initialize Swagger
swagger = Swagger(app)

# Set up Swagger UI at a specific URL
SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI
API_URL = '/static/swagger.json'  # API documentation URL

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI URL
    API_URL,      # Documentation URL
    config={      # Swagger UI configuration
        'app_name': "My Flask API"
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Define a sample route
@app.route('/users', methods=['GET'])
def get_users():
    """
    Get list of users
    ---
    responses:
      200:
        description: A list of users
    """
    return jsonify({"users": ["user1", "user2", "user3"]})

if __name__ == '__main__':
    app.run(debug=True)
