# Python For Testing - Log Parsing

This project introduces you to `pytest` - the most popular testing framework for Python - through a few exercises that parse a typical log file to check for errors and look for expected patterns. 

Parsing = “to analyze a sentence into its parts of speech and grammatical structure.”

## Installing Dependencies

To create a virtual environment and install all the dependencies, execute the following:

On Linux/Mac:
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

On Windows:
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Running Tests

To run all the existing tests and see them pass, run the command:

`pytest`

## Exercises

Each of the file under `tests` contain a few exercises that we will work through during the workshop. 

## Scope of Learning

- Previously: tour of python ecosystem tools => you have operational test development environment
- This material illustrates discovery of:
    * configuring pytest test location to folder test/
    * pytest.ini as source of command line arguments
    * parsing logs with python and pytest, and naming the patterns you search
    * html reports from pytest
    * debugging a pytest, why and how
    * difference of non-test/test and script/function
    * for loop, implicitly
    * counting items in a list
    * concept of fixture
    * concept of debugging
    * working in a git branch
- Intentionally later: scopes of fixtures, parametrized tests, libraries beyond the minimal, test targets other than files with text

## Attribution

This exercise originates from a time when Maaret Pyhäjärvi and Ru Cindrea taught python to fellow testers together. It has been set up as a layered learning exercise, showing you can do some with very little learning, and then continue peeling into more layers. 