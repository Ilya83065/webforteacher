from app import db
import re


def slagify(t):
    pat = r'[^/w+]'
    return re.sub(pat, '-', t)



class mod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titl = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(mod, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.cre:
            self.slug = slagify(self.titl)

    def __repr__(self):
        return '<id: {}, title: {}>'.format(self.id, self.cre)
