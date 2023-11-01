from IPython.display import clear_output

#initialize base Value class
class Value():
    def __init__(self, name):
        self.name = name
        self.value = None

#instantiating instances of Value for Income Class
rentalIncome = Value('rental income')
laundryIncome = Value('laundry income')
storageIncome = Value('storage income')
miscIncome = Value('miscellaneous income')

#initialize Income class
class Income():
    def __init__(self, rentalIncome, laundryIncome, storageIncome, miscIncome):
        self.rentalIncome = rentalIncome
        self.laundryIncome = laundryIncome
        self.storageIncome = storageIncome
        self.miscIncome = miscIncome
        self.totaledIncome = 0
        self.incomes = [self.rentalIncome, self.laundryIncome, self.storageIncome, self.miscIncome]
    
    #method for iterating thru assigning values to types of incomes
    def initial(self):
        for i in self.incomes:
            clear_output()
            action = str(input(f'Would you like to input a value for this expense ({i.name})?'))
            if action.lower() == "no":
                continue
            if action.lower() == "yes":
                value = int(input(f'How much in {i.name} for this property?'))
                i.value = value
                print(i.value)

    #write a function to sum all incomes 
    def totalIncome(self):
        for i in self.incomes:
            if isinstance(i.value, int):
                self.totaledIncome += i.value

#instantiating instances of Value for Expenses Class
mortgage = Value('mortgage')
taxes = Value('taxes')
insurance = Value('insurance')
water = Value('water')
garbage = Value('garbage')
electric = Value('electric')
HOA = Value('HOA')
lawnCare = Value('lawn care')
vacancy = Value('vacancy')
repairs = Value('repairs')
capEx = Value('capital expenditures')
propManagement = Value('property management')

#initializing Expenses Class
class Expenses():
    def __init__(self, mortgage, taxes, insurance, water, garbage, electric, HOA, lawnCare, vacancy, repairs, capEx, propManagement):
        self.mortgage = mortgage
        self.taxes = taxes
        self.insurance = insurance
        self.water = water
        self.garbage = garbage
        self.electric = electric
        self.HOA = HOA
        self.lawnCare = lawnCare
        self.vacancy = vacancy
        self.repairs = repairs
        self.capEx = capEx
        self.propManagement = propManagement
        self.totaledExpenses = 0
        self.expenses = [self.mortgage, self.taxes, self.insurance, self.water, self.garbage, self.electric, self.HOA, 
                         self.lawnCare, self.vacancy, self.repairs, self.capEx, self.propManagement]
    

    
    #method for iterating thru assigning values to types of expenses
    def initial(self):
        for i in self.expenses:
            clear_output()
            action = str(input(f'Would you like to input a value for this expense ({i.name})?'))
            if action.lower() == "no":
                continue
            if action.lower() == "yes":
                value = int(input(f'How much in {i.name} for this property?'))
                i.value = value
                print(i.value)

    #method for totaling expenses            
    def totalExpenses(self):
        for i in self.expenses:
            if isinstance(i.value, int):
                self.totaledExpenses += i.value

#initializing Cashflow class
class Cashflow():
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    #method for determining cashflow (income - expeneses)
    def monthlyCashflow(self):
        self.monthlyCash = self.income - self.expenses

    #method for determining annual cashflow
    def annualCashflow(self):
        self.annualCash = self.monthlyCash * 12

#instantiang instances of Value for ROI Class
downpayment = Value('down payment')
closingcosts = Value('closing costs')
rehabBudget = Value('rehab budget')
misc = Value('Miscellenious')

