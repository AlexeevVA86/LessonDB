class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surnaname = surname
        self.position = position
        self._income = {
            'wage': int(wage),
            'bonus': int(bonus)
        }


class Position(Worker):

    def get_full_name(self, name, surname):
        return print(f'Полное имя сотрудника: {name + " " + surname} ')

    def get_total_income(self, wage, bonus):
        total_income = wage + bonus
        return print(f'Зароботная плата сотрудника: {total_income}')


MDE = Position('Радмир', 'Абдрахманов', 'Middle Data Engineer', 100000, 50000)
print(f'Имя сотрудника: {MDE.name}\n'
      f'Фамилия сотрудника:{MDE.surnaname}\n'
      f'Должноcть: {MDE.position}\n'
      f'Оклад сотрудника: {MDE._income["wage"]}\n'
      f'Премия сотрудника: {MDE._income["bonus"]}\n')


MDE.get_total_income(MDE._income.get("wage"), MDE._income.get("bonus"))
MDE.get_full_name(MDE.name, MDE.surnaname)
