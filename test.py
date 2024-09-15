class Phone:
    def __init__(self, serial, year, cost):
        self.serial = serial
        self.year = year
        self.cost = cost

    def rate_phone(self):
        if self.year <= 1:
            res1 = f'Ваш {self.serial} пока что считается новым'
        elif 1 < self.year < 3:
            res1 = f'Ваш {self.serial} уже не новый'
        else:
            res1 = f'Ваш {self.serial} уже старый'
        if self.cost >= 85000:
            res2 = 'и стоил дорого'
        elif 85000 > self.cost >= 50000:
            res2 = ' и по стоимости входил в средний ценовой сегмент'
        else:
            res2 = ' и стоил относительно дешево'
        return res1 + res2

model = input('Введите модель айфона: ')
years_using = float(input('Введите срок использования(в годах): '))
cost = int(input('Введите цену: '))

phone = Phone(model, years_using, cost)
res = phone.rate_phone()
print(res)
