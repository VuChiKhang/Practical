# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia", "ACT": "Australian Capital Territory",
               "VIC": "Victoria", "TAS": "Tasmania", "QLD": "Queensland"}
# print(STATE_NAMES)

state = input("Enter short state: ")
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()