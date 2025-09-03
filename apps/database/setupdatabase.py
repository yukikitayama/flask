from basic import db, Puppy

# Create all the tables model
db.create_all()

sam = Puppy("Sammy", 3)
frank = Puppy("Frankie", 4)

# We should see None
print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])
# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)