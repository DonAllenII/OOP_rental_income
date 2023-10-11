from IPython.display import clear_output


class Value():
    def __init__(self, name):
        self.name = name
        self.value = None

rentalIncome = Value('rental income')
laundryIncome = Value('laundry income')
storageIncome = Value('storage income')
miscIncome = Value('miscellaneous income')


class Income():
    def __init__(self, rentalIncome, laundryIncome, storageIncome, miscIncome):
        self.rentalIncome = rentalIncome
        self.laundryIncome = laundryIncome
        self.storageIncome = storageIncome
        self.miscIncome = miscIncome
        self.totaledIncome = 0
        self.incomes = [self.rentalIncome, self.laundryIncome, self.storageIncome, self.miscIncome]
    

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
                
    def totalExpenses(self):
        for i in self.expenses:
            if isinstance(i.value, int):
                self.totaledExpenses += i.value


class Cashflow():
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses


    def monthlyCashflow(self):
        self.monthlyCash = self.income - self.expenses

    def annualCashflow(self):
        self.annualCash = self.monthlyCash * 12

downpayment = Value('down payment')
closingcosts = Value('closing costs')
rehabBudget = Value('rehab budget')
misc = Value('Miscellenious')

class ROI():
    def __init__(self, downpayment, closingcosts, rehabBudget, misc):
        self.downpayment = downpayment
        self.closingcosts = closingclosts
        self.rehab = rehabBudget
        self.misc = misc
        self.invested = [self.downPayment, self.closingcosts, self.rehabBudget, self.misc]

    def downPayment(self, downpayment):
        self.downpayment = downpayment

    def closingCosts(self, closingcosts):
        self.closingcosts = closingcosts

    def rehabBudget(self, rehabBudget):
        self.rehab = rehabBudget

    def miscCosts(self, misc):
        self.misc = misc

    invested = [downPayment, closingCosts, rehabBudget, miscCosts]

    def initial(self):
        for i in self.invested:
            clear_output()
            action = str(input(f'Would you like to input a value for this expense ({i.name})?'))
            if action.lower() == "no":
                continue
            if action.lower() == "yes":
                value = int(input(f'How much in {i.name} for this property?'))
                i.value = value
                print(i.value)

    def totalInvestment(self):
        for i in invested:
            if i != None:
                self.totalinvested += self.i


class Handler():
    def __init__(self):
        pass


    def run(self):
        while True:
            action = str(input("What would you like to do?\n Press 'n' for new\n Press 'i' for individual\n "))
            if action.lower() == "n":
                income.initial()
                income.totalIncome()
                print(income.totaledIncome)
                expenses.initial()
                expenses.totalExpenses()
                clear_output()
                print(expenses.totaledExpenses)
                print(income.totaledIncome)
                cashflow = Cashflow(income.totaledIncome, expenses.totaledExpenses)
                cashflow.monthlyCashflow()
                cashflow.annualCashflow()
                print(f'The monthly cashflow for this property is ${cashflow.monthlyCash}.')
                print(f'The annual cashflow for this property is ${cashflow.annualCash}.')
                roi.initial()
                roi.totalInvestment()
                
            
                
            break

income = Income(rentalIncome, laundryIncome, storageIncome, miscIncome)
expenses = Expenses(mortgage, taxes, insurance, water, garbage, electric, HOA, lawnCare, vacancy, repairs, capEx, propManagement)
roi = ROI(downpayment, closingcosts, rehabBudget, misc)
handle = Handler()
handle.run()