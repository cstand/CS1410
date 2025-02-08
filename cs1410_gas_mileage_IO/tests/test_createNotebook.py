"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import gas_mileage
import os
import json


class TestCreateNotebook(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_notebook.json"  # Use a temporary test file

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def write_test_file(self, data):
        with open(self.test_file, "w") as f:
            json.dump(data, f)

    def read_test_file(self):
        with open(self.test_file, "r") as f:
            return json.load(f)

    def test001_createNotebook_with_empty_data(self):
        self.write_test_file([])
        result = gas_mileage.createNotebook(self.test_file)
        file_data = self.read_test_file()
        self.assertEqual(
            result,
            file_data,
            "Function output should match file contents for an empty file",
        )

    def test002_createNotebook_with_valid_data(self):
        data = [
            {"date": "01/01/2017", "miles": 300.0, "gallons": 10.0},
            {"date": "01/02/2017", "miles": 270.0, "gallons": 8.6},
        ]
        self.write_test_file(data)
        result = gas_mileage.createNotebook(self.test_file)
        file_data = self.read_test_file()
        self.assertEqual(
            result,
            file_data,
            "Function output should match file contents for valid data",
        )

    def test003_createNotebook_with_invalid_data(self):
        with open(self.test_file, "w") as f:
            f.write("not a json")

        with self.assertRaises(
            json.JSONDecodeError, msg="Should raise JSONDecodeError for invalid JSON"
        ):
            gas_mileage.createNotebook(self.test_file)

    def test_createNotebook_with_missing_file(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        with self.assertRaises(
            FileNotFoundError, msg="Should raise FileNotFoundError for a missing file"
        ):
            gas_mileage.createNotebook(self.test_file)


if __name__ == "__main__":
    unittest.main()
