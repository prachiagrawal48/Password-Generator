import random
import string

def generate_password(length):
    #1.Define the sets of characters to use

    # string.ascii_letters includes:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    # string.digits includes: 0123456789
    # string.punctuation includes: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    #Combine all characters types for complexity
    all_characters = string.ascii_letters + string.digits + string.punctuation

    #Check if the desired length is valid 
    if length <= 0:
     return "Error: Password length must be a positive number."
    
    #2. Ensure atleast one of each type is included for strength
    #this guarantees the password meets a minimum complexity standard.
    if length < 4:
       #if length is too short, we can't guarantee all types, so we simplify the requirement.
       #However, for robustness, we'll try to include as many types as possible.
       pass #Will proceed to random choice

    # Start with a minimum set of characters (one of each type)
    #This helps ensure the pasword is complex and not just all lowercase letters, for example.

    # Initialize the password list 
    password = []

    # Ensure atleast one character of each type if the length permits
    # For a truly strong password , we enforce this (it requires length >= 4)
    if length >= 4:
      password.append(random.choice(string.ascii_lowercase)) # must have lowercase
      password.append(random.choice(string.ascii_uppercase)) # must have uppercase
      password.append(random.choice(string.digits)) # must have a number
      password.append(random.choice(string.punctuation)) # must have a symbol

      # Calculate how many characters are left to generate randomly
      remaining_length = length - 4

    else:
       #If length < 4, we use the whole length for purely random choices
      remaining_length = length

#3. Fill the rest of the password length with random choices
    for _ in range(remaining_length):
     password.append(random.choice(all_characters))

#4. Shuffle the list to randomize the position of the enforced characters

#This prevents the password from always starting with the same four types.
     random.shuffle(password)

#5. Convert the list of characters back into a single string
    return "".join(password)


#----Main Execution----
try:
   #User Input: Prompt the user to specify the desired length
   print("Welcome to the Python Password Generator!")

   #Get input and convert it to an integer
   #We use a loop and try/except to handle non-integer input gracefully
   while True:
        try:
          length_input = input("Enter the desired length of the password(e.g., 12):")
          password_length = int(length_input)

          if password_length <= 0:
               print("Please enter a positive length.")
               continue #Ask again
          break 
        #Exit loop if input is valid
        except ValueError:
          print("Invalid input. Please enter a whole number.")

    #Generate Password: Call the function 
   generated_pass = generate_password(password_length)
    #Display the password: Print the result
   print("\n---")
   print(f"Generated Password (Length:{password_length}): *{generated_pass}*")
   print("---")

except Exception as e:
   #Catch any unepected errors
   print(f"An unexpected error occurred: {e}")
