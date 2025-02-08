import unittest
from unittest.mock import patch, mock_open
import json
from gas_mileage import saveNotebook


class TestSaveNotebook(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test001_save_notebook(self, mock_file):
        # Define the notebook data to save
        notebook = [
            {"date": "2025-01-25", "miles": 120, "gallons": 8},
            {"date": "2025-01-26", "miles": 130, "gallons": 9},
        ]

        # Call the function to test
        saveNotebook(notebook)

        # Check that open was called with the correct file and mode
        mock_file.assert_called_with("notebook.json", "w")

        # Check that json.dumps was used to write the correct content
        mock_file().write.assert_called_once_with(json.dumps(notebook, indent=4))

    @patch("builtins.open", new_callable=mock_open)
    def test002_save_notebook_empty(self, mock_file):
        # Define an empty notebook
        notebook = []

        # Call the function to test
        saveNotebook(notebook)

        # Check that the file was written with the correct content
        mock_file().write.assert_called_once_with(json.dumps(notebook, indent=4))


if __name__ == "__main__":
    unittest.main()
