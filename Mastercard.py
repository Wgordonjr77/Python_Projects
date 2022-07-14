def isAnagram(s: str, t: str) -> bool:
  dict1= {}
  dict2 ={}
  for letter in s:
    if letter in dict1:
      dict1[letter]+=1
    else:
      dict1[letter]=1

  for letter in t:
    if letter in dict2:
      dict2[letter]+=1
    else:
      dict2[letter]=1
  print(dict1)
  print(dict2)
  print("Are {} and {} Anagrams?".format(s,t))
  return dict1 == dict2

s,t = input("Enter two words").split()
print("s is:", s)
print("t is:", t)
print(isAnagram(s,t))
