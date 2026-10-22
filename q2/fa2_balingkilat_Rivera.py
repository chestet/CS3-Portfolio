class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_bill_amount(self):
        return self.bill_amount
    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount
    def calculate_bill(self):
        print(f"Patient Name: {self.name}")
        print(f"Original Bill: ₱{self.bill_amount}")
        print(f"Final Bill: ₱{self.bill_amount}")
        
class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        self.final_bill = self.bill_amount - self.bill_amount*0.2
    def calculate_bill(self):
        print(f"Patient Name: {self.name}")
        print(f"Original Bill: ₱{self.bill_amount}")
        print(f"Final Bill: ₱{self.final_bill}")

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        self.final_bill = self.bill_amount - self.bill_amount*0.15
    def calculate_bill(self):
        print(f"Patient Name: {self.name}")
        print(f"Original Bill: ₱{self.bill_amount}")
        print(f"Final Bill: ₱{self.final_bill}")

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
