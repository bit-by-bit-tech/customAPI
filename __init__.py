import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:#Load the instance config, if it iexists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:#Load test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello, World!'

    from . import qrcode
    app.register_blueprint(qrcode.bp)

    from . import beerPrice
    app.register_blueprint(beerPrice.bp)


    return app
