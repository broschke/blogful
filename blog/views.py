from flask import render_template

from . import app
from .database import session, Entry

@app.route("/")
def entries():
    entries = session.query(Entry)
    entries = entries.order_by(Entry.datetime.desc())
    entries = entries.all()
    return render_template("entries.html",entries=entries)

@app.route("/entry/<id>")
def entry(id):
    entry = session.query(Entry)
    entry = entry.get(id)
    return render_template("entry.html",entry=entry)
