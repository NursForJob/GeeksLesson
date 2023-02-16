class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __str__(self):
        return f'Ваш процессор {self.__cpu} а Ваша паменять компьютера {self.__memory} '

    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        return self.__cpu + self.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def __str__(self):
        return f'Ваш список сим карт{self.__sim_cards_list}'

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        return f'Идет звонок на номер {call_to_number} \nc симкарты {sim_card_number} {self.__sim_cards_list[1]} '


class SmartPhone(Computer, Phone):
    def __str__(self):
        return 'Это обект Вашего смартфона'

    def use_gps(self, location):
        return f'Ваша местоположение {location}'


comp = Computer('core i3', '8gb')
print(comp)
ph = Phone(['Beeline', 'Oshka', 'Mega'])
print(ph)
print(ph.call('0500001010', '1'))
print(ph.set_sim_cards_list(['Beeline', 'Mega', 'Oshka']))
sm1 = SmartPhone('core i3', '8gb')
print(sm1)
sm2 = SmartPhone('core i5', '16gb')
print(sm2)
print(sm1.use_gps('Bishkek'))
print(sm2.use_gps('Tokmok'))