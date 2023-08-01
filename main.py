from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    current_date = datetime.now()
    week_later = current_date + timedelta(days=7)

    this_week_birthdays = {i: [] for i in range(7)}

    for user in users:
        user["birthday"] = datetime(current_date.year, user["birthday"].month, user["birthday"].day)
        birthday = user["birthday"]

        if current_date <= birthday <= week_later:
            week_day = birthday.weekday()
            week_day = 0 if week_day >= 5 else week_day

            this_week_birthdays[week_day].append(user['name'])

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    for index, names in this_week_birthdays.items():
        if names:
            day = days[index]
            print(f"{day}: {', '.join(names)}")

users = [
    {"name": "John", "birthday": datetime(1995, 7, 31)},
    {"name": "Emily", "birthday": datetime(1980, 7, 31)},
    {"name": "Chris", "birthday": datetime(1998, 8, 1)},
    {"name": "Anna", "birthday": datetime(1972, 8, 3)},
    {"name": "David", "birthday": datetime(2001, 8, 3)},
    {"name": "Sophia", "birthday": datetime(1999, 8, 5)},
    {"name": "Michael", "birthday": datetime(1985, 8, 7)},
]

get_birthdays_per_week(users)