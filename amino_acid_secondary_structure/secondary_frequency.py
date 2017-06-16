import csv
import numpy as np
import matplotlib.pyplot as plt

def secondaryStructureFrequency():
  pdbFile = open("2v4j.pdb", mode = "r")
  arrayOfLines = pdbFile.readlines()
  helix = {}
  sheet = {}
  irregular = {}
  result = []
  for line in arrayOfLines:
    if (line[0:5] == "HELIX"):
      helix[line[15:18]] = helix.get(line[15:18], 0) + 1
      helix[line[27:30]] = helix.get(line[27:30], 0) + 1
    elif (line[0:5] == "SHEET"):
      sheet[line[17:20]] = sheet.get(line[15:18], 0) + 1
      sheet[line[28:31]] = sheet.get(line[28:31], 0) + 1
    elif (line[0:6] == "SSBOND"):
      irregular[line[11:14]] = irregular.get(line[11:14], 0) + 1
      irregular[line[25:28]] = irregular.get(line[25:28], 0) + 1
  pdbFile.close()
  for key,value in helix.iteritems():
    aminoAcid = ("Helix", key, value)
    result.append(aminoAcid)
    if (sheet.get(key) == None):
      sheet[key] = 0
    elif (irregular.get(key) == None):
      irregular[key] = 0
  for key,value in sheet.iteritems():
    aminoAcid = ("Sheet", key, value)
    result.append(aminoAcid)
    if (helix.get(key) == None):
      helix[key] = 0
      result.append(("Helix",key, 0))
    elif (irregular.get(key) == None):
      irregular[key] = 0
  for key,value in irregular.iteritems():
    aminoAcid = ("Irregular", key, value)
    result.append(aminoAcid)
  return sorted(result)
secondaryStructureFrequency()

def createCsvFile():
  data = secondaryStructureFrequency()
  with open("secondary_struct.csv", mode = "w") as csvfile:
    csv_out = csv.writer(csvfile)
    csv_out.writerow(['Type','Name','Amount'])
    for row in data:
      csv_out.writerow(row)
createCsvFile()
def createGraph():
  helix_amino_acid_names = []
  helix_amounts = []
  sheet_amino_acid_names = []
  sheet_amounts = []
  irregular_amino_acid_names = []
  irregular_amounts = []
  with open("secondary_struct.csv", mode = "r") as csvfile:
    data = csv.reader(csvfile, delimiter = ",")
    for row in data:
      if (row[0] == "Helix"):
        helix_amino_acid_names.append(row[1])
        helix_amounts.append(row[2])
      elif (row[0] == "Sheet"):
        sheet_amino_acid_names.append(row[1])
        sheet_amounts.append(row[2])
      elif (row[0] == "Irregular"):
        irregular_amino_acid_names.append(row[1])
        irregular_amounts.append(row[2])

  N = len(helix_amounts)
  helix_amino_acids_names = tuple(helix_amino_acid_names)
  helix_amounts = tuple(helix_amounts)

  ind = np.arange(N)
  width = 0.25

  fig,ax = plt.subplots()
  helix_bars = ax.bar(ind,helix_amounts, width, color = 'r')

  sheet_amino_acid_names = tuple(sheet_amino_acid_names)
  sheet_amounts = tuple(sheet_amounts)
  sheet_bars = ax.bar(ind+width,sheet_amounts, width, color = 'b')

  irregular_amino_acid_names = tuple(irregular_amino_acid_names)
  irregular_amounts = tuple(irregular_amounts)
  irregular_bars = ax.bar(ind  + width+width, irregular_amounts, width, color ='y')

  ax.set_ylabel("Amount")
  ax.set_title("Amount of Amino Acids in Secondary Structure of 2v4j")
  ax.set_xticks(ind + width +width / 2)
  ax.set_xticklabels(helix_amino_acids_names)
  ax.legend((helix_bars[0],sheet_bars[0],irregular_bars[0]), ("Helix", "Sheet", "Irregular"))
createGraph()
plt.show()
