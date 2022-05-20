yesNoLogic = "Y = Yes and N = No"
validInput = "Please enter a Valid input"

workingDog = ""
nonWorkingDog= ""
guardDog = ""
supportDog = ""
highEnergyDog= ""
questionThree = ""

name = input("Please enter your name: ")

print (f"Hello {name} We hear you're looking for a new puppy to bring home. We are here to help! Lets get started.")

questionOne = input(f"Will you new dog have a job? {yesNoLogic}: ").lower()

if questionOne == "y":
    workingDog= input("Will it be a Guard Dog, Hearding/Farm dog, or Emotinal Support/Service animal? Enter G = Guard, H = Herd, or S = Service: ").lower()

if questionOne == "n":
    nonWorkingDog = input(f"Will this puppy be in inside dog or have some kind of shelter condusive all weather? {yesNoLogic}: ").lower()

if workingDog == "g":
   guardDog = input("Do you have a size preferance? S = less than 50lbs M= more than 50 less than 100 L=100+ pounds: ").lower()

if workingDog == "h":
    print("German Shepherd Dog or a Belgian Malinois would be a phenominal choice!")

if workingDog == "s":
    supportDog = input("Will this puppy be doing very day task or more for emotional support? E for everyday or ES for emotional support: ").lower()


if nonWorkingDog == "y":
    questionThree = input("which activity excites you more hiking outside or chilling watching tv. H for Hiking T for tv: ").lower()

if nonWorkingDog == "n":
    print(f"{name} Please DO NOT get a dog!")  
      
if guardDog == "s":
    print("Jack Russell Terrier would make a great puppy for you. Small but mighty!")

if guardDog == "m":
    print("Rottweiler or a Doberman Pinscher might be right for you. Very loyal and dont play around about there Hoomans")

if guardDog == "l":
    print("I would highly recommend the Cane Corso. Very large and intimidating. Very loyal and also very loving to the family.")

if supportDog == "e":
    print("I would recommend a Labradors. They are Very intellegent and very easy to train.")

if supportDog == "es":
    print("I would recommend a Golden Retriever. Very affectionate and very keen to the emotions of their Hoomans")

if questionThree == "t":
    print("mhhmm sounds like a bulldog could be a great companion for you!")

if questionThree == "h":
   highEnergyDog = input("I know you said hiking. BUT are you an active active person or just a walk ever other day type of person? A = Active Active or E = every otherday").lower()

if highEnergyDog == "a":
    print("If and ONLY IF you have dog training experience... you should get a Belgian Malinois! If not get a Labrador Retriever. You've been warned! ")

if highEnergyDog == "e":
    print("Dont worry you can still get a great companion. I suggest a very cute Cocker Spaniel to show off on your walking days.")