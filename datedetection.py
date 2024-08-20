import re

# Regex to get dates in DD/MM/YYYY format
dateRegex = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')

text = 'Mark these important dates in your calendar: The project kickoff meeting is scheduled for 15/09/2024.Our team-building event will take place on 28/10/2024.The deadline for submitting the quarterly report is 30/11/2024.We will have a company-wide meeting on 01/12/2024.Remember to send out invitations by 05/12/2024 for the end-of-year party on 20/12/2024.The new product launch is planned for 07/01/2025.Training sessions will be held from 10/02/2025 to 12/02/2025.The last day to submit feedback on the new policy is 25/03/2025.Our Q1 review meeting is on 05/04/2025.The annual performance reviews start on 15/05/2025 and will end by 20/06/2025.'

mo = dateRegex.findall(text)

def datevalidator(date, month, year):
    date, month, year = int(date), int(month), int(year)
    if year < 1000 or year > 2999:
        return False
    if month in [4, 6, 9, 11]:
        if date > 30:
            return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if date > 29:
                return False
        else:
            if date > 28:
                return False
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if date > 31:
            return False
    else:
        return False

    return True

def validator(list_of_dates):
    validated_dates = []
    for x in list_of_dates:
        date, month, year = x[0], x[1], x[2]
        if datevalidator(date, month, year):
            validated_dates.append(f"{date}/{month}/{year}")
    return validated_dates

print(validator(mo))
