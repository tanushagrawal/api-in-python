import smtplib
from flask import  Flask,jsonify,request,render_template
from flask_restful import Resource,Api
from flask_restful import reqparse
from email.message import EmailMessage


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('gmail',type=str,required = True)
parser.add_argument('message',type=str,required = True)
parser.add_argument('subject',type=str)

class MyApi(Resource):
    def __init__(self):
        self.__gmail = parser.parse_args().get('gmail',None)
        self.__message = parser.parse_args().get('message',None)
        self.__subject = parser.parse_args().get('subject',"Testing")


    def get(self):

        msg = EmailMessage()
        msg['Subject']= self.__subject
        msg['From'] = "agarwalom128@gmail.com"
        msg['To']= self.__gmail
        msg.set_content(self.__message)
        sm = smtplib.SMTP('smtp.gmail.com', 587)
        sm.ehlo()
        sm.starttls()
        sm.login('agarwalom128@gmail.com', '9652534488om')

        sm.send_message(msg)
        sm.close()
        return {"Response":200,"Data":parser.parse_args(),"send":True}



api.add_resource(MyApi,'/mailing/')

@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()



