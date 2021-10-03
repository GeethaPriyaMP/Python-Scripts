# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
pyarray = [1,2,3,"ello","Krishna"]
pydict = {"India":"Delhi","Srilanka":"Colombo","China":"Beijing"}

print(pyarray[2])
print(pyarray[4])

print("Capital of India is:",pydict["India"])
print("Capital of Srilanka is:",pydict["Srilanka"])

print(pydict.keys())

for item in pyarray:
    print(item)
    
for key in pydict.keys():
    print(key,'-',pydict[key])
 