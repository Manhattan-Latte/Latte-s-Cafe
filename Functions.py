Colors = {
    ("Black") : "30",
    ("Red") : "91",
    ("Green") : "92",
    ("Yellow") : "93",
    ("Blue") : "94",
    ("Magenta") : "95",
    ("Cyan") : "96",
    ("Gray") : "37",
    ("White") : "0",
}

def Text(Message : str, Color : str = "White", Bold : bool = False):
    Message = (f"\033[{Colors[Color]}m{Message}\033[0m")
    if Bold:
        Message = (f"\033[1;{Colors[Color]}m{Message}\033[0m")

    return Message

def Space(Message : str = "", Spacing : int = 0, Dent : bool = False, ReturnMessage : bool = True):
    Length = len(Message)
    Offset = (" " * (Spacing - Length))

    NewMessage = Offset
    if ReturnMessage:
        NewMessage = Message + Offset

        if Dent:
            NewMessage = Offset + Message

    return NewMessage

def Numerical(Original : str, IntOnly : bool = True):
    if Original == "":
        Original = "999"

    NewMessage = ""
    Float = False

    for Char in Original:
        if Char == "." and not Float:
            Float = True
        elif not Char.isdigit():
            continue

        NewMessage += Char

    if Float and not IntOnly:
        NewMessage = float(NewMessage)
    else:

        NewMessage = int(round(float(NewMessage)))

    return NewMessage

def Clamp(Number : int, Min : int = 0, Max : int = 1):
    if Number < Min:
        Number = Min
    elif Number > Max:
        Number = Max

    return Number
