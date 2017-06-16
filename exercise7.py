def total_co2_generated():
  data = ((10, 58.2),(20, 65.2),(30, 67.8), (40, 65.4), (50, 58.8), (60, 49.6), (70, 39.1), (80, 15.8))
  total = 0
  for datum in data:
    total += (datum[1] * 10)
  return total


print (total_co2_generated())
