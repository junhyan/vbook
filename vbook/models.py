from mongoengine import * 
     
class Book(Document):  
    book_id = StringField(required=True)  
    book_name = StringField(max_length=50)  
    book_author = StringField(max_length=50)  
    book_date = StringField(max_length=50)  

class Chapter(Document):  
    chap_id = StringField(required=True)
    chap_name = StringField(max_length=50)  
    chap_date = StringField(max_length=50)  
    chap_content = StringField(max_length=200)  
    book_id = StringField(required=True)
