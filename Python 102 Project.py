from datetime import datetime

def parse_date(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))

        if year < 0 or month < 1 or day < 1 or month > 12:
            return None
        return datetime(year, month, day)
    except:
        return None

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

def get_day_name(birthdate):
    return birthdate.strftime("%A")

def collect_people():
    people = []
    while True:
        name = input('Enter name (or "exit" to finish): ').strip()
        if name.lower() == 'exit':
            break
        date_str = input('Enter birthdate (YYYY-MM-DD): ').strip()
        birthdate = parse_date(date_str)
        if birthdate is None:
            print(f"Invalid date - {name}")
            continue
        person = {
            'name': name,
            'age': calculate_age(birthdate),
            'day': get_day_name(birthdate)}
        people.append(person)
        return people

def display_results(people):
    print("\n=== Results ===")
    for person in people:
        print(f'{person["name"]} - Age: {person["age"]} - Born on: {person["day"]}')
    count = len(people)
    print(f"\n Total people: {count}")
    if count == 1:
        print('There is no oldest or youngest')
    elif count > 1:
        oldest = max(people, key=lambda p: p['age'])
        youngest = min(people, key=lambda p: p['age'])
        print(f"Oldest: {oldest['name']}  ({oldest['age']})")
        print(f"Youngest: {youngest['name']} ({youngest['age']})")

def main():
    people = collect_people()
    display_results(people)
if __name__ == '__main__':
    main()



