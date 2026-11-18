import Functions

Text = Functions.Text
Space = Functions.Space
Clamp = Functions.Clamp
Numerical = Functions.Numerical

Lessons = {
    ("General Knowledge") : {
        ("What is python?") : "Python is a high-level programming language designed to be simple and easy to learn!",
        ("Who created python?") : "Python was created by a dutch software engineer known as Guido van Rossum back in 1991!",
        ("What're the benefits of python over any other language?") : "Python is one of the most used programming languages worldwide and offers both ease of access and readability whilst still being powerful for professional use.",
        ("What can I use to code with python?") : """There's multiple things you can use to start learning python, such as...
            Visual Studio Code,
            Jupyter Notebook
            and PyCharm!
            with the latter being the most beginner friendly!""",
        ("What are Variables?") : f"""
            Variables are what we use to allow us to mention something further down the program, you can give it a name, a number, or anything aslong as:
            Does not have {Text("numbers", "Red") + Text(",\nDoes not have spaces,\n and does not use special characters excluding underscores!", "Green")} 
            
            {Text("Variables can be done like:", "Green")} 
            {Text("IndexApprentice", "Green") + Text(" = ", "Yellow") + Text("\"Sora\"", "Blue")} 
        """,
        ("What are Data Types?"): f"""
            Data types are categories, they're what Variables use to define what type of data they're carrying.
            {Text("int", "Blue") + Text(" are whole numbers,", "Green")} 
            {Text("float", "Green") + Text(" are numbers with decimal placements,", "Green")} 
            {Text("str", "Yellow") + Text(" are text or characters inside quotations,", "Green")} 
            {Text("bool", "Magenta") + Text(" are true or false values.", "Green")} 
            
            {Text("Each data type serve different purposes and can create an error if used wrongly.", "Green")} 
       """,
        ("Arithmetic Operators") : """
            Python has arithmetic operators to allow for mathematics to be done in the program.
            [ + ] ADDITION - Adds two values together.
            [ - ] SUBTRACTION - Subtracts the secondary value from the primary value.
            [ * ] MULTIPLICATION - Multiplies the two values.
            [ / ] DIVISION - Divides the primary value by the secondary value.
            [ // ] FLOOR DIVISION - Similar to division, but it doesn't return any decimals.
            [ % ] MODULUS - Returns the remainder of a division.
            [ ** ] EXPONENTIATION - Raises the first value to the power of the second.
            
            Python follows the PEMDAS rule, meaning Paranthesis goes first, then Exponents, Multiplication and so on.
        """
    },

    ("Basic Fundamentals"): {
        ("Basic Syntax") :
            f"""
            Python is case sensitive, meaning it treats both uppercase and lowercase letters differently. Here's an example.
            Having:
                {Text("name", "Blue") + " = " + Text("ARAYA", "Yellow")}
                {Text("print", "Green") + "(" + Text("name", "Blue") + ")"}
            {Text("is not the same as having:", "Green")}
                {Text("name", "Blue") + " = " + Text("RYOSHU", "Yellow")}
                {Text("print", "Green") + "(" + Text("Name", "Red") + ")"}   
            {Text("Reason? The latter has uppercase letters on the very first letter of the variables mention! Making it wrong.", "Green")}
            """,

        ("Indentation"):
            f"""
            Similar to most programming languages, indentation is important to define each line of code.
            Having:

               {Text("laFamiglia", "Blue") + " = " + Text("Valencina", "Yellow")}
               {Text("if", "Magenta") + Text(" laFamiglia", "Blue") + " == " + Text("Valencina", "Yellow") + ":"}
                    {Text("print", "Green") + "(" + Text("\"I was like you once. Bold… proud… feeling like I could take on the whole City all on my own.\"", "Yellow") + ")"}

            {Text("would be correct, whilst:", "Green")}

               {Text("laFamiglia", "Blue") + " = " + Text("Valencina", "Yellow")}
               {Text("if", "Magenta") + Text(" laFamiglia", "Blue") + " == " + Text("Valencina", "Yellow") + ":"}
               {Text("print", "Green") + "(" + Text("\"I was like you once. Bold… proud… feeling like I could take on the whole City all on my own.\"", "Red") + ")"}

            {Text("would have", "Green") + Text(" errors", "Red") + Text(", due to it not being indented correctly.", "Green")}
            """,

        ("Inputs and Outputs"): {
            ("Description"): f"""
            Outputting is done with the use of the {Text("print", "Blue")} {Text("function, it allows you to send a message directly through the console.", "Green")}
            {Text("print", "Green") + "(" + Text("Test", "Blue") + ")"} 

            {Text("would print:", "Green")}
            {Text("\"If that's what it takes to burn and cut through the Nursefathers…\"", "Gray")}

            {Text("Inputting on the other hand, prints the text and then proceeds to wait for an input from the user.", "Green")}
            {Text("Test", "Yellow") + Text(" = ", "Green") + Text("input", "Magenta") + "(" + Text("\"Then yes, I will gladly become a bottomless pit for you to cast down every ugly secret you would rather forget and never see surfaced again.\"", "Blue") + ")"}
            {Text("print", "Green") + "(" + Text("Test", "Blue") + ")"} 

            {Text("which would output the users input, in this case:", "Green")}
            {Text("\"Then yes, I will gladly become a bottomless pit for you to cast down every ugly secret you would rather forget and never see surfaced again.\"", "Gray")}
            """,

            ("Tutorial"): "Output"
        },

        ("Comments"):
            f"""
                Comments are something that isn't executed, imagine putting a sign next to a door leading where it goes, that's what comments are!
                You can have comments by using hashes:
                {Text("#Let the swarm pullulate. Let the darkest black plague.", "Gray")}
                {Text("print", "Green") + "(" + Text("\"March. March. Consume.\"", "Blue") + ")"}
                {Text("or, if you want multiple lines:", "Green")}
                {Text("""
                      \"\"\"
                      Procreate.
                      Consume.
                      Erase.
                      \"\"\"
                      """, "Gray")}
                {Text("print", "Green") + "(" + Text("\"Erase. Regenerate. March..\"", "Blue") + ")"} 
        """,

        ("Conditional Statements and Logical Operators"): {
            ("Description"):
                f"""
                Conditional Statements are something that makes use of Data Types, they allow you to check if something is a number, a word or a specific combination of characters.
                {Text("Entanglement") + Text(" = ", "Blue") + Text("4", "Magenta")}
                {Text("if", "Yellow") + Text(" Entanglement ") + Text(">=", "Blue") + Text(" 3 ", "Magenta") + ":"}
                  {Text("print", "Green") + "(" + Text("\"The threads of fate are entwined by encounter, and by the length of time surrendered unto another.\"", "Blue") + ")"} 
                {Text("else", "Yellow") + ":"}
                  {Text("print", "Green") + "(" + Text("\"The time that has already been shared cannot be undone.\"", "Red") + ")"} 

                {Text("You can use any mathematical operators such as ==, >=, <=, >, < to check if something is equal to, less than or more than. And you can use != to check if something ISN'T the specified value.", "Green")}

                {Text("Logical operators are: and, or and not", "Green")}
                {Text("The and logical operator helps with checking two or more values are true,", "Green")}
                {Text("The or logical operator checks if at least one of multiple values are true,", "Green")}
                {Text("And the not logical operator checks if the value is false.", "Green")}
        """,
            ("Tutorial"): "Conditional"
        },

        ("Loops and Iterations"): {
            ("Description") :
                f"""
                Loops and iterations are used for repeating a process for a set amount of cycles or till a requirement is met.
                {Text("for", "Blue") + Text(" Rupture ", "Magenta") + Text("in", "Blue") + Text(" range", "Yellow") + "(" + Text("20", "Blue") + ")"}
                    {Text("Convert all", "Green") + Text("Coins", "Yellow") + Text(" into ", "Green") + Text("Unbreakable Coins", "Red")}
                
                {Text("If you want to repeat something until a requirement is met, just use a ", "Green") + Text("while", "Red") + Text(" loop!", "Green")}
                {Text("Loops help make your codes shorter and easier to modify, specially if you need to repeat the same task multiple times.", "Green")}
                """,

            ("Tutorial") : "Loops"
        },
    },

    ("Pseudocoding"): {
        ("Basic Information"): """
        Pseucoding, in its very essence, is the act of mimicking code with simple English statements to plan out the program / allow others with little to no knowledge on programming to read it.
        It's not a requirement, but it's heavily recommended as you won't have to alter your code in the future if you've any planned mechanics to add unto it.
        If you're struggling understanding on how to do it, use a step by step process where you:
        Find the problem,
        Analyze the problem,
        Create the algorithm,
        Write the pseudocode,
        Draw the flowchart (Not required, recommended.)
        Write the program,
        Test and bugfix the program.
        """,

        ("Common Pseudocode Keywords"): f"""
        Pseudocode, since it's a branch from coding has it's own keywords that mimic actual statements from programming.
        {Text("START / END", "Magenta") + Text(" acts as a way to show where the beginning and the end of the code is.", "Green")}
        {Text("DECLARE", "Blue") + Text(" acts as a way to declare a variable and it's data type.", "Green")}
        {Text("=", "Yellow") + Text(" is still similar to it's programming counterpart, assigning values.", "Green")}
        {Text("INPUT", "Cyan") + Text(" is a way to show its accepting inputs from the user, similar to the input function.", "Green")}
        {Text("OUTPUT", "Magenta") + Text(" shows what the user will see in the console.", "Green")}
        {Text("IF / ELSE, WHILE / FOR", "Yellow") + Text(" are still copying the functions of their originals.", "Green")}
        
        {Text("Example:", "Green")}
             {Text("START", "Magenta")}
                {Text("DECLARE Prescripts, Grace, Unlock : INT", "Blue")}
                {Text("INPUT Prescripts", "Cyan")}
                {Text("INPUT Grace", "Cyan")}
                {Text("Unlock = Prescripts * Grace")}
                {Text("OUTPUT", "Magenta") + Text(" \"Heal SP from\"", "Green") + ", " + Text("Unlock", "Blue")}
             {Text("END", "Magenta")}
             
        {Text("Things like mathematical operators, conditional statements and logical operators are still the same in pseudocoding.", "Green")}
        """,

        ("Flowcharts"): f"""
        A flowchart is a diagram representing the sequence of steps or operations to be performed by the program, it's usually created with the use of microsoft word.
        Flowcharts are commonly used to simplify showing the pseudocode as it's easier to read images than it is to read long text.
        """,
    }
}
