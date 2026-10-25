class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.name = name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount
    def calculate_bill(self):
        print(f"Patient Name: {self.get_name()}")
        print(f"Original Bill: ₱{self.get_bill_amount()}")
        print(f"Final Bill: ₱{self.get_bill_amount()}")
        
class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        bill_amount = self.get_bill_amount()
        final_bill = bill_amount - (bill_amount*0.2)
        print(f"Patient Name: {self.get_name()}")
        print(f"Original Bill: ₱{self.get_bill_amount()}")
        print(f"Final Bill: ₱{final_bill}")

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        bill_amount = self.get_bill_amount()
        final_bill = bill_amount - (bill_amount*0.15)
        print(f"Patient Name: {self.get_name()}")
        print(f"Original Bill: ₱{self.get_bill_amount()}")
        print(f"Final Bill: ₱{final_bill}")

print("Hospital Billing System")
print("-----------------------")
regpatient = Patient("Juan Dela Cruz", 15000.0)
regpatient.calculate_bill()
print()
senpatient = SeniorPatient("Maria Santos", 15000.0)
senpatient.calculate_bill()
print()
philpatient = PhilHealthPatient("Pedro Reyes", 15000.0)
philpatient.calculate_bill()

