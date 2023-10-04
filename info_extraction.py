import webbrowser
import requests
#search_key="Hrithik_Roshan"
search_key=input("enter the celebrity name :")
temp_list=search_key.split()
temp_list=[i.capitalize() for i in temp_list]
search_key="_".join(temp_list)
search_url = f"https://en.wikipedia.org/wiki/{search_key}"
response=requests.get(search_url)
Text=response.text
#print(Text)
import re
age_actress=re.findall(r"\(age&#160;(\d+)",Text)
print(f"{search_key} age is : {age_actress}")

#for i in _actress:
#   print(i)