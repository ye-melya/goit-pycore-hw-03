from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year+1)
        days= (birthday_this_year - today).days

        if 0 <= days < 7:
            cong_date = birthday_this_year

            if cong_date.weekday() ==5:
                cong_date = cong_date + timedelta(days=2)
            elif cong_date.weekday() ==6:
                cong_date = cong_date + timedelta(days=1)

            result.append({
                "name":user["name"],
                "cong_date":cong_date.strftime("%Y.%m.%d")
            })
    return result
users = [
    {"name": "John Doe", "birthday": "1995.10.26"},
    {"name": "Jane Smith", "birthday": "1990.10.31"}
]
print(get_upcoming_birthdays(users))