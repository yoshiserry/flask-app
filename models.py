from app import db


class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    details = db.Column(db.String, nullable=False)

    def __init__(self, title, details):
        self.title = title
        self.details = details

    def __repr__(self):
        return '<title {}'.format(self.title, self.details)
