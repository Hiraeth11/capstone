import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, Actor, setup_db
from auth import AuthError, requires_auth



def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response


    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):
        '''returns an array of all actors in database'''
        actors = Actor.query.all()

        if len(actors) == 0:
            abort(404)    

        formatted_actors = [actor.format() for actor in actors]

        return jsonify({
            "success": True,
            "actors": formatted_actors
        })


    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(payload):
        '''returns an array of all movies in database'''
        movies = Movie.query.all()

        if len(movies) == 0:
            abort(404)    

        # formatted_movies = [movie.format() for movie in movies]

        return jsonify({
            "success": True,
            "movies": [movie.format() for movie in movies]
        })


    @app.route('/actors/<actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        '''deletes the actor with the corrosponding actor id'''
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            "success": True,
            "actor": actor.format()
        })

    @app.route('/movies/<movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        '''deletes the movie with the corrosponding movie id'''
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({
            "success": True,
            "movie": movie.format()
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actor(payload):
        '''creates a new actors'''
        body = request.get_json()

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)

        actor = Actor(name=new_name,age=new_age, gender=new_gender)
        actor.insert()

        return jsonify({
            'success': True,
            'new_actor': actor.format()
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movie(payload):
        '''creates a new movie'''
        body = request.get_json()
        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        movie = Movie(title=new_title, release_date=new_release_date)
        movie.insert()

        return jsonify({
            'success': True,
            'new_movie': movie.format()
        })

    

    @app.route('/actors/<actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actor(payload, actor_id):
        '''updates an actors details'''
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(404)

        body = request.get_json()

        if "name" in body:
            name = body.get('name', None)
            actor.name = name

        if "age" in body:
            age = body.get('age', None)
            actor.age = age
        
        if "gender" in body:
            gender = body.get('gender', None)
            actor.gender = gender


        return jsonify({
            'success': True,
            'actor': actor.format()
        })

    @app.route('/movies/<movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movie(payload, movie_id):
        '''updates a movies details'''
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404)

        body = request.get_json()

        if "title" in body:
            title = body.get('title', None)
            movie.title = title
        
        if "release_date" in body:
            release_date = body.get('release_date', None)
            release_date.title = title

        return jsonify({
            'success': True,
            'movie': movie.format()
        })


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Resource Not Found"
        }), 404

    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "Unprocessable Entity"
        }), 422

    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': "Method Not Allowed"
        }), 405

    @app.errorhandler(AuthError)
    def authentication_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['code']
            }), 401


    @app.errorhandler(500)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': "Internal Server Error"
        }), 500

    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
