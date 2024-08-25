from .models import URLmodel
from .forms import URLform
from flask import render_template, url_for, redirect
from . import app, db
from .models import get_short


@app.route('/', methods=['POST', 'GET'])
def index():
    form = URLform()
    if form.validate_on_submit():
        url = URLmodel()
        url.original_url = form.original_url.data
        url.short = get_short()
        db.session.add(url)
        db.session.commit()
        return redirect(url_for('urls'))
    return render_template('index.html', form=form)


@app.route('/urls', methods=['GET'])
def urls():
    urls = URLmodel.query.all()
    return render_template('urls.html', urls=urls)


@app.route('/<string:short>', methods=['GET'])
def url_redirect(short):
    url = URLmodel.query.filter(URLmodel.short == short).first()
    if url:
        url.visits += 1
        db.session.add(url)
        db.session.commit()
        return redirect(url.original_url)
    return redirect(url_for('index'))
