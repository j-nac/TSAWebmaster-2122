from flask import render_template, url_for, redirect, flash, request
from app import app, db, csrf
from app.models import Item, Tag
from app.forms import SearchStore, NewsletterForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('home.html', title='Home', newsletter_form=newsletter_form)

@app.route('/artists')
def artists():
    return render_template('artists.html', title='Artists')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/store')
@csrf.exempt
def store():
    search = request.args.get('search')
    if search == None or search == '':
        search_results = Item.query.all()
    else:
        search_results = Item.query.filter(Item.name.contains(search))
    
    tags = request.args.getlist('tags')
    tag_results = []
    for tag_name in tags:
        # Get tag object
        tags_obj = Tag.query.filter_by(name=tag_name).first()
        if tags_obj == None:
            continue
        # Get items with tag
        mini_tag_results = Item.query.filter(Item.tags.contains(tags_obj))
        for r in mini_tag_results:
            # Don't include duplicates
            if r not in tag_results:
                tag_results.append(r)
    
    if len(tags) == 0:
        tag_results = Item.query.all()
    
    query_results = list(set(search_results).intersection(tag_results))

    form = SearchStore()
    tags = Tag.query.all()

    return render_template('store.html', title='Store', query_results=query_results, form=form, tags=tags)

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