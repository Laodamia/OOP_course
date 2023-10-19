class Bill:
    """
    Object that has data about the bill,
    e.g. amount, period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    create a person who lives in the flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    create pdf report with data about: flatmates, amount, period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


bill = Bill(amount=20, period="March 2021")
print(bill)
j = Flatmate("John", 30)
m = Flatmate("Mary", 25)

print(j.pays(bill))