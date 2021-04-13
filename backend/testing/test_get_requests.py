import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, routes
import unittest

class GetTest(unittest.TestCase):

    # Valid requests can be made with no end slash in route
    def test_all_list_with_no_end_slash(self):
        tester = app.test_client(self)
        response = tester.get("/lists")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"List One" and b"List Two" and b"Test list" in response.data, "One or more of the list names is not in the response data")
        self.assertTrue(b"Jane Doe" and b"John Smith" and b"Damon" in response.data, "One or more of the author names is not in the response data")
        self.assertTrue(b"My first list" and b"vocabulario para espanol" and b"English vocabulary" in response.data, "One or more of the description names is not in the response data")
        self.assertTrue(b"portuguese" and b"spanish" and b"english" in response.data, "One or more of the language names is not in the response data")

    def test_all_list(self):
        tester = app.test_client(self)
        response = tester.get("/lists/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"List One" and b"List Two" and b"Test list" in response.data, "One or more of the list names is not in the response data")
        self.assertTrue(b"Jane Doe" and b"John Smith" and b"Damon" in response.data, "One or more of the author names is not in the response data")
        self.assertTrue(b"My first list" and b"vocabulario para espanol" and b"English vocabulary" in response.data, "One or more of the description names is not in the response data")
        self.assertTrue(b"portuguese" and b"spanish" and b"english" in response.data, "One or more of the language names is not in the response data")

    def test_single_list(self):
        tester = app.test_client(self)
        response = tester.get("/list/1/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"List One" in response.data, "The list name is not in the response data")
        self.assertTrue(b"Jane Doe" in response.data, "The author name is not in the response data")
        self.assertTrue(b"My first list" in response.data, "The description name is not in the response data")
        self.assertTrue(b"portuguese" in response.data, "The language name is not in the response data")

    def test_non_existing_single_list(self):
        tester = app.test_client(self)
        response = tester.get("/list/4/")
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"List doesn't exist" in response.data, "Valid list data returned")

    def test_all_cards_in_single_list(self):
        tester = app.test_client(self)
        response = tester.get("/cards/list/1/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"List One" in response.data, "The list name is not in the response data")
        self.assertTrue(b"Jane Doe" in response.data, "The author name is not in the response data")
        self.assertTrue(b"My first list" in response.data, "The description name is not in the response data")
        self.assertTrue(b"portuguese" in response.data, "The language name is not in the response data")
        self.assertTrue(b"coisa" and b"cachorro" and b"entenderas" in response.data, "One or more of the terms is not in the response data")
        self.assertTrue(b"algo que existe" and b"animal mais fofinho do mundo" and b"saber" and b"saber algo" in response.data, "One or more of the terms is not in the response data")

    def test_single_card_in_single_list(self):
        tester = app.test_client(self)
        response = tester.get("/list/1/card/3/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"Jane Doe" in response.data, "The author name is not in the response data")
        self.assertTrue(b"portuguese" in response.data, "The language name is not in the response data")
        self.assertTrue(b"entenderas" in response.data, "The term is not in the response data")
        self.assertTrue(b"saber" in response.data, "The description is not in the response data")
        self.assertTrue(b"11" in response.data, "The card id (from the backend) is not in the response data")
        self.assertTrue(b"1" in response.data, "The list id is not in the response data")

    def test_non_existing_single_card_in_single_list(self):
        tester = app.test_client(self)
        response = tester.get("/list/2/card/3/")
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Card doesn't exist" in response.data, "Valid card data returned")

    def test_non_existing_single_card_in_non_existing_single_list(self):
        tester = app.test_client(self)
        response = tester.get("/list/4/card/1")
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Card doesn't exist" in response.data, "Valid card data returned")

    def test_languages(self):
        tester = app.test_client(self)
        response = tester.get("/languages/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"portuguese" and b"spanish" and b"english" in response.data, "One or more of the language names is not in the response data")
        self.assertTrue(b"pt" and b"es" and b"en" in response.data, "One or more of the language codes is not in the response data")

    def test_audio(self):
        tester = app.test_client(self)
        response = tester.get("/audio/coisa/portuguese/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b"https://apifree.forvo.com/audio/" in response.data, "Audio path is not in the response data")

    def test_invalid_audio(self):
        tester = app.test_client(self)
        response = tester.get("/audio/either/portuguese/")
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertTrue(b"Word doesn't exist in: portuguese" in response.data, "Word that doesn't exist in language is part of the response data")

if __name__ == "__main__":
    unittest.main()
