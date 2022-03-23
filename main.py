#This python file calculates all the possible rolls and decimal probabilities of each roll of 3 six sided dice.
#Could easily be expanded to higher numbers of dice using additional for loops.
#It works by creating a library, which has indices created via the possible values of x,y, and z (x+y+z), which stand for the rolls of 3 6 sided dice. 
#E.G. if you rolled a 2, a 3, and a 5, you would have the key: 10. and the number in the indices 10 of the rolls library is incremented by one. -> rolls_library[key] += 1
#After these values are calculated. You have a dictionary, where the only indices created are ones that are valid dice rolls.
#this then prints using f"...{code goes here}" which I'm still not 100% sure how it works, but I got it working well enough

#Initalizes the rolls dictionary. I'm not 100% sure why it is a dictionary, but the initial build idea from examples used a doctionary so... I think it is because I wanted a data type that could have indices in different value positions, and not just a list containing values with a cardinal set of indices.
rolls_library = {}
#Initializes the keys list, which will be used to track all of the various keys 
keys = []

# Initializes rolls_library key positions. 
# Without this KeyError was thrown 
# There is probably a better way to initializes these so an extra 3 loops aren't needed.
for x in range(1,7):
  for y in range(1,7):
    for z in range(1,7):
      # -- testing command --
      # print(str(x+y+z))
      
      # temp key assignment
      key = x+y+z
      # rolls library indices initialization
      rolls_library[key] = 0

# Increment indices for every time a combination of rolls hits.
for x in range(1,7):
  for y in range(1,7):
    for z in range(1,7):
      # Temporary key assingment
      key = x+y+z
      # key is appended to the keys list.
      # this is apparently a 'pythonic' way of making sure only unique values are added to a list
      keys.append(key) if key not in keys else keys
      # increments the key indices by 1
      rolls_library[key] += 1
      # -- testing command --
      # print(str(key) + " value at "+str(rolls_library[key]))

# Initializes the sum variable
sum = 0
# Prints a new line for every value in keys. (every key in keys) as well as the ultimate probability that you will roll that if you roll 3d6. This uses f"...{code goes here}...", which is some aspect of how print behaves, though I am not 100% sure on the specifics. It did fix an error that I was having however. 
for i in keys:
  print(f"Value {str(i)} has a probability of" + f"  {str(rolls_library[i])}/216. That is a decimal value of " + f"{str(round((rolls_library[i]/216), 5))}")


# Sites used after I googled a solution for whichever bug / logic problem I was thinking through while coding this. 

# The book on canvas. Specifically todays parts 1 and 3, with included deepnotes.
# Dynamic creation of variable names. -> Google search that lead me to discovering the dictionary
# https://stackoverflow.com/questions/5036700/how-can-you-dynamically-create-variables
# Returning specific amounts of decimals from a float
# https://www.codegrepper.com/code-examples/python/how+to+return+a+float+with+2+decimal+places+in+python
# Formatting using f"...{}..."
# link lost use google
# appending to a list only unique values 
# https://stackoverflow.com/questions/17370984/appending-an-id-to-a-list-if-not-already-present-in-a-string 
# Collections within a library
# https://docs.python.org/3/library/collections.html
# Collections datatype examples
# https://docs.python.org/3/library/collections.html
# Python KeyError
#https://realpython.com/python-keyerror/
# The need to be 100% sure your math is right.
# https://www.thoughtco.com/probabilities-for-rolling-three-dice-3126558#:~:text=Possible%20Outcomes%20and%20Sums,there%20are%206n%20outcomes.
# You REALLY gotta double check your math is right. 
# https://www.google.com/search?q=1%2F216&sourceid=chrome&ie=UTF-8