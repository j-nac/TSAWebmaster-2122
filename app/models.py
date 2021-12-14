from app import db

class Merch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    image_file = db.Column(db.String(80))

    def __repr__(self):
        return '<Merchandise item {0}>'.format(self.name)