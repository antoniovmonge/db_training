import sqlalchemy as db

engine = db.create_engine('sqlite:///users-sqlalchemy.db')

metadata = db.MetaData()

connection = engine.connect()

users = db.Table(
    'Users',
    metadata, 
    db.Column('user_id', db.Integer, primary_key=True),
    db.Column('first_name', db.Text),
    db.Column('last_name', db.Text),
    db.Column('email_address', db.Text)
)

metadata.create_all(engine)

insertion_query = users.insert().values([
    {'first_name': 'Taliban','last_name':'Pachacho','email_address': 'taliban@explota.com'},
    {'first_name':'Jibiri' ,'last_name':'Jibiri' ,'email_address': 'jibiri@jibiri.com'},
    {'first_name': 'Rafaela','last_name':'Carra' ,'email_address': 'mexplota@mexplota.mexplo'},
    {'first_name': 'Donald','last_name': 'Trump','email_address': 'subnormal@naranja.com'},
    {'first_name': 'Otro','last_name': 'Pachacho','email_address': 'please@stop.ya'}
])

connection.execute(insertion_query)

selection_query = db.select([users.columns.email_address])
selection_result = connection.execute(selection_query)

print(selection_result.fetchall())