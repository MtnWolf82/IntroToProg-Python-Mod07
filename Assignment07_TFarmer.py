# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling to store more complex data in a
#              binary file.
#              Creating custom exception messages to inform the user of
#              input errors within the program, and provide guidance for
#              resolution of the errors.
# ChangeLog (Who,When,What):
# TFarmer, 2.27.22, Created initial script for assignment 07
# TFarmer, 2.28.22, Revised script for assignment 07
# TFarmer, 3.1.22, Finished script for assignment 07
# ---------------------------------------------------------------------------- #
# Demonstrate pickling data

# Import applicable modules
import pickle

# Creating lists of data to be pickled
print("<<< Pickling lists by discipline and type >>>")
discipline = ["Cross Country", "Enduro", "Downhill"]
type = ["Rigid", "Hardtail", "Full Suspension"]

# Pickling list data into a binary file
file = open("pickledbikes.txt", "wb")
pickle.dump(discipline, file)
pickle.dump(type, file)
file.close()
print("\nOur data has been pickled into a binary file! Feel free"
      "\nto take a look at the 'pickledbikes.txt' file to verify.")
input("Press Enter to continue and unpickle our list data.")

# Unpickling list data from our binary file
print("\n<<< Unpickling our lists of bike data >>>")
file = open("pickledbikes.txt", "rb")
discipline = pickle.load(file)
type = pickle.load(file)
print("\nList data has been unpickled!")
input("Press the Enter key to continue and print our list data.")

# Displaying our unpickled list data
print("\nThe unpickled list data can be seen below.")
print(discipline)
print(type)
file.close()
print("\nThat concludes our pickling of data.")
input("Press the Enter key to continue on to exception handling.")

# Demonstrate exception handling
print("\nPick a number between 1 and 10.")
try:
    num = float(input("\nEnter your number: "))
    if num in range(0,10):
        print("Your number is",num)
    else:
        print(num,"is not a valid entry.")
except ValueError:
    print("\nThat was not a number!")

input("\nPress the Enter key to exit.")