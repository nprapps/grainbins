import datetime
import locale
import math

from peewee import *

db = SqliteDatabase('data/grain.db')

# Set locale to US for comma printing.
locale.setlocale(locale.LC_ALL, '')


class Incident(Model):
    """
    A single incident.
    Inspection_no is _sorta_ a primary key.
    But some of them have dots and stuff in them.
    """
    # First round of fields.
    inspection_no = CharField()
    name = CharField()
    age = IntegerField()
    incident_date = PrimaryKeyField()
    state = CharField()
    zip_code = IntegerField()
    initial_fine = IntegerField()
    current_fine = IntegerField()
    narrative = TextField()

    # Second round of fields.
    postofficename = CharField()
    lat = CharField()
    long = CharField()
    cityfips = CharField()

    class Meta:
        database = db
        db_table = 'grain'

    def get_state_img(self):
        dec = str(self.inspection_no).split('.0')
        if dec[1] == None:
            return 'img/maps/%s.png' % self.inspection_no
        else:
            return 'img/maps/%s.png' % dec[0]

    def osha_url(self):
        """
        Return the OSHA URL for this incident.
        """
        return 'http://www.osha.gov/pls/imis/establishment.inspection_detail?id=%s' % self.inspection_no

    def clean_incident_date(self):
        """
        Return a prettified version of the incident date.
        """
        date = datetime.date(
            int(str(self.incident_date)[0:4].strip()),
            int(str(self.incident_date)[4:6].strip()),
            int(str(self.incident_date)[6:8].strip()))
        return date.strftime('%B %e, %Y')

    def fine_percent_reduction(self):
        if self.initial_fine and self.current_fine:
            fine_reduction = (float(self.initial_fine) - float(self.current_fine))
            percent_decrease = fine_reduction / float(self.initial_fine)
            return int(percent_decrease * 100)

    def clean_fine_amount(self, fine):
        """
        Return the fine amount with commas.
        """
        if fine:
            # Handle "none" fines
            commafied_fine = locale.format("%d", fine, grouping=True)
            return commafied_fine
        else:
            return fine
