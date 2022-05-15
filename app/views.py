from flask import render_template, url_for, redirect, flash, request
from app import app, db, mail, csrf
from app.models import Item, Tag
from app.forms import SearchStore, NewsletterForm, ContactForm
from flask_mail import Message, Attachment

msg = Message(subject='Never Gonna Give You Up', sender='Rick Astley', body='''We're no strangers to love\nYou know the rules and so do I\nA full commitment's what I'm thinking of\nYou wouldn't get this from any other guy\n\nI just wanna tell you how I'm feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWe've known each other for so long\nYour heart's been aching, but\nYou're too shy to say it\nInside, we both know what's been going on\nWe know the game and we're gonna play it\n\nAnd if you ask me how I'm feeling\nDon't tell me you're too blind to see\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\n(Ooh, give you up)\n(Ooh, give you up)\nNever gonna give, never gonna give\n(Give you up)\nNever gonna give, never gonna give\n(Give you up)\n\nWe've known each other for so long\nYour heart's been aching, but\nYou're too shy to say it\nInside, we both know what's been going on\nWe know the game and we're gonna play it\n\nI just wanna tell you how I'm feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you''')
with app.open_resource("./static/etc/rickroll.gif") as fp:
    msg.attach("./static/etc/rickroll.gif", "image/gif", fp.read())

@app.route('/', methods=['GET', 'POST', 'STATIC'])
@app.route('/index', methods=['GET', 'POST', 'STATIC'])
@app.route('/home', methods=['GET', 'POST', 'STATIC'])
def home():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('home.html', title='Home', newsletter_form=newsletter_form, file=file)

@app.route('/news', methods=['STATIC'])
def news():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    return ''

@app.route('/artists', methods=['GET', 'POST', 'STATIC'])
def artists():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('artists.html', title='Artists', newsletter_form=newsletter_form, file=file)

@app.route('/register', methods=['GET', 'POST', 'STATIC'])
def register():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('register.html', title='Register', newsletter_form=newsletter_form, file=file)

@app.route('/store', methods=['GET', 'POST', 'STATIC'])
@csrf.exempt
def store():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    
    search = request.args.get('search')
    tags = request.args.getlist('tags')
    if search == None or search == '':
        search_results = Item.query.all()
    else:
        search_results = Item.query.filter(Item.name.contains(search))
    
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

    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    redirect = '/store' if request.method == 'STATIC' else ''
    return render_template('store.html', title='Store', query_results=query_results, form=form, tags=tags, selected_tags=request.args.getlist('tags'), newsletter_form=newsletter_form, file=file, redirect=redirect, search = request.args.get('search'))

'''
To filter by tag:

Item.query.filter(Item.tags.contains(t))
where t is a database tag object
'''

@app.route('/items/<int:id>', methods=['GET', 'POST', 'STATIC'])
def item(id):
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)

    item = Item.query.get(id)
    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('item.html', title=f'{item.name} | Store' , item=item, newsletter_form=newsletter_form, file=file)

@app.route('/faq', methods=['GET', 'POST', 'STATIC'])
def faq():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)

    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('faq.html', title='FAQ', newsletter_form=newsletter_form, file=file)

@app.route('/contact', methods=['GET', 'POST', 'STATIC'])
def contact():
    newsletter_form = NewsletterForm()
    form = ContactForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    file=file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('contact.html', title='Contact', newsletter_form=newsletter_form, form=form, file=file)

@app.route('/sale-and-refund', methods=['GET', 'POST', 'STATIC'])
def refund():
    newsletter_form = NewsletterForm()
    form = ContactForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('refund.html', title='Sales & Refund', newsletter_form=newsletter_form, form=form)

@app.route('/privacy-policy', methods=['GET', 'POST', 'STATIC'])
def privacy():
    newsletter_form = NewsletterForm()
    form = ContactForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('privacy.html', title='Privacy Policy', newsletter_form=newsletter_form, form=form, file=file )

@app.route('/licensing', methods=['GET', 'POST', 'STATIC'])
def licensing():
    newsletter_form = NewsletterForm()
    form = ContactForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('licensing.html', title='Licensing', newsletter_form=newsletter_form, form=form, file=file)

@app.route('/tsa-info', methods=['GET', 'POST', 'STATIC'])
def tsa_info():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        msg.recipients = [newsletter_form.email.data]
        mail.send(msg)
    file = 'spa.html' if request.method == 'STATIC' else 'base.html'
    return render_template('tsa-info.html', title='TSA Info', newsletter_form=newsletter_form, file=file)