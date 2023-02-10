class Patient:
   def __init__(self, first_name="", last_name="", age=0, mrn=0, tests=[]):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.mrn = mrn
       self.tests = tests

   def get_full_name(self):
       return "{} {}".format(self.first_name, self.last_name)

   def is_adult(self):
       return self.age > 18


if __name__ == '__main__':
   new_patient = Patient("Christian", "Garvin", 22, 1, [("HDL", 100)])
   second_patient = Patient("Zach", "Thomson", 23, 2)
   third_patient = Patient("Little", "Girl", 5, 3)
   print(new_patient.get_full_name())
   print(new_patient.is_adult())
   print(third_patient.is_adult())
