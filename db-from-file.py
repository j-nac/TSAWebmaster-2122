from app import db
from app.models import Item, Tag
from json import loads

for i in Tag.query.all():
    db.session.delete(i)
for i in Item.query.all():
    db.session.delete(i)
with open(input('enter the path to the file: \n')) as f:
    data = loads(f.read())

tags = []
for i in data:
    for t in i['Tags'].split(','):
        t = t.strip()
        if t not in tags:
            name = t

            new_tag = Tag(name=name)
            
            db.session.add(new_tag)
            db.session.commit()
nameid = {}
for t in Tag.query.all():
    nameid[t.name]=t.id

for i in data:
    tag_ids = [int(nameid[j.strip()]) for j in i['Tags'].split(',')]
    tags = []
    for j in tag_ids:
        tags.append(Tag.query.get(j))
    new_item = Item(name=i['Item name'], description=i['Item Description'], price=i['Item price'], image_file='merch-designs/'+i['Image path'], tags=tags)

    print(tags)
    db.session.add(new_item)
    db.session.commit()
