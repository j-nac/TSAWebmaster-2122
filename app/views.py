from flask import render_template, url_for, redirect, flash, request
from app import app, db, csrf, messages
from app.models import Item, Tag
from app.forms import SearchStore, NewsletterForm, ContactForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('home.html', title='Home', newsletter_form=newsletter_form)

@app.route('/artists', methods=['GET', 'POST'])
def artists():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('artists.html', title='Artists', newsletter_form=newsletter_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('register.html', title='Register', newsletter_form=newsletter_form)

@app.route('/store', methods=['GET', 'POST'])
@csrf.exempt
def store():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)

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

    return render_template('store.html', title='Store', query_results=query_results, form=form, tags=tags, newsletter_form=newsletter_form)

'''
To filter by tag:

Item.query.filter(Item.tags.contains(t))
where t is a database tag object
'''

@app.route('/items/<int:id>', methods=['GET', 'POST'])
def item(id):
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)

    item = Item.query.get(id)
    return render_template('item.html', title=f'{item.name} | Store' , item=item, newsletter_form=newsletter_form)

@app.route('/faq', methods=['GET', 'POST'])
def faq():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)

    return render_template('faq.html', title='FAQ', newsletter_form=newsletter_form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    newsletter_form = NewsletterForm()
    form = ContactForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('contact.html', title='Contact', newsletter_form=newsletter_form, form=form)

@app.route('/tsa-info', methods=['GET', 'POST'])
def tsa_info():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('tsa-info.html', title='TSA Info', newsletter_form=newsletter_form)