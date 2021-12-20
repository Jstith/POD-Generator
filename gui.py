#!/usr/bin/python3
import PySimpleGUI as sg
from datetime import datetime

dict_uniforms = {
    "ODUs":"Operational Dress Uniforms",
    "Trops":"Tropical Blue Uniforms",
    "Long Sleeve Trops":"Long Sleeve Tropical Blue Uniforms",
    "SDBs":"Service Dress Bravo Uniforms"
}

dict_covers = {
    "Class-Specific Ballcaps":"with Class-Specific Ballcaps",
    "Combo Covers":"with Combination Covers",
    "Garrison Covers":"with Garrison Covers"
}

dict_jackets = {
    "Parkas":"and **Parkas**",
    "Fleeces":"and **Fleeses**",
    "Windbreakers":"and **Windbreakers**",
    "Trenchcoats":"and **Trenchcoats**",
    "Bridgecoats":"and **Bridgecoats**",
    "None":""
}

dict_schedules = {
    "Monday":"0600: Reveille\n0615: Guardmount\n**0620: Morning Formation**\n0625: Family Style Breakfast\n0800-1150: Morning Classes\n**1205: Afternoon Formation**\n1210: Family Style Lunch\n1250-1540: Afternoon Classes\n1600-1800: Sports Period\n1715-1915: Buffet Dinner\n1930: Restricted Cadet Formation\n2200: Taps/Restricted Cadet Formation",
    "Wed/Fri":"0600: Reveille\n0615: Guardmount\n0630-0800: Buffet Breakfast\n**0740: Morning Formation**\n0800-1150: Morning Classes\n**1205: Afternoon Formation**\n1210: Family Style Lunch\n1250-1540: Afternoon Classes\n1600-1800: Sports Period\n1715-1915: Buffet Dinner\n1930: Restricted Cadet Formation\n2200: Taps/Restricted Cadet Formation",
    "Tues/Thur":"0600: Reveille\n0615: Guardmount\n0630-0800: Buffet Breakfast\n**0740: Morning Formation**\n0800-1205: Morning Classes\n**1220: Afternoon Formation**\n1225: Family Style Lunch\n1300-1540: Afternoon Classes\n1600-1800: Sports Period\n1715-1915: Buffet Dinner\n1930: Restricted Cadet Formation\n2200: Taps/Restricted Cadet Formation",
    "Saturday":"0645: Guardmount\n0730: Reveille\n**0745: Morning Formation (UOD)**\n0630-0800: Buffet Breakfast\n1300: Restricted Cadet Formation\n1600: Restricted Cadet Formation\n1700-1800: Buffet Dinner\n1930: Restricted Cadet Formation\n2200: Taps/Restricted Cadet Formation",
    "Sunday":"0715: Guardmount\n0800-0915: Buffet Breakfast\n**Sunday Religious Schedule**\n0830-1000: Latter Day Saints Sunday School (Smith129)\n0900-1000: Catholic Mass (Memorial Chapel)\n0900-1000: Protestant Sunday School (Satterlee 128)\n1000-1030: Catholic and Protestant Fellowship (Memorial Chapel)\n1000-1200: Other Faith Groups (Leamy Hall)\n1030-1130: Protestant Worship (Memorial Chapel)\n1100-1230: Buffet Lunch\n1300: Restricted Cadet Formation\n1600: Restricted Cadet Formation\n1700-1800: Buffet Dinner\n1930: Restricted Cadet Formation\n2200: Taps/Restricted Cadet Formation"
}

hasError = False

# Method to get first line
def getDay(window, date):
    global hasError
    try:
        day = datetime.strptime(date, '%d%b%y')
        str_builder = "# "
        str_builder += day.strftime('%A %d %B %Y')
        str_builder += '\n'
    except Exception as e:
        print("improperly formatted date")
        hasError = True
        window['error_message'].update('Invalid date format.')
        str_builder = 'DATE_FORMAT_ERROR\n'
    return str_builder

# Method to format the Duty Section
def getDuty(window, chdo, rcdo, acdo, duty_section):
    global hasError
    for x in vars().values():
        if x == '':
            hasError = True
            window['error_message'].update('Missing duty information.')
            str_builder = 'DUTY_FORMAT_ERROR\n'
            return str_builder
    str_builder = ""
    str_builder += "**CHDO** - " + chdo + "  \n"
    str_builder += "**RCDO** - " + rcdo + "  \n"
    str_builder += "**ACDO** - " + acdo + "  \n"
    str_builder += "**Duty Section** - " + duty_section + "  \n";
    return str_builder

