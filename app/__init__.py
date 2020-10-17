from flask import Flask

def create_app(config_name):
    app=Flask(__name__)
    if config_name=='default':
        app.config.from_pyfile('../config.py')
    else:
        app.config.from_pyfile(config_name)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app