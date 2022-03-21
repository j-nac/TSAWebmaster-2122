from flask import render_template, url_for, redirect, flash, request
from app import app, db, mail, csrf
from app.models import Item, Tag
from app.forms import SearchStore, NewsletterForm, ContactForm
from flask_mail import Message, Attachment

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
        msg = Message(subject='Never Gonna Give You Up',
            sender='Rick Astley',
            recipients=[newsletter_form.email.data],
            body='''We're no strangers to love
            You know the rules and so do I
            A full commitment's what I'm thinking of
            You wouldn't get this from any other guy
            
            I just wanna tell you how I'm feeling
            Gotta make you understand
            
            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you

            We've known each other for so long
            Your heart's been aching, but
            You're too shy to say it
            Inside, we both know what's been going on
            We know the game and we're gonna play it
            
            And if you ask me how I'm feeling
            Don't tell me you're too blind to see
            
            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you

            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you

            (Ooh, give you up)
            (Ooh, give you up)
            Never gonna give, never gonna give
            (Give you up)
            Never gonna give, never gonna give
            (Give you up)

            We've known each other for so long
            Your heart's been aching, but
            You're too shy to say it
            Inside, we both know what's been going on
            We know the game and we're gonna play it

            I just wanna tell you how I'm feeling
            Gotta make you understand

            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you

            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you

            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you''',
            attachments=[Attachment(filename='app/static/etc/rickroll.gif')])
        mail.send(msg)
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

@app.route('/sale-and-refund', methods=['GET', 'POST'])
def refund():
    newsletter_form = NewsletterForm()
    form = ContactForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('refund.html', title='Sales & Refund', newsletter_form=newsletter_form, form=form)

@app.route('/privacy-policy', methods=['GET', 'POST'])
def privacy():
    newsletter_form = NewsletterForm()
    form = ContactForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('privacy.html', title='Privacy Policy', newsletter_form=newsletter_form, form=form)

@app.route('/licensing', methods=['GET', 'POST'])
def licensing():
    newsletter_form = NewsletterForm()
    form = ContactForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('licensing.html', title='Licensing', newsletter_form=newsletter_form, form=form)

@app.route('/tsa-info', methods=['GET', 'POST'])
def tsa_info():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email.data)
    return render_template('tsa-info.html', title='TSA Info', newsletter_form=newsletter_form)