from flask import Flask, request, Response, render_template
from flask_restx import Resource, Api, fields
from flask import abort, jsonify


app = Flask(__name__)
api = Api(app)

ns_movie = api.namespace('ns_movie', description='Movie APIs')

movie_data = api.model(
    'Movie Data',
    {
      "name": fields.String(description="movie name", required=True),
      "description": fields.String(description="movie description", required=True),
    }
)

movie_info = {
    'Evil_Dead_2013':'1st movie',
    'Annabelle_Creation':'2nd movie',
    'Insidious_The_Last_Key':'3rd movie',
    'The_Conjuring_2':'4th movie',
    'Dawn_Of_Justice':'5th movie',
    'Suicide_Squad':'6th movie',
    'John_Wick_Chapter_1':'7th movie',
    'John_Wick_Chapter_2':'8th movie',
    'John_Wick_Chapter_3':'9th movie',
    'Lost_In_Space_S1':'10th movie',
    'Lost_In_Space_S2':'11th movie',
    'Pacific_Rim_2013':'12th movie',
    'Pacific_Rim_Uprising_2017':'13th movie'
}



@app.route("/movies")
def get():
  name = request.args.get('name')
  data = movie_info[name]
  return render_template('form.html',movie_name=name,data=data)




@ns_movie.route("/movies")
class movies(Resource):
  def get(self):
    return {
      'movie_info': movie_info
    }


@ns_movie.route('/movies/<string:name>')
class movies_name(Resource):
  # 브랜드 정보 조회
  def get(self, name):
    if not name in movie_info.keys():
     abort(404, description=f"name {name} doesn't exist")
    data = movie_info[name]

    return {
      'Description' : data
    }

  # 새로운 브랜드 생성
  def post(self, name):
    if name in movie_info.keys():
      abort(409, description=f"name {name} already exists")

    movie_info[name] = dict()
    return Response(status=201)


  # 브랜드 정보 삭제
  def delete(self, name):
    if not name in movie_info.keys():
      abort(404, description=f"name {name} doesn't exists")
      
    del movie_info[name]
    return Response(status=200)


  # 브랜드 이름 변경
  def put(self, name):
    # todo
    return Response(status=200)


@ns_movie.route('/movies/<string:name>/<string:des>')
class movies_name_des(Resource):
  def get(self, name, des):
    if not name in movie_info.keys():
      abort(404, description=f"name {name} doesn't exists")
    if not des in movie_info[name].keys():
      abort(404, description=f"Movie id {name}/{des} doesn't exists")

    return {
        'des': des,
        'data': movie_info[name]
    }

#  @api.expect(movie_data) # body
  def post(self, name, des):
#    if not name in movie_info.keys():
#      abort(404, description=f"name {name} doesn't exists")
#    if des in movie_info[name].keys():
#      abort(409, description=f"Movie ID {name}/{des} already exists")
    
#    movie_info[name] = des

#    body = request.json
#    name = body['name']
    movie_info[name] = des

    return Response(status=200)
  

  def delete(self, name, des):
    if not name in movie_info.keys():
      abort(404, description=f"name {name} doesn't exists")
    if not des in movie_info[name].keys():
      abort(404, description=f"Movie ID {name}/{des} doesn't exists")

    del movie_info[name]

    return Response(status=200)


#  @api.expect(movie_data)
  def put(self, name, des):
    global movie_info

#    if not name in movie_info.keys():
#      abort(404, description=f"name {name} doesn't exists")
#    if not des in movie_info[name].keys():
#      abort(404, description=f"Movie ID {name}/{des} doesn't exists")
    
    
    return Response(status=200)

      


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
