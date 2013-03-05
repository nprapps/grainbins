#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

from models import Incident

url_base = 'http://www.osha.gov/pls/imis/establishment.inspection_detail?id='

for incident in Incident.select():
    if incident.narrative:
        pass
    else:
        try:
            url = url_base + '%s' % incident.inspection_no
            print url
            r = requests.get(url)
            soup = BeautifulSoup(r.content)

            tables = soup.find(id="maincontain").find_all('table', bgcolor='white')
            num_matches = len(tables)
            narrative = tables[num_matches-3].find('td').text.strip()

            print narrative
            query = Incident.update(narrative=narrative).where(Incident.inspection_no == incident.inspection_no)
            print query
            query.execute()
        except Exception as error:
            print 'Failed: %s, error is: %s' % (incident.inspection_no, error)
