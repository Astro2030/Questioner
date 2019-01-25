"""create and manage the database object"""
import psycopg2
import click
from werkzeug.security import generate_password_hash
import os
from flask.cli import with_appcontext
from flask import current_app, g
from sys import modules

def get_database():
    """create and return database connection object"""
    if os.getenv('APP_SETTINGS') == 'testing':
        g.db_conn = psycopg2.connect(
            host='localhost',port=5432,user='postgres',password= 'password1234', database='test_db'
        )
        g.db_conn.autocommit = True
    else :
        g.db_conn = psycopg2.connect(
            host='localhost',port=5432,user='postgres',password= 'password1234',database='questioner'
        )
        g.db_conn.autocommit = True
    return g.db_conn


def close_database(error=None):
    """remove the database connection from app context and close it"""
    db_conn = g.pop('database', None)
    if db_conn is not None:
        db_conn.close()

def create_admin(conn):
    hashed=generate_password_hash('Andela1!!!')
    query = "INSERT INTO users (firstname,lastname,username,email,is_admin,password)" \
            "VALUES('wycliffe','omari', 'cliffe', 'omariwycliffe5@gmail.com',True, %(password)s);"
    cur = conn.cursor()
    cur.execute(query, {'password':hashed})


def init_database():
    """initialize the database schemas"""
    conn = get_database()
    with current_app.open_resource('api/v2/models/schema.sql') as q:
        conn.cursor().execute(q.read().decode('utf-8'))

    #admin
    create_admin(conn)
    
        


@click.command('init-db')
@with_appcontext
def init_db_command():
    """reset database content"""
    init_database()
    click.echo('Initialized database')


def reg_app(app):
    """register the application object"""
    app.teardown_appcontext(close_database)
    app.cli.add_command(init_db_command)