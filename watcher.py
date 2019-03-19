import uwsgi
from uwsgidecorators import filemon

@filemon('mysite.wsgi')
def reloaded(num):
    uwsgi.reload()