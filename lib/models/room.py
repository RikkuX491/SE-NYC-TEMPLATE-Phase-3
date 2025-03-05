from models.__init__ import CONN, CURSOR
from data_structure_examples.doubly_linked_list import DoublyLinkedList, Node

class Room:

    doubly_linked_list = DoublyLinkedList()

    # Add next_node and prev_node parameters to the __init__() method that both have a default value of None
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # Create a next_node instance variable that will have the value of the next_node parameter
        # Create a prev_node instance variable that will have the value of the prev_node parameter

    @property
    def name_getter(self):
        return self._name
    
    @name_getter.setter
    def name(self, value):
        if (type(value) == str) and (len(value) > 0):
            self._name = value
        else:
            raise Exception("Error: Name must be at least 1 character long!")
        
    @property
    def description_getter(self):
        return self._description
    
    @description_getter.setter
    def description(self, value):
        if (type(value) == str) and (len(value) > 0):
            self._description = value
        else:
            raise Exception("Error: Description must be at least 1 character long!")
        
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
            )
        '''

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS rooms
        '''

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO rooms (name, description)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.description))
        CONN.commit()

        self.id = CURSOR.lastrowid

        # Append to the DoublyLinkedList containing the Room instances

    @classmethod
    def create(cls, name, description):
        room = cls(name, description)
        room.save()
        return room
    
    @classmethod
    def instance_from_db(cls, row):
        room = cls(row[1], row[2])
        room.id = row[0]
        return room
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM rooms
        """

        rows = CURSOR.execute(sql).fetchall()

        # Update the doubly_linked_list class variable that contains the DoublyLinkedList used to store the data for the rooms to contain the data for the rows obtained from the rooms table.
        return cls.doubly_linked_list