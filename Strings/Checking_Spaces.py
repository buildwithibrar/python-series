sentence = input("Enter a sentence with spaces.")  

user_Sentence = sentence                    #Spaces Sentence.
print("Original:",user_Sentence)

remove_Spaces = user_Sentence.strip()       #Remove Spaces.
print("Strip:", remove_Spaces)

left_Strip = user_Sentence.lstrip()         #Remove Left Spaces.
print("Left Strip:", left_Strip)

right_Strip = user_Sentence.rstrip()        #Remove Right Spaces.
print("Right Strip:", right_Strip)

# ask the user for another sentence and determine 
# whether it starts or ends with spaces.

user_input = input("Enter your sentence.")

check_Start = user_input.startswith("Hello")
print("Starts with Hello.", check_Start)

check_End = user_input.endswith(".")
print("Ends with Dot.", check_End)
