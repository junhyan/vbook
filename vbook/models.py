from mongoengine import Document  
     
class TestModel(Document):  
    test_key = StringField(required=True)  
    test_value = StringField(max_length=50)  
