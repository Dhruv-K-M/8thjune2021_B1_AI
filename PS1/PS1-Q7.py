def check_pangram(arg):
  if len(set('abcdefghijklmnopqrstuvwxyz') - set(arg.lower())) == 0 :
    return True

  return False

user_str = input("Enter a string ")

if(check_pangram(user_str)):
  print("Pangram string")
else:
  print("Not a pangram string")
