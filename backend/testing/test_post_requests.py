import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, routes
import unittest
import json
import psycopg2

class PostTest(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        DB_HOST = 'localhost'
        DB_NAME = 'postgres'
        DB_USER = 'postgres'
        DB_PASS = 'admin'

        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()
        cur.execute('DELETE FROM lists WHERE id > 3;')
        cur.execute('DELETE FROM cards WHERE id > 11;')
        conn.commit()
        cur.close()
        conn.close()

    # Valid requests can be made with no end slash in route
    def test_addlist_with_no_end_slash(self):
        tester = app.test_client(self)
        response = tester.post("/addlist", json=dict(name="List Five", author="Jimmy Smith", description="beginner", language="french"))
        status_code = response.status_code
        self.assertEqual(status_code, 201)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"List Five" in response.data, "The list name is not in the response data")
        self.assertTrue(b"Jimmy Smith" in response.data, "The author name is not in the response data")
        self.assertTrue(b"beginner" in response.data, "The description name is not in the response data")
        self.assertTrue(b"french" in response.data, "The language name is not in the response data")

    def test_addlist(self):
        tester = app.test_client(self)
        response = tester.post("/addlist", json=dict(name="List Five", author="Jimmy Smith", description="beginner", language="french"))
        status_code = response.status_code
        self.assertEqual(status_code, 201)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"List Five" in response.data, "The list name is not in the response data")
        self.assertTrue(b"Jimmy Smith" in response.data, "The author name is not in the response data")
        self.assertTrue(b"beginner" in response.data, "The description name is not in the response data")
        self.assertTrue(b"french" in response.data, "The language name is not in the response data")

    def test_addlist_non_existing_language(self):
        tester = app.test_client(self)
        response = tester.post("/addlist/", json=dict(name="List Five", author="Jimmy Smith", description="beginner", language="blarg"))
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Language provided does not exist" in response.data, "Invalid list added")

    def test_addcard(self):
        tester = app.test_client(self)
        response = tester.post("/list/1/addcard/", json=dict(term="gato", author="Jimmy Smith", description="animal independente", language="portuguese"))
        status_code = response.status_code
        self.assertEqual(status_code, 201)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"gato" in response.data, "The term name is not in the response data")
        self.assertTrue(b"Jimmy Smith" in response.data, "The author name is not in the response data")
        self.assertTrue(b"animal independente" in response.data, "The description name is not in the response data")
        self.assertTrue(b"portuguese" in response.data, "The language name is not in the response data")

    # ADDCARD non-existing language
    def test_addcard_non_existing_language(self):
        tester = app.test_client(self)
        response = tester.post("/list/1/addcard/", json=dict(term="nothing", author="Jimmy Smith", description="everything", language="glarb"))
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Language provided does not exist" in response.data, "Invalid card added")

    def test_addcard_non_matching_language(self):
        tester = app.test_client(self)
        response = tester.post("/list/2/addcard/", json=dict(term="nothing", author="Jimmy Smith", description="everything", language="english"))
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Language provided does not match list's language" in response.data, "Invalid card added")

    def test_addcard_non_existing_list(self):
        tester = app.test_client(self)
        response = tester.post("/list/4/addcard/", json=dict(term="gato", author="Jimmy Smith", description="animal independente", language="portuguese"))
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"List doesn't exist" in response.data, "Valid list data returned")

    def test_addcard_non_existing_term_in_language(self):
        tester = app.test_client(self)
        response = tester.post("/list/2/addcard/", json=dict(term="coisa", author="Jimmy Smith", description="everything", language="spanish"))
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Word doesn't exist in: spanish" in response.data, "Invalid card added")


if __name__ == "__main__":
    unittest.main()
