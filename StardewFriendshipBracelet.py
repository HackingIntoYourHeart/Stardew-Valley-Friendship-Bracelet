import os
import xml.etree.ElementTree as ET

os.chdir(r"C:\Users\\" + os.getlogin() + "\AppData\Roaming\StardewValley\Saves")

def getChildrenByTitle(node, name):
	for child in node.childNodes:
		if child.localName==name:
			yield child

farms = []
for FILE in os.listdir():
	if os.path.isdir(FILE):
		farms.append(FILE)

saveFolder = ""
if len(farms) > 1:
	counter = 0
	for farm in farms:
		print(str(counter) + ": " + farm.split('_')[0])
		counter += 1
	saveFolder = int(input("Which farm? (Enter the number!): "))
else:
	try:
		saveFolder = farms[0]
	except:
		print("Error: Failed to find a farm!")
		input()
		exit()
os.chdir(saveFolder)

root = ET.parse(saveFolder)

userIDs = []
farmhands = root.findall("farmhands")
for farmhand in farmhands:
	#print(farmhand)
	farmers = farmhand.findall("Farmer")
	for farmer in farmers:
		print("Fixing farmer:", farmer.find("name").text)
		userIDs.append(farmer.find("userID").text)

with open(saveFolder, 'r') as file:
	saveData = file.read()

for userID in userIDs:
	try:
		saveData = saveData.replace(userID, '')
		print("Friendship bracelet granted!!!")
	except:
		print("Fix already applied...")

with open(saveFolder, 'w') as file:
	file.write(saveData)

print("Done :)")
input()
exit()
