#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.page import Page
from models.room import Room

def seed_database():
    Page.drop_table()
    Room.drop_table()

    Page.create_table()
    Room.create_table()

    # Create seed data
    Page.create("Once upon a time, I woke up bright and early in the morning. I was so sleepy, so I decided to make a cup of Java coffee. But then I realized that I forgot how to make coffee. Luckily for me, I wrote a Script that reminds me of how to make Java coffee. Get it? Java Script?")
    Page.create("How did you React to my programming joke?")
    Page.create("I just remembered that it was time to feed my Python.")
    Page.create("Before leaving from home, I decided to store the rest of my coffee in a Flask. Off we go to the Flatiron School Software Engineering bootcamp!")

    Room.create("Alan Turing Classroom", "Welcome to Alan Turing Classroom - where your journey begins and ends. Exciting events including instructor kickoffs, project presentations, and Switch 'N Brew takes places in this action-packed room. This is also one of rooms you'll find instructors giving lectures in.")
    Room.create("Collins Classroom", "Welcome to Collins Classroom! Enjoy the lovely views offered outside the windows. It's yet another one of our rooms you'll find instructors giving lectures in.")
    Room.create("Kay Classroom", "Welcome to Kay Classroom - a pretty quiet and chill classroom near the phone booths, lockers, and instructor tables.")
    Room.create("Katherine Johnson Workroom", "Welcome to Katherine Johnson Workroom - the quiet space for students to focus on getting those assignments done, or also to relax away from all of the noise.")
    Room.create("Teacher's Lounge", "401 Unauthorized")

seed_database()
print("🌱 Pages and Rooms successfully seeded! 🌱")