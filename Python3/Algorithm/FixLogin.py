''' # # # # FIX LOGIN # # # #'''
import glob

for a in glob.glob("Transformice-0/*.class.asasm"):
  lines = readAsasm(a).split('\n')
  b = 0
  c = 0
  for i, line in enumerate(lines):
    if 'True()' and 'end' and 'Boolean' in line: # Second attempt :)
      n = '"int"'
      b = i
      if n not in lines[i+1] and n in lines[i-1]:
        fixLogin = line.split(' ')
        print(f"test : {lines[275].replace(fixLogin[11:12][0], 'False()')}")
        s = readAsasm(a)
        with open(a, 'w') as f:
          s = s.replace(fixLogin[11:12][0], 'False()')
          f.write(s)
          f.close()
        print(f"P-code : {lines[i]}\n{range(i,len(lines))}\n\n-----------------------")
        break
