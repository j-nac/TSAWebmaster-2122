from flask import render_template, url_for, redirect, flash, request
from app import app, db, csrf
from app.models import Item, Tag
from app.forms import SearchStore

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
@csrf.exempt
def store():
    tags = request.args.getlist('tags')
    query_results = []
    for tag_name in tags:
        # Get tag object
        tags_obj = Tag.query.filter_by(name=tag_name).first()
        if tags_obj == None:
            continue
        # Get items with tag
        mini_query_results = Item.query.filter(Item.tags.contains(tags_obj))
        for r in mini_query_results:
            # Don't include duplicates
            if r not in query_results:
                query_results.append(r)

    form = SearchStore()

    return render_template('store.html', title='Store', query_results=query_results, form=form)

'''
To filter by tag:

Item.query.filter(Item.tags.contains(t))
where t is a database tag object
'''

@app.route('/items/<int:id>')
def item(id):
    item = Item.query.get(id)
    return render_template('item.html', title=f'{item.name} | Store' , item=item)

@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQ')

@app.route('/tsa-info')
def tsa_info():
    return render_template('tsa-info.html', title='TSA Info')