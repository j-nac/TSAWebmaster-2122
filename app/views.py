from flask import render_template, url_for, redirect, flash, request
from app import app, db
from app.models import Item, Tag

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/artists')
def artists():
    return render_template('artists.html', title='Artists')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/store')
def store():
    tags = request.args.get('tags')
    if tags == None:
        query_results = Item.query.all()
    else:
        if ',' in tags:
            tags = tags.split(',')
        else:
            tags = [tags]
        query_results = []
        for tag_name in tags:
            tags_obj = Tag.query.filter_by(name=tag_name).first()
            if tags_obj == None:
                continue
            mini_query_results = Item.query.filter(Item.tags.contains(tags_obj))
            for r in mini_query_results:
                if r not in query_results:
                    query_results.append(r)
    return render_template('store.html', title='Store', query_results=query_results)

'''
To filter by tag:

Item.query.filter(Item.tags.contains(t))
where t is a database tag object
'''

@app.route('/items/<int:id>')
def item(id):
    item = Item.query.get(id)
    return render_template('store-item.html', title=f'{item.name} | Store' , item=item)

@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQ')

@app.route('/tsa-info')
def tsa_info():
    return render_template('tsa-info.html', title='TSA Info')