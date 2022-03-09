# Instructions
This project was built using Python 3.7.9 and Flask framework.  

## Create an environment and activate it
```
$ python -m venv origin_env
$ cd origin_env\Scripts
$ activate
$ cd ../../
```

## Install requirements dependencies by doing 
```
$ pip install -r requirements.txt
```

## Define a environment variable for flask by doing the code bellow if running on a windows machine 
```
$ set FLASK_APP=src\main\app.py
```

## Define a environment variable for flask by doing the code bellow if running on a linux machine 
```
$ export FLASK_APP=src/main/app.py
```

### After these configurations, run flask by doing
```
$ flask run
```

### By using postman (or any other of preference) make a POST request to the route '/risk-analysis'
```JSON
{
  "age": 35,
  "dependents": 2,
  "house": {"ownership_status": "owned"},
  "income": 0,
  "marital_status": "married",
  "risk_questions": [0, 1, 0],
  "vehicle": {"year": 2018}
}
```

### The response should be as follows 

```JSON
{
    "auto": "regular",
    "disability": "ineligible",
    "home": "economic",
    "life": "regular"
}
```

### In order to run the tests, do :

```JSON
$ python -m unittest src/test/test_user_risk_validator.py
```


# Technical Decisions

Before building the code itself, I designed what I was willing to achieve at each point in time.
I considered separating all the modules in two main folders 
- main 
- test

Main folder would hold all the project itself, with the layers and the main app, whereas the Test folder
would hold test cases. 

I have used Enums in order to make it more clean and ajustable in case of future changes, by avoiding 
repetition and bug fixing due to mismatching. I also build a service layer where the business rules take place 
by calling a validator I have created. 

Each of the business rules conditions I turned into a function, which resembles a little of the strategy pattern.
validate method is where the logic takes place and a new score map is created and returned. 

I also chose to separate risk profile related methods into RiskProfile class, 
this way I would initialize and retrieve the maps intended to be used.  

# Relevant Comments 
I believe the project is well structured, of course there are lots of changes that could be taken like creating 
specialized exception messages, maybe creating separate controllers for each entity routes. But overall, I believe this 
solution solves the problem well. 
Another comment I'd like to do is regarding the tests which I have done some, but could also be improved.