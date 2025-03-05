from models.__init__ import CONN, CURSOR
from data_structure_examples.singly_linked_list import SinglyLinkedList, Node

class Page:

    singly_linked_list = SinglyLinkedList()

    # Add a next_node parameter to the __init__() method that has a default value of None
    def __init__(self, text):
        self.text = text
        # Create a next_node instance variable that will have the value of the next_node parameter

    @property
    def text_getter(self):
        return self._text
    
    @text_getter.setter
    def text(self, value):
        if (type(value) == str) and (len(value) > 0):
            self._text = value
        else:
            raise Exception("Error: Text must be at least 1 character long!")
        
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pages (
                id INTEGER PRIMARY KEY,
                text TEXT
            )
        '''

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS pages
        '''

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO pages (text)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.text,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        # Append to the SinglyLinkedList containing the Page instances

    @classmethod
    def create(cls, text):
        page = cls(text)
        page.save()
        return page
    
    @classmethod
    def instance_from_db(cls, row):
        page = cls(row[1])
        page.id = row[0]
        return page
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM pages
        """

        rows = CURSOR.execute(sql).fetchall()

        # Update the singly_linked_list class variable that contains the SinglyLinkedList used to store the data for the pages to contain the data for the rows obtained from the pages table.
        return cls.singly_linked_list