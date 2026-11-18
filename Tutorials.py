import time

import Functions

Text = Functions.Text
Space = Functions.Space
Clamp = Functions.Clamp
Numerical = Functions.Numerical

def Output():
    print(f"{Text("Try making code that makes use of both the 'input' and 'output' function!", "Green")}")
    WaitForInput(False, {"input", "output"})

def Conditional():
    print(f"{Text("Try making code that uses an if conditional with an 'and' logical operator!", "Green")}")
    WaitForInput(False, {"if", "and"})

def Loops():
     print(f"{Text("Try making code that has a 'for i' loop!", "Green")}")
     WaitForInput(False, {"for", "in"})

Tutorials = {
    "Output" : Output,
    "Conditional" : Conditional,
    "Loops" : Loops
}

def WaitForInput(Error : bool = False, Keywords : str = {""}):
    print("\n" * 100)
    PrintText = f"{Text("Try entering your code! Type ", "Green") + Text("end", "Yellow") + Text(" to stop!", "Green")}"

    if Error:
        PrintText = f"{Text("Try fixing the ", "Green") + Text("error!", "Red")}"

    ToExecute = ""
    print(PrintText)
    while True:
        Execute = input()
        if Execute.lower() == "end":
            break
        else:
            ToExecute += (Execute + "\n")

    Success = False
    Amount = 0
    for Keyword in Keywords:
        if ToExecute.lower().find(Keyword.lower()):
            Amount += 1

    if Amount >= len(Keywords):
        Success = True

    if not Success:
        print(Text("Your code doesn't seem to be correct.. Try again!", "Green"))
        time.sleep(1)
        WaitForInput(False, Keywords)
    else:
        try:
            print("\n" * 100)
            print(Text("Here's your code running in full view!", "Green"))
            exec(ToExecute)
        except Exception as Error:
            Exec = print(
                f"{Text("An error occurred!", "Red") + Text(" Try and attempt a fix!", "Green")}): {Error}")
            time.sleep(2)
            WaitForInput(True, Keywords)
