import subprocess

numbers = []

for i in range(5):
   numbers.append(input(""))

command_result = subprocess.run(['termux-clipboard-get'], stdout=subprocess.PIPE) 
x = command_result.stdout.decode('utf-8')

for i in numbers:
    print(str(i)+" : "+x[int(i)-1])
    
subprocess.run(['termux-clipboard-set',"nope"], stdout=subprocess.PIPE) 

