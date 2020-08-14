
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Movie, Actor, db_drop_and_create_all
from app import create_app


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}/{}".format(
            'postgres:password@localhost:5432', 'capstone_test')

        setup_db(self.app, self.database_path)

        db_drop_and_create_all()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_actor = Actor(
            id = 25,
            name = "test actor",
            age =  32,
            gender = "Male"
        )

        self.new_movie = Movie(
            id = 25,
            title = "test movie",
            release_date = '2020-01-01'
        )

        self.new_actor_json = {
            "name": "test actor post",
            "age": 27,
            "gender": "Female"
        }

        self.new_movie_json = {
            "title": "test movie post",
            "release_date": '2020-02-01'
        }

        first_movie = Movie(
            title = "first movie",
            release_date = '2020-01-01')

        first_actor = Actor(
            name = "first actor",
            age =  32,
            gender = "Male"
        )

        first_movie.insert()
        first_actor.insert()



    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['actors'])

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        print("hello")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))
        self.assertTrue(data['movies'])
        
    #decide on test for this maybe ask in knowledge
    # def test_get_actors_with_invalid_endpoint(self):
    #     res = self.client().get('/movies/2')

    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message', 'Resource Not Found'])

    def test_delete_actor(self):
        self.new_actor.insert()

        res = self.client().delete('/actors/25')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["actor"])

    def test_delete_actor_that_does_not_exist(self):
        res = self.client().delete('/actors/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Resource Not Found")

    def test_delete_movie(self):
        self.new_movie.insert()

        res = self.client().delete('/movies/25')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["movie"])

    def test_delete_movie_that_does_not_exist(self):
        res = self.client().delete('/movies/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Resource Not Found")
    

    def test_post_movie(self):
        res = self.client().post('/movies', json=self.new_movie_json)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["new_movie"])


    def test_405_if_post_movie_not_allowed(self):
        res = self.client().post('/movies/1231', json=self.new_movie_json)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Method Not Allowed")

    def test_post_actor(self):
        res = self.client().post('/actors', json=self.new_actor_json)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["new_actor"])

    def test_405_if_post_actor_not_allowed(self):
        res = self.client().post('/actors/1231', json=self.new_actor_json)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Method Not Allowed")

    def test_patch_movie(self):
        self.new_movie.insert()
        patch_movie = {"title": "updated title"}
        res = self.client().patch('/movies/25', json=patch_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie']['title'], "updated title")

    def test_405_if_patch_movie_not_allowed(self):
        self.new_movie.insert()
        patch_movie = {"title": "updated title"}
        res = self.client().patch('/movies', json=patch_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Method Not Allowed")

    def test_patch_actor(self):
        self.new_actor.insert()
        patch_actor = {"name":"bob"}
        res = self.client().patch('/actors/25', json=patch_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        self.assertEqual(data['actor']['name'], "bob")

    def test_405_if_patch_actor_not_allowed(self):
        self.new_actor.insert()
        patch_actor = {"name":"bob"}
        res = self.client().patch('/actors', json=patch_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Method Not Allowed")
    


if __name__ == "__main__":
    unittest.main()

        
