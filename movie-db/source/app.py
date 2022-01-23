from flask import Flask, request, Response
from flask_restx import Resource, Api, fields
from flask import abort, jsonify


app = Flask(__name__)
api = Api(app)

ns_movie = api.namespace('ns_movie', description='Movie APIs')

movie_info = {
    'Evil Dead 2013':'1st movie',
    'Annabelle Creation':'2nd movie',
    'Insidious The Last Key':'3rd movie',
    'The Conjuring 2':'4th movie',
    'Dawn Of Justice':'5th movie',
    'Suicide Squad':'6th movie',
    'John Wick Chapter 1':'7th movie',
    'John Wick Chapter 2':'8th movie',
    'John Wick Chapter 3':'9th movie',
    'Lost In Space S1':'10th movie',
    'Lost In Space S2':'11th movie',
    'Pacific Rim 2013':'12th movie',
    'Pacific Rim Uprising 2017':'13th movie'
}

@ns_movie.route('/movies')
class movies(Resource):
  def get(self):
    return {
        'movie_info': movie_info
    }


@ns_movie.route('/movies/<string:name>')
class movies_name(Resource):
  # 영화 이름 정보 조회
  def get(self, name):
    if not name in movie_info.keys():
      abort(404, description=f"Movie {name} doesn't exist")
    movie_description = movie_info[name]

    return {
        'Movie Name' : name,
        'Movie Description': movie_description
    }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

