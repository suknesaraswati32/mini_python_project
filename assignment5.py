# with open("name.txt","w")as f:
#   n1=input("enter name:")
#   n2=input("enter name:")
#   f.write(f"{n1}\n{n2}")
  
# with open("name.txt","r")as f:
#   data=f.read()
#   print(data)

# with open("log.txt","a") as f:
#   log=input("enter log:")
#   f.write(f"{log}\n")

# li=[5,10,15,20,25]

# li=[val for val in li if val>15]
# print(li)
# import json
# li={
#   'delhi':300000,
#   'mumbai':3500000,
#   'kolkata':2500000,
# }
# city=input("enter city name:")
# population=input("enter population:")
# li[city]=population
  
# with open("city.txt","w") as f:
#   data=json.dumps(li)
#   f.write(data)
  
# with open("city.txt","r") as f:
#   data=f.read()
#   data=json.loads(data)
#   print(data)
# try:    
#   with open("data.txt","r")as f:
#     data=f.read()
#     print(data)
# except FileNotFoundError:
#   print("file not found")  