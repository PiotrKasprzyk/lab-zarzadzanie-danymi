from basicmodel import app, db, Student

app.app_context().push()

db.create_all()

piotr=Student('Piotr', 3)
andrzej=Student('Andrzej', 1)

print(piotr.id)
print(andrzej.id)

db.session.add_all([piotr, andrzej])

db.session.commit()

print(piotr.id)
print(andrzej.id)

print(piotr)
print(andrzej)