# Method to format the uniform
def getUniform(window, uniform, cover, jacket):
    global hasError
    str_builder = "**Uniform** - "
    if(uniform in dict_uniforms.keys() and cover in dict_covers.keys() and jacket in dict_jackets.keys()):
        str_builder += dict_uniforms[uniform] + " "
        str_builder += dict_covers[cover] + " "
        str_builder += dict_jackets[jacket]
        return str_builder
    else:
        hasError = True
        window['error_message'].update('Invalid uniform selection. (Use dropdown menus)')
        str_builder = 'UNIFORM_FORMAT_ERROR\n'
        return str_builder

# Method to format daily schedule
def getSchedule(window, weekday):
    global hasError
    if(weekday in dict_schedules.keys()):
        return dict_schedules[weekday]
    else:
        hasError = True
        window['error_message'].update('Invalid weekday selection (Use dropdowm menus)')
        return 'WEEKDAY_FORMAT_ERROR\n'

def gen_pod(window, values):
    global hasError
    str_builder = ''
    str_builder += getDay(window, values['inp_date'])
    str_builder += getDuty(window, values['inp_chdo'], values['inp_rcdo'], values['inp_acdo'], values['inp_dutySection'])
    str_builder += getUniform(window, values['uniform'], values['cover'], values['jacket'])
    #str_builder += getSchedule(data, values['weekday'])
    arr_added = getSchedule(window, values['weekday']).split('\n')
    #print('arrAdded')
    #print(type(arr_added))
    #print(arr_added)
    arr_toAdd = values['event_box'].strip()
    arr_toAdd = arr_toAdd.split('\n')
    #print('arr')
    #print(type(arr_toAdd))
    #print(arr_toAdd)
    if(not arr_toAdd == ['']):
        add_indexes = [0]*len(arr_toAdd)
        counter = 0
        for value in arr_toAdd:
            #print(value)
            try:
                stripped = int(value.split(':')[0])
            except ValueError:
                hasError = True
                window['error_message'].update('Invalid Schedule formatting. Please input in the format specified')
                return 'SCHEDULE_ERROR\n'
            #print(f"stripped time to slot: {stripped}")
            counter_2 = 0
            for x in arr_added:
                #print(f"x is {x}")
                stripped_check = x.split(':')[0]
                if('**' in stripped_check):
                    stripped_check = stripped_check[2:]
                if('-' in stripped_check):
                    stripped_check = stripped_check.split('-')[0]
                stripped_check = int(stripped_check)
                #print(f"stripped time to check: {stripped_check}")
                if(stripped <= stripped_check):
                    #print(f"slotting {stripped} before {stripped_check}")
                    #print(f"index is {counter_2}")
                    add_indexes[counter] = counter_2
                    break
                counter_2 += 1
            counter += 1

        #print(f"length of add_indexes = {add_indexes}")

        str_builder += "\n\n"
        for x in range(len(arr_added)):
            if x in add_indexes:
                for y in range(len(add_indexes)):
                    if add_indexes[y] == x:
                        str_builder += "**" + arr_toAdd[y] + "**\n\n"
            str_builder += arr_added[x] + "\n\n"
    else:
        str_builder += "\n\n"
        for x in arr_added:
            str_builder += x + "\n\n"
    str_builder += "Cadet recall status: **B-24**"

    #### PRINT STR_BUILDER IN NEW WINDOW
    layout = [
    [sg.Text("Markdown POD for: " + values['inp_date'])],
    [sg.Multiline(size=(100,50), key='pod_out', )]
    ]
    print(hasError)
    if(not hasError):
        output_window = sg.Window("Markdown POD", layout, modal=True, finalize=True)
        output_window['pod_out'].update(str_builder)
        while True:
            event, values2 = output_window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
        output_window.close()

