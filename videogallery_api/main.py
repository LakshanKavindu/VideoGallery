from flask import Flask
from flask_restful import Api,Resource,reqparse,abort

app = Flask(__name__)
api = Api(app)
users = {}

videos = [
    {
        'name':'first video',
        'description':'first desc',
        'url':'www.dfdfsd.com'

    },
     {
        'name':'second video',
        'description':'seocn desc',
        'url':'www.dfdfsd12134.com'

    },
     {
        'name':'third video',
        'description':'third desc',
        'url':'www.dfdfsddfjdsk212k1.com'

    },
     {
        'name':'fourth video',
        'description':'fourth desc',
        'url':'www.dfdfsdkjkds23s#2.com'

    },
]



user_put_args = reqparse.RequestParser()
user_put_args.add_argument("name",type=str,help="name of the user",required=True)
user_put_args.add_argument("email",type=str,help="email of the user",required = True)
user_put_args.add_argument("password",type=str,help="password of the user",required=True)



video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str,help="name of the video",required=True)
video_put_args.add_argument("description",type=str,help="desc of the video",required=True)
video_put_args.add_argument("url",type=str,help="url of the video",required=True)

###############################################user abort functions##################################################
def abort_if_user_already_exist(email):
    if email in users:
        abort(409,message="user is already exist")

############################################## video abort funcitons ##############################################

def abort_if_video_already_exist(name):
    for i in videos:
        if name in i.keys():
            abort(409,message = "video is already there")
            

   
        


    


class User(Resource):
    def get(self):
        return {"status":"ok"}
    
    def post(self):
        args = user_put_args.parse_args()
        abort_if_user_already_exist(args['email'])
        users[args['email']]=args['password']
        print(users)

        return users,201

    
class Videos(Resource):
    def get(self):
        return videos


    def post(self):
        
        args = video_put_args.parse_args()
        abort_if_video_already_exist(args['name'])
        new = {}
        new['name'] = args['name']
        new['description'] = args['description']
        new['url'] = args['url']

        videos.append(new)

        print(videos)

        return {"status":"video succesfully added"},200



class Name(Resource):
    def get(self):
        return {"status":"ok"}

    

    



        


api.add_resource(User,"/api/register")
api.add_resource(Videos,'/api/videos')


if __name__ == "__main__":
    app.run(debug=True)