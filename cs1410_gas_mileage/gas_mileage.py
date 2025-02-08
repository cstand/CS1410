import json
import sys


def milesPerGallon(miles, gallons):
    if gallons == 0:
        return 0.0
    else:
        return miles / gallons


def createNotebook(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    if not data:
        return []
    return json.loads(data)


def saveNotebook(notebook):
    file = open("notebook.json", "w")
    file.write(json.dumps(notebook, indent=4))
    file.close()


def recordTrip(notebook, date, miles, gallons):
    trip = {"date": date, "miles": miles, "gallons": gallons}
    notebook.append(trip)
    saveNotebook(notebook)


def listTrips(notebook):
    display = []
    if len(notebook) == 0:
        return []
    for item in notebook:
        display.append(
            f"On {item['date']}: {item['miles']} miles traveled using {item['gallons']} gallons. Gas mileage: {milesPerGallon(item['miles'], item['gallons'])} MPG"
        )
    return display


def calculateMPG(notebook):
    allmiles = 0
    allgall = 0
    if len(notebook) == 0:
        return 0.0
    for item in notebook:
        allmiles += item["miles"]
        if item["gallons"] > 0:
            allgall += item["gallons"]
        else:
            return 0
    return float(allmiles / allgall)


def getUserString(prompt):
    choice = input(prompt).strip()
    while choice == "":
        choice = input(prompt).strip()
    return choice


def getUserFloat(prompt):
    while True:
        try:
            choice = float(input(prompt).strip())
            if choice > 0:
                return choice
            else:
                print("Must be greater than 0.")
        except ValueError:
            print("You can't convert strings to floats.")


def getDate():
    return getUserString("What is the date? ")


def getMiles():
    return getUserFloat("How many miles did you drive since last filling up? ")


def getGallons():
    return getUserFloat("How many gallons of gas did you add to your tank? ")


def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()
    recordTrip(notebook, date, miles, gallons)
    print("Trip recorded and saved!")


def listTripsAction(notebook):
    if len(notebook) == 0:
        print("There are no trips in the notebook.")
    else:
        for item in listTrips(notebook):
            print(item)


def calculateMPGAction(notebook):
    if len(notebook) == 0:
        print("There is no trip data.")
    else:
        print("Average gas mileage: " + str(calculateMPG(notebook)) + " MPG")


def quitAction(notebook):
    print("Bye! See you next time!")
    sys.exit(0)


def applyAction(notebook, choice):
    if choice == "r":
        recordTripAction(notebook)
    elif choice == "l":
        listTripsAction(notebook)
    elif choice == "c":
        calculateMPGAction(notebook)
    elif choice == "q":
        quitAction(notebook)
    else:
        print("Sorry, that option is invalid.")


def formatMenu():
    return [
        "What would you like to do?",
        "[r] Record Gas Consumption",
        "[l] List Mileage History",
        "[c] Calculate Gas Mileage",
        "[q] Quit",
    ]


def formatMenuPrompt():
    return "Enter an option: "


def main():
    notebook = createNotebook("notebook.json")
    while True:
        for item in formatMenu():
            print(item)
        choice = getUserString(formatMenuPrompt())
        applyAction(notebook, choice)


if __name__ == "__main__":
    main()
