"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
STATE_NAMES_LOWER = {"qld": "Queensland", "nsw": "New South Wales", "nt": "Northern Territory", "wa": "Western Australia",
               "act": "Australian Capital Territory", "vic": "Victoria", "tas": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ")
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    elif state in STATE_NAMES_LOWER:
        print(state, "is", STATE_NAMES_LOWER[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")
