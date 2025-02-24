import os

from flask import Flask

def create_app(test_config=None):
    #create and configure the application
        # __name__ is the name of the current module
        # instance_relative_config=True tells the application that configuration files are relative to the instance folder
        # The instance folder is located outside of the flaskr package and can hold data that should not be committed to version control
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import students
    app.register_blueprint(students.bp)

    return app