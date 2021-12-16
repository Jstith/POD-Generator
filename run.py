#!/usr/bin/python3
import json
from datetime import datetime

# Method to generate first line
def getDay():
    while True:
        try:
            date = input("Enter day (i.e. 01JAN22):\n")
            day = datetime.strptime(date, '%d%b%y')
            break
        except Exception as e:
            print("improperly formatted date")
    str_builder = "# "
    str_builder += day.strftime('%A %d %B %Y')

    return str_builder

# Method to format the Duty Section
def getDuty():
    chdo = input("Enter CHDO:\n")
    rcdo = input("Enter RCDO:\n")
    acdo = input("Enter ACDO:\n")
    duty_section = input("Enter Duty Section:\n")

    str_builder = ""
    str_builder += "**CHDO** - " + chdo + "  \n"
    str_builder += "**RCDO** - " + rcdo + "  \n"
    str_builder += "**ACDO** - " + acdo + "  \n"
    str_builder += "**Duty Section** - " + duty_section + "  \n";

    return str_builder

# Method to format the uniform
def getUniform(data):
    print("Choose from the list of uniforms:")
    print("1)\tODUs")
    print("2)\tTrops")
    print("3)\tTrop Longs")
    print("4)\tSDBs")
    uniform = int(input("\n"))

    print("Choose from the list of covers:")
    print("1)\tClass-Specific Ballcaps")
    print("2)\tCombination Covers")
    print("3)\tGarrison Covers")
    cover = int(input("\n"))

    print("Choose from the list of jackets:")
    print("1)\tParkas")
    print("2)\tFleese")
    print("3)\tWindbreakers")
    print("4)\tTrenchcoats")
    print("5)\tBridgecoats")
    print("6)\tNone")
    jacket = int(input("\n"))

    str_builder = "**Uniform** - "
    str_builder += data["uniforms"][0][str(uniform)] + " "
    str_builder += data["uniforms"][1][str(cover)] + " "
    str_builder += data["uniforms"][2][str(jacket)]

    return str_builder

# Method to format daily schedule
def getSchedule(data):
    print("Select daily schedule template:")
    print("1)\tMonday")
    print("2)\tWednesday/Friday")
    print("3)\tTuesday/Thrusday")
    print("4)\tSaturday")
    print("5)\tSunday")
    weekday = input("\n")

    return data["schedules"][0][str(weekday)]

def main():
    data = json.loads(open('data.json').read())

    str_builder = ""
    str_builder += getDay()
    str_builder += "\n"
    str_builder += getDuty()
    str_builder += getUniform(data)
    str_builder += "\n\n"
    str_builder += getSchedule(data)

    print("\n" + str_builder)

if __name__ == "__main__":
    main()
