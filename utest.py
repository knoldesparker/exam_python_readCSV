import unittest
from csvreader import showDB, searchCrime, makeHTML,makeJSON
from unittest import mock
import os


class Test(unittest.TestCase):
         

    # Test if project directory is being created
    def test_create_html_doc(self):
        filePath = 'html/fullhtml.html'
        makeHTML() # testing this method
        is_created = False
        if os.path.exists(filePath):
            is_created = True
        self.assertTrue(is_created, "sucsessful, since file is created"),

    def test_create_html_doc_fail(self):
        filePath = 'html/fullhtmlFail.html'
        makeHTML() # testing this method
        is_created = False
        if os.path.exists(filePath):
            is_created = True
        self.assertTrue(is_created, "Fails since filename is wrong"),


    def test_create_json_doc(self):
        filePath = 'json/fulljson.json'
        makeJSON() # testing this method
        is_created = False
        if os.path.exists(filePath):
            is_created = True
        self.assertTrue(is_created, "sucsessful, since file is created")
    
    
    def test_create_json_doc_fail(self):
        filePath = 'json/fulljsonFail.json'
        makeJSON() # testing this method
        is_created = False
        if os.path.exists(filePath):
            is_created = True
        self.assertTrue(is_created,"Fails, since filename is wrong")



    


if __name__ == "__main__":
    unittest.main()