def gui():
    global hasError
    sg.theme("DarkBlue12")
    pod_text = ''

    # Date and duty section information
    first_column = [
        [sg.Text('Date - Format like: 01Jan22')],
        [sg.In(size=(25,1), enable_events=True, key='inp_date')],
        [sg.Text('CHDO')],
        [sg.In(size=(25,1), enable_events=True, key='inp_chdo')],
        [sg.Text('RCDO')],
        [sg.In(size=(25,1), enable_events=True, key='inp_rcdo')],
        [sg.Text('ACDO')],
        [sg.In(size=(25,1), enable_events=True, key='inp_acdo')],
        [sg.Text('Duty Section')],
        [sg.In(size=(25,1), enable_events=True, key='inp_dutySection')]
    ]

    second_column = [
        [sg.Text('Select General Schedule:')],
        [sg.Combo(list(dict_schedules.keys()), enable_events=True, key='weekday')],
        [sg.Text('Select Uniform:')],
        [sg.Combo(list(dict_uniforms.keys()), enable_events=True, key='uniform')],
        [sg.Text('Select Cover:')],
        [sg.Combo(list(dict_covers.keys()), enable_events=True, key='cover')],
        [sg.Text('Select jacket:')],
        [sg.Combo(list(dict_jackets.keys()), enable_events=True, key='jacket')]
    ]

    third_column = [
        [sg.Text('Add Event:')],
        [sg.Text('Event Name:')],
        [sg.In(size=(25,1), enable_events=True, key='inp_eventName')],
        [sg.Text('Time:')],
        [sg.In(size=(25,1), enable_events=True, key='inp_eventTime')],
        [sg.Text('Location')],
        [sg.In(size=(25,1), enable_events=True, key='inp_eventLocation')],
        [sg.Text('UOD:')],
        [sg.In(size=(25,1), enable_events=True, key='inp_eventUOD')],
        [sg.Text('Classes:')],
        [sg.Checkbox('2022', default=False, enable_events=True, key='check_2022')],
        [sg.Checkbox('2023', default=False, enable_events=True, key='check_2023')],
        [sg.Checkbox('2024', default=False, enable_events=True, key='check_2024')],
        [sg.Checkbox('2025', default=False, enable_events=True, key='check_2025')],
        [sg.Radio('All Classes', 'class_radio', default=False, enable_events=True, key='check_all')],
        [sg.Button('Add Event', enable_events=True, key='add_event')]
    ]

    layout = [
        [
            sg.Column(first_column),
            sg.VSeperator(),
            sg.Column(second_column),
            sg.VSeperator(),
            sg.Column(third_column)
        ],
        [sg.Text('Special Events - Start with "time:" (ex. "0700: Drill...")')],
        [sg.Multiline(size=(60,10), key='event_box')],
        [sg.Button("Generate Markdown POD")],
        [sg.Text('', enable_events=True, key='error_message')]
    ]

    window = sg.Window('Markdown POD Generator', layout, size=(600,700))

    while True:

        # Pull event data from window
        event, values = window.read()

        # Break loop and close if window closed
        if event == sg.WIN_CLOSED:
            break

        # Debuging output
        # print(f"event: {event}")
        # print(f"values: {values}")

        # Class Button Logic
        if event == 'check_all' and values['check_all'] == True:
            window['check_2022'].update(False)
            window['check_2023'].update(False)
            window['check_2024'].update(False)
            window['check_2025'].update(False)
            #print("all classes checked!")
        if values['check_all'] == True:
            for x in range(2022,2026):
                if event == ('check_' + str(x)) and values['check_' + str(x)] == True:
                    window['check_all'].update(False)

        # Add Event Logic
        if event == 'add_event':
            if(values['inp_eventTime'].isdecimal() and int(values['inp_eventTime']) < 2400 and values['inp_eventName'] != ''):
                str_builder = (values['inp_eventTime'] + ': ')
                for x in range(2022,2026):
                    if values['check_' + str(x)]:
                        str_builder += (str(x) + ' ')
                    # If check all, then it'll just add nothing
                str_builder += (values['inp_eventName'] + ', ' + values['inp_eventLocation'] + ', ' + values['inp_eventUOD'])
                window['event_box'].update(window['event_box'].get() + "\n" + str_builder)
            else:
                window['error_message'].update('Invalid format for event (check all fields)')

        # Make POD
        if event == 'Generate Markdown POD':
            hasError = False
            window['error_message'].update('')
            gen_pod(window, values)

    window.close()

if __name__ == "__main__":
    gui()
