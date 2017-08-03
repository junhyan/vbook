from mongoengine import * 
     
class Book(Document):  
    book_id = StringField(required=True)  
    book_name = StringField(max_length=50)  
    book_author = StringField(max_length=50)  
    book_date = StringField(max_length=50)  
