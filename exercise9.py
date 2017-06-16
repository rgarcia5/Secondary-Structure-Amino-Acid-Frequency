class AminoAcid:

  molarMass = 0
  isoelectricPoint = 0
  name = ""
  def setName(self,newName):
    self.name = newName
  def setMolarMass(self,newMolarMass):
    self.molarMass = newMolarMass
  def setIsoelectricPoint(self,newIsoelectricPoint):
    self.isoelectricPoint = newIsoelectricPoint

lysine = AminoAcid()
lysine.setName("Lysine")
lysine.setMolarMass(100.52)
lysine.setIsoelectricPoint(-5)

print(lysine.name)
print(lysine.isoelectricPoint)
print(lysine.molarMass)
