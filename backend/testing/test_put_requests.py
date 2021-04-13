import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, routes
import unittest
import json
import psycopg2

class PutTest(unittest.TestCase):
    LIST_ID = 0

    @classmethod
    def setUpClass(cls):
        DB_HOST = 'localhost'
        DB_NAME = 'postgres'
        DB_USER = 'postgres'
        DB_PASS = 'admin'

        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()
                  
        data = ("New list", "Henry", "my first list", "english")
        cur.execute('INSERT INTO Lists (name, author, description, language) VALUES(%s, %s, %s, %s)', data)
        cur.execute("SELECT id FROM lists WHERE name='New list';")
        cls.LIST_ID = cur.fetchone()[0]
        data = (cls.LIST_ID, "welcome", "Henry", "greeting", "english")
        cur.execute('INSERT INTO Cards (listId, term, author, description, language) VALUES(%s, %s, %s, %s, %s);', data) #INSERT LIST and CARD to test valid ones on
        conn.commit()
        cur.close()
        conn.close()

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
    def test_single_list_with_no_end_slash(self):
        tester = app.test_client(self)
        response = tester.put(f"/list/{self.LIST_ID}", json=dict(name="New list", author="Henry", description="beginner list", language="english"))
        status_code = response.status_code
        self.assertEqual(status_code, 204)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertEqual(b"", response.data)

    # # PUTLIST- DIFFERENT AUTHOR - TODO later after delete functionality
    # def test_putlist_author_return_codes_and_type(self):
    #     tester = app.test_client(self)
    #     response = tester.put("/list/1/", json=dict(name="List Five", author="Jimmy Smith", description="beginner", language="portuguese"))
    #     status_code = response.status_code
    #     self.assertEqual(status_code, 204)
    #     self.assertEqual(response.content_type, "text/html; charset=utf-8")
    #     self.assertEqual(b"", response.data)

    def test_card(self):
        tester = app.test_client(self)
        response = tester.put(f"/list/{self.LIST_ID}/card/1/", json=dict(term="hi", author="Henry", description="greeting", language="english"))
        status_code = response.status_code
        self.assertEqual(status_code, 204)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertEqual(b"", response.data)

    def test_list_non_existing_language(self):
        tester = app.test_client(self)
        response = tester.put(f"/list/{self.LIST_ID}/", json=dict(name="New list", author="Henry", description="beginner list", language="blarg"))
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Language provided does not exist" in response.data, "Invalid list added")

    # N/A- PUTLIST- NOT MATCHING LANGUAGE- TODO after delete functionality

    def test_non_existing_list(self):
        tester = app.test_client(self)
        response = tester.put("/list/5/", json=dict(name="Newer list", author="Henry", description="very basic list", language="english"))
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"List doesn't exist" in response.data, "Valid list data returned")

    def test_card_non_existing_language(self):
        tester = app.test_client(self)
        response = tester.put(f"/list/{self.LIST_ID}/card/1", json=dict(term="hi", author="Henry", description="greeting", language="xckasf"))
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Language provided does not exist" in response.data, "Invalid list added")

    # N/A- PUTCARD- NOT MATCHING LANGUAGE- TODO after delete functionality

    # PUTCARD- DIFFERENT AUTHOR - TODO later after delete functionality. refer to PUTLIST

    def test_non_existing_card_in_non_existing_list(self):
        tester = app.test_client(self)
        response = tester.put("/list/5/card/1/")
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Card doesn't exist" in response.data, "Valid card data returned")

if __name__ == "__main__":
    unittest.main()
