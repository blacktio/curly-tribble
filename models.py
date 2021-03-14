from app import db


class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    surname = db.Column(db.String(250))
    email = db.Column(db.String(250))
    country = db.Column(db.String(250))

    def __str__(self):
        return (
            f'Id: {self.id}'
            f'Name: {self.name}'
            f'Surname: {self.surname}'
            f'Email: {self.email}'
            f'Country: {self.country}'
        )

