from flask import g     #Global Context
import sqlite3

DATABASE="user.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db