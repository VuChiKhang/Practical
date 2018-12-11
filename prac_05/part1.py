COLOUR_NAMES = {"#faebd7": "AntiqueWhite", "#f0f8ff": "AliceBlue", "#7fffd4": "aquamarine1", "#838b8b": "azure4",
               "#f5f5dc": "beige", "#000000": "black", "#8a2be2": "BlueViolet", "	#5f9ea0": "CadetBlue",
               "#d2691e": "chocolate", "#ffb6c1": "LightPink"}
# print(COLOUR_NAMES)

colour = input("Enter colour code: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour code")
    colour = input("Enter colour code: ")