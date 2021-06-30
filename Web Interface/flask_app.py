from flask import Flask,render_template
from flask_paginate import Pagination,get_page_parameter,request,get_page_args
from model import db
from werkzeug.exceptions import abort
app = Flask(__name__)

@app.route("/blogs/")
def blogs():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    per_page = 5
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(db), search=search, record_name='articles',per_page=per_page)
    i=(page-1)*per_page
    items=db[i:i+per_page]
    return render_template("blogs.html",items=items,pagination=pagination)

@app.route("/")
def home():
    return render_template("index.html",title="Home")

@app.route("/content/<int:index>")
def article_content(index):
    if index < 0 or index > 19:
        abort(error)
    source=db[index-1]
    return render_template("article_content.html",title="Blogs",source=source)

@app.route("/comments/<int:index>")
def article_comments(index):
    if index < 0 or index > 19:
        abort(error)
    source=db[index-1]
    return render_template("article_comments.html",title="Comments",source=source)

@app.route("/about/")
def about():
    return render_template("about.html",title="About us")

@app.route("/404/")
def error():
    return render_template("404.html",title="404")

if __name__ == ('__main__'):
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)