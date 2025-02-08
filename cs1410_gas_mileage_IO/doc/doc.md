----------------------------------

# CS 1410: Gas Mileage I/O

- Copy your completed gas_mileage code from Assignment 3 to the gas_mileage.py file

----------------------------------

## Introduction

In this assignment you will store the gas_mileage data in JSON format in a file called notebook.json.

You can learn about using JSON in Python here:
https://www.w3schools.com/python/python_json.asp 

----------------------------------

## Assignment

Modify/create the following functions

### `createNotebook`

Modify the function `createNotebook` so that it receives one parameter, the name of the file you are storing the data in.  It opens the file, reads the data, closes the file. If the file is empty, it returns an empty list. Otherwise it converts the data from JSON to Python and returns the data. 

if notebook.json is empty:
```language-python
createNotebook("notebook.json) -> []
```
if notebook.json contains: [{'date': '01/01/2017', 'miles': 300.0, 'gallons': 10.0}]
```language-python
createNotebook("notebook.json) -> [{'date': '01/01/2017', 'miles': 300.0, 'gallons': 10.0}]
```
-----------------------------------

### `saveNotebook`

The new function `saveNotebook` takes one parameter, the notebook list. The function opens the file "notebook.json" and writes the notebook out in JSON format. Finally it closes the file. **The function should not modify the notebook.**

-----------------------------------

### `recordTrip`

Modify `recordTrip` so that it saves the notebook to the file by calling saveNotebook. 

-----------------------------------


### `main`

In `main` modify the call to createNotebook to contain the name of the file to read from.

-----------------------------------

### Finishing Up

Lastly add this snippet at the bottom of your file which will execute your `main()` function when you run `gas_mileage.py` but will allow it to be imported into the unittest files without executing the main function.

```language-python
if __name__ == '__main__':
    main()
```
