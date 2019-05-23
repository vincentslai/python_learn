#Calling another .py in the same directory using from 
print("Calling a function from different .py file")
from mymodule import my_func

my_func()

print("")
print("Calling a function/module from inside a main folder and sub folder inside the main folder")
from MainFolder import main
from MainFolder.SubFolder import sub

main.main_report()
sub.sub_report()



