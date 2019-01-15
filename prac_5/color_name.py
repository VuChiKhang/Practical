color_name = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite4": "#8b8378", "azure1": "#f0ffff",
              "BlueViolet": "#8a2be2", "brown4": "#8b2323", "CadetBlue1": "#98f5ff", "chartreuse1": "#7fff00",
              "coral": "#ff7f50"}

color= input("Enter the color name: ")
while color!="":
    if color in color_name:
        print("The code for \"{}\" is {}".format(color, color_name.get(color)))
    else:
        print("Invalid color")
    color = input("Enter the color name: ")

