import datetime

from peewee import *

db = SqliteDatabase('data/grain.db')


class Incident(Model):
    inspection_no = PrimaryKeyField()
    name = CharField()
    age = IntegerField()
    incident_date = CharField()
    state = CharField()
    zip_code = IntegerField()
    initial_fine = IntegerField()
    current_fine = IntegerField()
    narrative = TextField()

    class Meta:
        database = db
        db_table = 'grain'

    def clean_incident_date(self):

        date = datetime.date(
            int(self.incident_date.split('-')[0].strip()),
            int(self.incident_date.split('-')[1].strip()),
            int(self.incident_date.split('-')[2].strip()))
        return date.strftime('%b. %e, %Y')
