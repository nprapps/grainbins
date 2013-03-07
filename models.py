import datetime

from peewee import *

db = SqliteDatabase('data/grain.db')


class Incident(Model):
    """
    A single incident.
    Inspection_no is _sorta_ a primary key.
    But some of them have dots and stuff in them.
    """
    # First round of fields.
    inspection_no = PrimaryKeyField()
    name = CharField()
    age = IntegerField()
    incident_date = CharField()
    state = CharField()
    zip_code = IntegerField()
    initial_fine = IntegerField()
    current_fine = IntegerField()
    narrative = TextField()

    # Second round of fields.
    postofficename = CharField()
    lat = CharField()
    long = CharField()
    sqmiles = FloatField()
    pop2010 = CharField()
    cityfips = CharField()

    class Meta:
        database = db
        db_table = 'grain'

    def osha_url(self):
        """
        Return the OSHA URL for this incident.
        """
        return

    def clean_incident_date(self):
        """
        Return a prettified version of the incident date.
        """
        date = datetime.date(
            int(self.incident_date[0:4].strip()),
            int(self.incident_date[4:6].strip()),
            int(self.incident_date[6:8].strip()))
        return date.strftime('%B %e, %Y')
