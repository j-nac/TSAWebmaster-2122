from app import db
from app.models import Item, Tag

if __name__ == '__main__':
    while True:
        command = int(input('What do you want to do?\n1. Show items\n2. Add item\n3. Delete item\n4. Show tags\n5. Add tag\n6. Delete tag\n7. Quit\n> '))

        if command == 1:
            item_query = Item.query.all()
            for i in item_query:
                print(f'Item {i.id} - {i.name}')
                print(f'Price: {i.price}')
                print(f'Description: {i.description}')
                print(f'Tags: {[t.name for t in i.tags]}')
                print('\n')
            input('Press ENTER to close')
            
        elif command == 2:
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
        
        elif command == 3:
            item_query = Item.query.all()
            for i in item_query:
                print(f'{i.id}. {i.name}')
            item_del = int(input('Item to delete: '))
            obj_item_del = Item.query.get(item_del)
            confirm = input(f'Are you sure you want to delete {obj_item_del.name} (y/n): ')
            if confirm == 'y':
                db.session.delete(obj_item_del)
                db.session.commit()
                print('Done')
            else:
                print('Operation cancelled')
        
        elif command == 4:
            tag_query = Tag.query.all()
            for t in tag_query:
                print(f'Tag {t.id} - {t.name}')
            input('Press ENTER to close')

        elif command == 5:
            print('Create tag')
            name = input('Name: ')

            new_tag = Tag(name=name)
            
            db.session.add(new_tag)
            db.session.commit()
            print('Done')
        
        elif command == 6:
            tag_query = Tag.query.all()
            for t in tag_query:
                print(f'{t.id}. {t.name}')
            tag_del = int(input('Tag to delete: '))
            obj_tag_del = Tag.query.get(tag_del)
            confirm = input(f'Are you sure you want to delete {obj_tag_del.name} (y/n): ')
            if confirm == 'y':
                db.session.delete(obj_tag_del)
                db.session.commit()
                print('Done')
            else:
                print('Operation cancelled')
        
        else:
            print('Goodbye')
            break