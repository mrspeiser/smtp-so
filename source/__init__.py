from flask import Flask

def create_app(test_config=True):
  app = Flask(__name__)
  

  print('app has started')

  @app.route('/')
  def root_root():
    return "root\n"

  return app


