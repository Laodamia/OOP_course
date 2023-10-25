from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

# get the user to give us the variables
amount = float(input("Hey user, enter the bill amount: "))
period = input("What's the period we're talking about (ideal format: Month YYYY): ")
name1 = input("What's your name? ")
days1 = int(input(f"How many days did {name1} spend in the house? "))
name2 = input("What's your flatmate's name? ")
days2 = int(input(f"How many days did {name2} spend in the house? "))

bill = Bill(amount, period)
flatmate_1 = Flatmate(name=name1, days_in_house=days1)
flatmate_2 = Flatmate(name= name2, days_in_house=days2)

#print results
print(f"{flatmate_1.name} pays:", round(flatmate_1.pays(bill, flatmate_2),2))
print(f"{flatmate_2.name} pays:", round(flatmate_2.pays(bill, flatmate_1),2))

# output the report
pdf_report = PdfReport(filename=f"{bill.period}.pdf")
pdf_report.generate(flatmate_1, flatmate_2, bill)

file_sharer = FileSharer(filepath=f"Files/{pdf_report.filename}")
print(file_sharer.share())