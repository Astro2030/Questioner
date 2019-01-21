"""create and manage the database object"""
import psycopg2
import click
from flask.cli import with_appcontext
from flask import current_app, g

POSTGRES_CONFIG = {
    'host':'localhost',
    'port':5432,
    'user':'users',
    'password': 'password123',
    'database':'questioner'
}

def get_database():
    """create and return database connection object"""
    if 'database' not in g:
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


def init_database():
    """initialize the database schemas"""
    conn = get_database()
    with current_app.open_resource('api/v2/models/schema.sql') as q:
        conn.cursor().execute(q.read().decode('utf-8'))


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