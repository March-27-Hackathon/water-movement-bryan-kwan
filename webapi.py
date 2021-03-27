
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

#parse requests
parser = reqparse.RequestParser()
parser.add_argument("msg", type = str, help = '''needs a message''', required=True)


messages = {'1': {'msg': 'hello world'}, 
'2': {'msg': 'spaghettify'},
}


def abort_msg_doesnt_exist(msg_id):
    if msg_id not in messages:
        abort(404, message="Message {} doesn't exist".format(msg_id))


class Message(Resource):

    def get(self, msg_id):
        abort_msg_doesnt_exist(msg_id)
        return messages[msg_id]
    
    def put(self, msg_id):
        args = parser.parse_args()
        message = {'msg': args['msg']}
        messages[msg_id] = message
        return messages[msg_id]

    def delete(self, msg_id):
        abort_msg_doesnt_exist(msg_id)
        del messages[msg_id]
        return ''

#displays all messages
class MessageBoard(Resource):
    def get(self):
        return messages
    def post(self):
        args = parser.parse_args()
        msg_id = int(max(messages.keys()) + 1)
        messages[msg_id] = {'msg': args['msg']}
        return messages[msg_id]



#add to the default directory
api.add_resource(Message, "/messageboard/<string:msg_id>")
api.add_resource(MessageBoard, '/', "/messageboard/", "/messageboard")


if __name__ == "__main__":
    app.run(debug=True, port='4996')
