from app import db
from app.models import Item, Tag

if __name__ == '__main__':
    while True:
        command = int(input('What do you want to do?\n1. Add item\n2. Add tag\n3. Quit\n> '))

        if command == 1:
            print('Create item')

            name = input('Name: ')
            description = input('Description: ')
            price = float(input('Price: '))
            image_file = input('Image filename: ')

            # Print list of tags
            tag_query = Tag.query.all()
            for t in tag_query:
                print(f'{t.id}. {t.name}')

            # Add tags
            tag_ids = str(input('Tags (separate with space): '))
            tag_ids = [int(x) for x in tag_ids.split()]
            tags = []
            for i in tag_ids:
                tags.append(Tag.query.get(i))

            new_item = Item(name=name, description=description, price=price, image_file=image_file, tags=tags)

            db.session.add(new_item)
            db.session.commit()
            print('Done')

        elif command == 2:
            print('Create tag')
            name = input('Name: ')

            new_tag = Tag(name=name)
            
            db.session.add(new_tag)
            db.session.commit()
            print('Done')
        
        else:
            print('Goodbye')
            break