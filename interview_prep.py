# ------------------------------------------------
# -----------------Understanding------------------
# ------------------------------------------------

# Given a dictionary with both strings and numbers for either keys and values,
# we want to print the sume of all values that are numbers

# ------------------------------------------------
# --------------------Planning--------------------
# ------------------------------------------------

# Loop through the dictionary, printing all values from their key pairs
  # If the value is a number, add them together

# ------------------------------------------------
# ------------------Execution---------------------
# ------------------------------------------------

dict = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

def sumdict(dictionary):
  newArray = []
  for i in dictionary.values():
    # print(i)
    if type(i) == int:
      newArray.append(i)
      print(newArray)
  return sum(newArray)


print(sumdict(dict))