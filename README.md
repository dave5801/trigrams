# Trigrams

This module takes a text document and creates a dictionary out of three word patterns contained in it. This dictionary is then used to generate new text. 

At the command line, enter: 

> python trigrams.py {file} {number} 

where file is the path to the text document to pass into the module and number is how many words in the generated text. The module will print the results to the console. For example, using a text file, wish.txt containing the text "I wish I may I wish I might" the module would create a dictionary: 

> {"i wish" : ["i", "i"],
> "wish i" : ["may", "might"],
> "i may" : ["i"],
> "may i" : ["wish"]}

Typing 

> python trigrams.py wish.txt 10

into the console will print something like 

> may i wish i may i might wish i may

Authors:
David Franklin
Allan Liebold
