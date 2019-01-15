print("Electricity Bill Estimator")

cents = float(input("Enter cents per kWh: "))
while cents <= 0 :
    print ("Error!")
    cents = float(input("Enter cents per kWh: "))

dailyUse = float(input("Enter daily use in kWh: "))
while dailyUse <= 0:
      print ("Error!")
      dailyUse = float(input("Enter daily use in kWh: "))

numOfDay = int(input("Enter number of billing days: "))
while numOfDay <=0:
      print ("Error!")
      numOfDay = int(input("Enter number of billing days: "))

total = (cents/100) * dailyUse *numOfDay

print ("Estimated bill: ${:.2f}".format(total))
print ()

print("Electricity Bill Estimator 2.0 ")

tariff = int(input("Which tariff? 11 or 31: "))
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

while tariff != 11 and tariff != 31:
      print ("Error!")
      tariff = int(input("Which tariff? 11 or 31: "))

if tariff == 11:
       tariff = TARIFF_11
elif tariff == 31:
       tariff = TARIFF_31


dailyUse2 = float(input("Enter daily use in kWh: "))
while dailyUse2 <= 0:
      print ("Error!")
      dailyUse2 = float(input("Enter daily use in kWh: "))

numOfDay2 = int(input("Enter number of billing days: "))
while numOfDay2 <=0:
      print ("Error!")
      numOfDay2 = int(input("Enter number of billing days: "))

total2 = tariff * dailyUse2 * numOfDay2
print ("Estimated bill: ${:.2f}".format(total2))
print ()