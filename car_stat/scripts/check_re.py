from accounts.models import *
import re

def run():
    vehicles = Vehicle.objects.all()
    count = 0
    for v in vehicles:
        link = str(v.link)
        pattern = 'https\:\/\/www\.avito\.ru\/([a-z]+)\/avtomobili\/' \
                '([a-z\-]+)' \
                '\_' \
                '([a-z\_]*)' \
                '([a-z0-9\-]+)' \
                '\_' \
                '([a-z]*\d{0,1}\_*)|(\d*x*\d*)' \
                '([a-z]*\d{0,1}\_*)' \
                '(\d\d\d\d)'
        check = re.search(pattern, link)
        if not check:
            count += 1
            print(link)

    print(count)