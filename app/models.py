from app import db

'''
The item table has all the normal stuff. However, each item can have multiple tags. Thus, there is the tag table which contains all the tag information. The two tables are connected via the tags_link table and relationships.

- https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_many_to_many_relationships.htm
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships
- https://stackoverflow.com/questions/25668092/flask-sqlalchemy-many-to-many-insert-data

The documentation is piss
'''

tags_link = db.Table('tags_link',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    image_file = db.Column(db.String(80))
    tags = db.relationship('Tag', secondary=tags_link)

    def __repr__(self):
        return f'<Item {self.name}>'

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Tag {self.name}>'