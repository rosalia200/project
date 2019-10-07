from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from configs.config import Development,Production

app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/Registration/',methods=['POST','GET'])
def registration():
    if request.method == 'POST':
        first_name = request.form['fname']
        print(first_name)

    #
    return render_template('registration.html')



if __name__ == '__main__':
    app.run()
