# django-scapy
Web Based Network Protocol Analyzer using Django and Scapy

This a WIP. For now ony python3 is supported.

Quick install:
- clone the repo
- create a postgres DB scapy
- create a dbuser: createuser scapy -s -P (pass also scapy)
- create a virtuenv for the project and activate it
- install deps: go to requirements and run: pip install -r development.txt
- install lbdnet; OSX: brew install libdnet
- run: python manage.py migrate
- run: python manage.py createsuperuser

