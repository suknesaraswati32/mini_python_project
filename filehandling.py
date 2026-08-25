with open('text.txt','r') as f:
  text=f.read()
list=text.split()
count=0
freq={}
for word in list:
  if word not in freq:
    freq[word]=1
  else:
    freq[word]+=1
      
  count=count+1
print(freq)  
print(count)
for key,val in freq.items():
  if(val>=1):
    print(key,":",val)
  
queryt=0 
with open ('sara.txt','a+') as f:
   f.write('Highlight (or mark) all occurrences of the query in the text by surrounding them with ** or another marker of your choice.')
   query=input("enter your query")
   f.seek(0)
   text=f.read()
if query in text:
   queryt=queryt+1
   query="**"
print(queryt)  
print(text) 

