filename = input("File name:")
f = open(filename, "r")
wt = f.readlines()
f.close()
g = open("html.html","w")

for i in wt:
  if i.startswith("="*5) and i.endswith("="*5):
    h_level = int(i.count("=")/2)
  elif i.startswith("="*4) and i.endswith("="*4):
      
