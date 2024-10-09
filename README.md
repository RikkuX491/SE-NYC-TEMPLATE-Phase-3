# Lecture # 4 - OOP Part 2: Class Methods & Class Variables

## Lecture Topics

- Class variables
- Class methods (`@classmethod`)

## Introduction

In today's lecture, we will discuss more topics of Object Oriented Programming in Python including class variables and class methods.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install `pytest` and any other required packages.

2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

## Deliverables

Write your code in `lib/car.py` (the `car.py` file in the `lib` directory / folder)

1. Create a class attribute, `all`. We will use this attribute to keep track of the new `Car` instances that are created from the `Car` class. Set this attribute equal to `[]`. Then in `__init__`, you will need to append the new `Car` instances to the list contained within the `all` class attribute for the `Car` class.

2. Create a class method, `average_year()` that will return the average year for all cars created.