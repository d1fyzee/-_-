class Computer:
    def __init__(self, cpu, cores, ram, hdd):
        self.cpu = cpu
        self.cores = cores
        self.ram = ram
        self.hdd = hdd

    def cost(self):
        return (self.cpu * self.cores / 100) + (self.ram / 80) + (self.hdd / 20)

    def is_suitable(self):
        if self.cpu >= 2000 and self.cores >= 2 and self.ram >= 2048 and self.hdd >= 320:
            return True
        else:
            return False

    def info(self):
        return (f"Компьютер: Процессор {self.cpu} МГц, Ядер {self.cores}, "
                f"ОЗУ {self.ram} МБ, Диск {self.hdd} ГБ. "
                f"Стоимость: {self.cost()} у.е., Подходит: {self.is_suitable()}")


class Laptop(Computer):
    def __init__(self, cpu, cores, ram, hdd, battery):
        super().__init__(cpu, cores, ram, hdd)
        self.battery = battery

    # Переопределяем метод: Стоимость
    def cost(self):
        base_cost = super().cost()
        return base_cost + (self.battery / 10)

    # Переопределяем метод: Пригодность
    def is_suitable(self):
        base_suitable = super().is_suitable()
        if base_suitable == True and self.battery >= 60:
            return True
        else:
            return False

    # Переопределяем информацию, чтобы было слово "Ноутбук"
    def info(self):
        return (f"Ноутбук: Процессор {self.cpu} МГц, Ядер {self.cores}, "
                f"ОЗУ {self.ram} МБ, Диск {self.hdd} ГБ, Батарея: {self.battery} мин. "
                f"Стоимость: {self.cost()} у.е., Подходит: {self.is_suitable()}")



my_pc = Computer(cpu=3000, cores=4, ram=8192, hdd=1000)
my_laptop = Laptop(cpu=1500, cores=2, ram=4096, hdd=500, battery=120)

print(my_pc.info())
print(my_laptop.info())