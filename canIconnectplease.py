from pymodm import connect, MongoModel, fields

connect("mongodb+srv://cz124:mongo_db@cluster0.jdfcs.mongodb.net/"
        "myFirstDatabase?retryWrites=true&w=majority")


class User(MongoModel):
    name=fields.CharField()
    

x = User(name='David')
x.save()