import csv

#fiels names
fields=['emp_name','emp_id','emp_add']

#data rows of csv file
rows=[['Sonali','1','Mumbai'],
      ['GDTC','2','Parel']

]

with open('employee.csv', 'w', newline='') as csvfile:
    empwriter = csv.writer(csvfile)

    empwriter.writerow(fields)

    empwriter.writerow(rows)


