from datetime import datetime


def get_birthdays_per_week(lst):
    result = ""
    schedule = {"Monday": [],
                "Tuesday": [],
                "Wednesday": [],
                "Thursday": [],
                "Friday": []}

    for person in lst:
        birthday = datetime.strptime(person["birthday"], "%d.%m.%Y").date()
        this_year = birthday.replace(2023)
        # print(f'{person["name"]}: {birthday}')
        weekday = this_year.strftime("%A")
        # print(weekday)

        for key in schedule.keys():
            if key == weekday:
                schedule[weekday].append(person["name"])
        if weekday == "Saturday" or weekday == "Sunday":
            schedule["Monday"].append(person["name"])

    for day in schedule.keys():
        result += f"{day}: {', '.join(schedule[day])}\n"

    return result


users = [{"name": "Jack", "birthday": "12.07.1998"},
         {"name": "Diana", "birthday": "20.01.2002"},
         {"name": "Bob", "birthday": "19.03.2003"},
         {"name": "Klara", "birthday": "02.08.2000"},
         {"name": "Bill", "birthday": "01.08.1996"},
         {"name": "Kim", "birthday": "05.05.2005"}]

print(get_birthdays_per_week(users))
