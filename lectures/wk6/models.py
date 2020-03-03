

class User(db.Document):
    email = db.EmailField(unique=True, required=True)
    username = db.StringField(unique=True, required=True)
    password = db.StringField()
    img = db.ImageField()

user = User(username='Link', email='link@hyrule.com', password=hash)
user.img.put()