#initialzing the ROI Class
class ROI():
    def __init__(self, downpayment, closingcosts, rehabBudget, misc):
        self.downpayment = downpayment
        self.closingcosts = closingcosts
        self.rehab = rehabBudget
        self.misc = misc
        self.totalinvested = 0
        self.invested = [self.downpayment, self.closingcosts, self.rehab, self.misc]

    def downPayment(self, downpayment):
        self.downpayment = downpayment

    def closingCosts(self, closingcosts):
        self.closingcosts = closingcosts

    def rehabBudget(self, rehabBudget):
        self.rehab = rehabBudget

    def miscCosts(self, misc):
        self.misc = misc

    invested = [downPayment, closingCosts, rehabBudget, miscCosts]

    #method for iterating and assigning values to ROI Class
    def initial(self):
        for i in self.invested:
            clear_output()
            action = str(input(f'Would you like to input a value for this expense ({i.name})?'))
            print(i.name)
            if action.lower() == "no":
                continue
            if action.lower() == "yes":
                value = int(input(f'How much in {i.name} for this property?'))
                i.value = value
                print(i.value)

    #method for adding up total investment in ROI Class
    def totalInvestment(self):
        for i in self.invested:
            if i.value != None:
                self.totalinvested += i.value

    #method for determining cash on cash ROI
    def roi(self, aCashflow):
        self.roi = aCashflow / self.totalinvested


#initializing the Handler Class
class Handler():
    def __init__(self):
        pass

    #method for running the rental income program
    def run(self):
        while True:
            action = str(input("What would you like to do?\n Press 'F' to fill out sections\n Press 'S' for stats & information\n Press 'Q' to quit program"))
            if action.lower() == "f":
                action = str(input("Which section would you like fill out?\n Press 'I' for Income\n Press 'E' for Expenses\n Press 'C' for Cashflow\n Press 'R' for ROI(Return on Investment) "))
                if action.lower() == "i":
                    income.initial()
                    income.totalIncome()
                    print(income.totaledIncome)
                
                if action.lower() == "e":
                    expenses.initial()
                    expenses.totalExpenses()
                    clear_output()
                    print(f'Total expenses are ${expenses.totaledExpenses}.')
                    print(f'Total income is ${income.totaledIncome}.')
                if action.lower() == "c":
                    if income.totaledIncome == 0:
                        print(f'Please update income to reflect a more accurate cashflow.')
                    if expenses.totaledExpenses == 0:
                        print(f'Please update expenses to reflect a more accurate cashflow.')
                    cashflow = Cashflow(income.totaledIncome, expenses.totaledExpenses)
                    cashflow.monthlyCashflow()
                    cashflow.annualCashflow()
                    print(f'The monthly cashflow for this property is ${cashflow.monthlyCash}.')
                    print(f'The annual cashflow for this property is ${cashflow.annualCash}.')
                if action.lower() == "r":
                    roi.initial()
                    roi.totalInvestment()
                    print(f'The total invested in this property is ${roi.totalinvested}.')
            if action.lower() == "s":
                action = str(input("Which info would you like?\n Press 'M' for income\n Press 'E'  for expenses\n Press 'C'  for cashflow\n Press 'R' for Cash on Cash ROI"))
                if action.lower() == 'm':
                    print(f'Total income for this property is ${income.totaledIncome}.')
                if action.lower() == 'e':
                    print(f'Total expenses for this property are ${expense.totaledExpenses}')
                if action.lower() == 'c':
                    if income.totaledIncome == 0:
                        print(f'Please update income to reflect a more accurate cashflow.')
                    if expenses.totaledExpenses == 0:
                        print(f'Please update expenses to reflect a more accurate cashflow.')
                    cashflow = Cashflow(income.totaledIncome, expenses.totaledExpenses)
                    cashflow.monthlyCashflow()
                    cashflow.annualCashflow()
                    print(f'The monthly cashflow for this property is ${cashflow.monthlyCash}.')
                    print(f'The annual cashflow for this property is ${cashflow.annualCash}.')
                if action.lower() == 'r':
                    print(f'The total investment in this property is ${roi.totalinvested}')
                    print(f'The cash on cash ROI for this property is {roi.roi}')
            if action.lower() == "q":
                break
                
            
                

#instantiating an instance of the Income class
income = Income(rentalIncome, laundryIncome, storageIncome, miscIncome)
#instatiating an instance of the Expenses class
expenses = Expenses(mortgage, taxes, insurance, water, garbage, electric, HOA, lawnCare, vacancy, repairs, capEx, propManagement)
#instantiating an instance of the ROI class
roi = ROI(downpayment, closingcosts, rehabBudget, misc)

#instantiating an instance of the Handler class, use run method
handle = Handler()
handle.run()