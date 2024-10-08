# Lecture # 3 - Object Oriented Programming in Python

## Lecture Topics

- Classes
- Instances
- Initializing with attributes using `__init__`
- Instance methods
- Self
- Object properties
- Using the `@property` decorator
- Attribute functions: `get_attr()`, `set_attr()`, `has_attr()`, `del_attr()`
- Modifying the `__repr__` instance method for a class

## Introduction

In today's lecture, we will discuss topics of Object Oriented Programming in Python such as classes, instances, `__init__`, attributes, instance methods, `self`, and object properties.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install `pytest` and any other required packages.
2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

## Deliverables

Write your code in `lib/car.py` (the `car.py` file in the `lib` directory / folder)

1. Create a `Car` class that takes in values for the following parameters for the `__init__` method: `make`, `model`, `year`. The `__init__` method should also take an optional value for the `horn_volume` parameter (set the default value for `horn_volume` to `1`). Write the code to create the appropriate instance variables and assign the values from the input parameters to the appropriate instance variables.
   - The `Car` class should have the following instance variables and values:
     - An instance variable named `make` that has the value of the `make` parameter from the `__init__` method.
     - An instance variable named `model` that has the value of the `model` parameter from the `__init__` method.
     - An instance variable named `year` that has the value of the `year` parameter from the `__init__` method.
     - An instance variable named `horn_volume` that has the value of the `horn_volume` parameter from the `__init__` method.

2. Create a property for the `year` instance variable. For the setter method, the `year` must be an `int` that is between `1900` and `2024`. If the value is not an `int`, raise a `TypeError` with the message `"Year must be an integer!"`. If the value is not between `1900` and `2024`, raise a `ValueError` with the message `"Year must be between 1900 and 2024!"`

3. Create a property for the `horn_volume` instance variable. For the setter method, the `horn_volume` must be an `int` that is between `1` and `10`. If the value is not an `int`, raise a `TypeError` with the message `"Horn Volume must be an integer!"`. If the value is not between `1` and `10`, raise a `ValueError` with the message `"Horn Volume must be between 1 and 10!"`

4. Create a property for the `make` instance variable. For the setter method, the `make` must be a `str` (string) that is at least 3 characters long. If the value is not a `str`, raise a `TypeError` with the message `"Make must be a string!"`. If the value is less than 3 characters long, raise a `ValueError` with the message `"Make must be at least 3 characters long!"`

5. Make an instance method called `honk_horn` that will print a message in the following format: "BEEP BEEP!". The number of exclamation marks '!' should be dependent on the value for the `horn_volume` instance variable. So if `horn_volume` has the value of `3`. There should be 3 exclamation marks `!` after "BEEP BEEP".
