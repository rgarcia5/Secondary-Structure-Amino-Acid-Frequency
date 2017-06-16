import re
def huntingtonCheck():
  sequenceArray = open("huntingtin.txt", mode = "r").read().splitlines()
  sequenceString = "".join(sequenceArray)
  s = re.compile('(CA[AG]){35,}')
  return len(s.findall(sequenceString))


print (huntingtonCheck())
