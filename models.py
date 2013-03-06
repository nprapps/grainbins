import datetime

from peewee import *

db = SqliteDatabase('data/grain.db')


class Incident(Model):
    """
    A single incident.
    Inspection_no is _sorta_ a primary key.
    But some of them have dots and stuff in them.
    """
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
        """
        Return a prettified version of the incident date.
        """
        date = datetime.date(
            int(self.incident_date.split('-')[0].strip()),
            int(self.incident_date.split('-')[1].strip()),
            int(self.incident_date.split('-')[2].strip()))
        return date.strftime('%B %e, %Y')
