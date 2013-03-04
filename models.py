from peewee import *

db = SqliteDatabase('data/grain.db')

class Incident(Model):
    inspection_no = PrimaryKeyField()
    name = CharField()
    age = IntegerField()
    incident_date = DateField()
    state = CharField()
    zip_code = IntegerField()
    initial_fine = IntegerField()
    current_fine = IntegerField()
    narrative = TextField()

    class Meta:
        database = db
        db_table = 'grain'
