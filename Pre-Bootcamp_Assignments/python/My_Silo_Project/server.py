from flask_app import app
from flask_app.controllers import login_controller, routine_controller, workout_controller, measure_controller, explore_controller, more_controller


if __name__ == "__main__":
    app.run(debug=True)