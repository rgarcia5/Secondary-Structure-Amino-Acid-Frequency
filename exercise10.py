readFile = open("P46013.fasta.txt", mode = "r")
listOfLines  = readFile.readlines()
aminoAcidFrequency = {}
for line in listOfLines:
  if (line[0] == ">"):
    continue
  else:
    i = 0
    while (i < len(line) - 1):
      if (line[i] == "P"):
        j = i + 1
        while (j < len(line)):
          if (line[j] == "P" or line[j] == "\n"):
            break
          else:
            aminoAcidFrequency[line[j]] = aminoAcidFrequency.get(line[j],0) + 1
          j += 1
      i += 1
readFile.close()
print (aminoAcidFrequency)
