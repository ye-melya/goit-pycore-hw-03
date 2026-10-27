from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
       
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            birthday_this_year = birthday.replace(year=today.year, day=28)

        if birthday_this_year < today:
            try:
                birthday_this_year = birthday.replace(year=today.year +1)
            except ValueError:
                        birthday_this_year = birthday.replace(year=today.year + 1, day=28)
          
        days= (birthday_this_year - today).days

        if 0 <= days < 7:
           congratulation_date = birthday_this_year

           if congratulation_date.weekday() ==5:
               congratulation_date = congratulation_date + timedelta(days=2)
           elif congratulation_date.weekday() ==6:
               congratulation_date = congratulation_date + timedelta(days=1)

           result.append({
               "name":user["name"],
               "congratulation_date":congratulation_date.strftime("%Y.%m.%d")
           })
    return result
users = [
    {"name": "John Doe", "birthday": "1995.10.26"},
    {"name": "Jane Smith", "birthday": "1990.10.31"}
]
print(get_upcoming_birthdays(users))
