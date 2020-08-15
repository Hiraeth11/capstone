
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

        casting_assistant_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh3VXZlWTVFTl9ndExXNzV5dXNfeCJ9.eyJpc3MiOiJodHRwczovL2Rldi15OTZ5NWc3ci5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmI4NjcxNzA0YWYwMDZkZGZkZDU5IiwiYXVkIjoibW92aWUiLCJpYXQiOjE1OTc0Mjk4NjcsImV4cCI6MTU5NzUxNjI2NywiYXpwIjoidlZ5Szk3M3pudHIybU5jU2drb1VjcWN4YXl1ZUZpR1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.ocbjr4CYpyhwGDhGI6GF3fl8C1ZAUK2gB3YjqD9Dqdxmedl9Cl-3SMPoSmt0qOu6O9OIOteSC0L1sjbWigq62pP_s902g5LPyT_3vp0knLg2ZdwKEfpCqljX5hDWmbB0wh6F10xarFxoagM06BXqLATq4HwcTgeG1P5PVc9uMMluy-U7PIP2a1YlzUuAY1mY-T85aFFnG_PMLAfP3Z1rmrwUF39FmeGaSvUo0b8zxTprng2qQ2WG56JkcyebNWtCKkT1jNNl81onyqD9wzXm1aW5hrLps8RDyTlRCZUGNPFIMAKw8miyhn5nlvMeYs3V9oDY301AYRTdJPToPZ5_5A"
        casting_director_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh3VXZlWTVFTl9ndExXNzV5dXNfeCJ9.eyJpc3MiOiJodHRwczovL2Rldi15OTZ5NWc3ci5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmI4ODcyOTkzM2MwMDY3M2JkMTIwIiwiYXVkIjoibW92aWUiLCJpYXQiOjE1OTc0Mjk4MjcsImV4cCI6MTU5NzUxNjIyNywiYXpwIjoidlZ5Szk3M3pudHIybU5jU2drb1VjcWN4YXl1ZUZpR1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.FGvcemKG66Af6F52FuwTrHtVx_MjcNTh4SiLkvQc4X8QOnLgX_SLUn05q9ceq-Vim9faLlWc5_DXJu-l34q9M1fAH8SEngq6UgfrN37lRAhPEvwK2RKpMYWppAHrr6SAc5UOpdFItQutckIuZw3TCxqebY3OG8vw8F6YSgXoivDTuQoWlgxpiylmUhjYz5z1U91Qtx-stzIEocOUAAywdtYix3kd3KD0vSlKpcqjt2YEG1idexFL61J_uJj9POdyCC5oacBNFOCp_hYOkYDbth8I--ud_33sp2NpaARdA3Gm1LDMK0SROb8cmT26qEKbMBYk24TC-wkNRfMRycLQkA"
        executive_producer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh3VXZlWTVFTl9ndExXNzV5dXNfeCJ9.eyJpc3MiOiJodHRwczovL2Rldi15OTZ5NWc3ci5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmI4YTk0ZWU1MDMwMDZkNjc3NWJlIiwiYXVkIjoibW92aWUiLCJpYXQiOjE1OTc0Mjk2OTgsImV4cCI6MTU5NzUxNjA5OCwiYXpwIjoidlZ5Szk3M3pudHIybU5jU2drb1VjcWN4YXl1ZUZpR1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.GRIeB6ynNSHqw-OKjpwnq9bDucXmGd8XQbcQ9gpq8GoC9WFDyYn07wqX6RVLoe4-SldQvpD3GoAni2aJRWf84dNU9WgmCGKIqieneitM31SjVWY9Oe0ocge10TrpkQ5im7oT14KWVskT_CUaMqVmttK7Cd4tl14UrvJvC-iVnRZ_ktZUa_I2hpCcQsuYaVj4lSLUjbi0I57xxgdJSrq9tD-zrmj9kmQZ4H18vZnYfHwOAXPnYh2OqwZDPx1tN7ip9drz_Nvibl-HV4ckvWVneuF71JSv7RXj-ObZGFheSKO8gR7YzyCkKLODW_pqHNWRqxyXfL0rfvrfPnKtnGZxEA"


        self.casting_assistant_header = {
            "Authorization": "Bearer " + casting_assistant_token
            # "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh3VXZlWTVFTl9ndExXNzV5dXNfeCJ9.eyJpc3MiOiJodHRwczovL2Rldi15OTZ5NWc3ci5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmI4NjcxNzA0YWYwMDZkZGZkZDU5IiwiYXVkIjoibW92aWUiLCJpYXQiOjE1OTc0Mjk4NjcsImV4cCI6MTU5NzUxNjI2NywiYXpwIjoidlZ5Szk3M3pudHIybU5jU2drb1VjcWN4YXl1ZUZpR1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.ocbjr4CYpyhwGDhGI6GF3fl8C1ZAUK2gB3YjqD9Dqdxmedl9Cl-3SMPoSmt0qOu6O9OIOteSC0L1sjbWigq62pP_s902g5LPyT_3vp0knLg2ZdwKEfpCqljX5hDWmbB0wh6F10xarFxoagM06BXqLATq4HwcTgeG1P5PVc9uMMluy-U7PIP2a1YlzUuAY1mY-T85aFFnG_PMLAfP3Z1rmrwUF39FmeGaSvUo0b8zxTprng2qQ2WG56JkcyebNWtCKkT1jNNl81onyqD9wzXm1aW5hrLps8RDyTlRCZUGNPFIMAKw8miyhn5nlvMeYs3V9oDY301AYRTdJPToPZ5_5A"

        }
        

        self.casting_director_header = {
            "Authorization": "Bearer " + casting_director_token
        }

        self.executive_producer_header = {
            "Authorization": "Bearer " + executive_producer_token
            # "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh3VXZlWTVFTl9ndExXNzV5dXNfeCJ9.eyJpc3MiOiJodHRwczovL2Rldi15OTZ5NWc3ci5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmI4YTk0ZWU1MDMwMDZkNjc3NWJlIiwiYXVkIjoibW92aWUiLCJpYXQiOjE1OTc0Mjk2OTgsImV4cCI6MTU5NzUxNjA5OCwiYXpwIjoidlZ5Szk3M3pudHIybU5jU2drb1VjcWN4YXl1ZUZpR1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.GRIeB6ynNSHqw-OKjpwnq9bDucXmGd8XQbcQ9gpq8GoC9WFDyYn07wqX6RVLoe4-SldQvpD3GoAni2aJRWf84dNU9WgmCGKIqieneitM31SjVWY9Oe0ocge10TrpkQ5im7oT14KWVskT_CUaMqVmttK7Cd4tl14UrvJvC-iVnRZ_ktZUa_I2hpCcQsuYaVj4lSLUjbi0I57xxgdJSrq9tD-zrmj9kmQZ4H18vZnYfHwOAXPnYh2OqwZDPx1tN7ip9drz_Nvibl-HV4ckvWVneuF71JSv7RXj-ObZGFheSKO8gR7YzyCkKLODW_pqHNWRqxyXfL0rfvrfPnKtnGZxEA"


        }

    def tearDown(self):
        """Executed after reach test"""
        pass


    # GET endpoint tests

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['actors'])

    def test_get_actors_with_invalid_endpoint(self):
        res = self.client().get('/actors/2', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))
        self.assertTrue(data['movies'])
        
    def test_get_movies_with_invalid_endpoint(self):
        res = self.client().get('/movies/2', headers=self.executive_producer_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')


    # DELETE endpoint tests

    def test_delete_actor(self):
        self.new_actor.insert()

        res = self.client().delete('/actors/25', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["actor"])

    def test_delete_actor_that_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Resource Not Found")

    def test_delete_movie(self):
        self.new_movie.insert()

        res = self.client().delete('/movies/25', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["movie"])

    def test_delete_movie_that_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Resource Not Found")

    # POST endpoint tests

    def test_post_movie(self):
        res = self.client().post('/movies', json=self.new_movie_json, headers=self.executive_producer_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["new_movie"])


    def test_405_if_post_movie_not_allowed(self):
        res = self.client().post('/movies/1231', json=self.new_movie_json, headers=self.executive_producer_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Method Not Allowed")


    def test_post_actor(self):
        res = self.client().post('/actors', json=self.new_actor_json, headers=self.executive_producer_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["new_actor"])

    def test_405_if_post_actor_not_allowed(self):
        res = self.client().post('/actors/1231', json=self.new_actor_json, headers=self.executive_producer_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Method Not Allowed")

    # PATCH endpoint tests

    def test_patch_movie(self):
        self.new_movie.insert()
        patch_movie = {"title": "updated title"}
        res = self.client().patch('/movies/25', json=patch_movie, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie']['title'], "updated title")

    def test_405_if_patch_movie_not_allowed(self):
        self.new_movie.insert()
        patch_movie = {"title": "updated title"}
        res = self.client().patch('/movies', json=patch_movie, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Method Not Allowed")

    def test_patch_actor(self):
        self.new_actor.insert()
        patch_actor = {"name":"bob"}
        res = self.client().patch('/actors/25', json=patch_actor, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        self.assertEqual(data['actor']['name'], "bob")

    def test_405_if_patch_actor_without_id_not_allowed(self):
        self.new_actor.insert()
        patch_actor = {"name":"bob"}
        res = self.client().patch('/actors', json=patch_actor, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data["message"], "Method Not Allowed")
    

if __name__ == "__main__":
    unittest.main()
