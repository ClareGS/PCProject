from flask import Flask, render_template, request
import logging

flask_app = Flask(__name__)

#CONFIGURING LOGGING
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler('application_logs.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

#app = Flask("pcprojectApp")

@flask_app.route("/")
def hello_someone():
    return render_template("hello.html")

logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)

#app.run(debug=True)
