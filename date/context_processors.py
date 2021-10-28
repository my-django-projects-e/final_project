import datetime


def current_date(request):
    return {'today': datetime.date.today()}
