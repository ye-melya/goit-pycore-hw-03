from datetime import datetime

def get_days_from_today(date):
    try:
        giv_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - giv_date).days
    except ValueError:
        return None

