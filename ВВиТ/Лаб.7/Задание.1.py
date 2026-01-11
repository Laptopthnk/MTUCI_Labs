class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_info(self):
        return f'{self.name}, {self.id}'
    
class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def get_info(self):
        return f'{super().get_info}, {self.department}'
    
    def manage_project(self):
        print('Управляет проектами')

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def get_info(self):
        return f'{super().get_info}, {self.specialization}'
    
    def perform_maintenance(self):
        print('Выполняет техническое обслуживание')

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def get_info(self):
        return f'{Employee.get_info(self)}'
    
    def manage_project(self):
        print('Управляет проектами')

    def perform_maintenance(self):
        print('Выполняет техническое обслуживание')

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return f'{self.team}'

emp = Employee('Джон', 'RT5324')
man = Manager('Эдвард', 'UI8347', 'IT-отдел')
tech = Technician('Стив', 'PL8439', 'QA-инженер')
TM = TechManager('Демогоргон', 'NB0920', 'Кибербезопасность', 'Инженер по безопасности')

print(emp.get_info())
print(man.manage_project())
print(tech.perform_maintenance())
print(TM.get_info())
TM.add_employee(man)
TM.add_employee(tech)
print(TM.get_team_info())
