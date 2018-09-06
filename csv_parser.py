import csv

html_output=''
names=[]
counter=0
header={}

with open('us-500.csv') as data_file:
    csv_data=csv.DictReader(data_file)
    next(csv_data)
    for line in csv_data:
      counter+=1
      names.append(f"{line['first_name']} {line['last_name']}  {line['address']}")
      if counter>19:
        header=line
        break
         
html_output += f'<p>There are currently {len(names)} in the list. Thank you!!</p>'
html_output += f'\n<ul>'
#html_output+=f'\n\t<li>First Name Last Name  Address</li>'
for name in names:
  html_output += f'\n\t<li>{name}</li>'
html_output += f'\n</ul>'

print(html_output)
