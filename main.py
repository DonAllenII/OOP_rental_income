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
