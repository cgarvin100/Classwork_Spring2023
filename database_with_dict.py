def create_patient_entry(first_name, last_name, patient_mrn, patient_age):
   new_patient = {"First Name": first_name, "Last Name": last_name,
                  "MRN": patient_mrn, "Age": patient_age, "Tests": []}
   return new_patient


def get_patient_entry(db, mrn):
   try:
       return db[mrn]
   except KeyError:
       print("MRN {} not in the database".format(mrn))
       return False


def add_test_to_patient(db, mrn, test_name, test_value):
   patient = get_patient_entry(db, mrn)
   if patient is False:
       print("Patient does not exist")
       return
   patient["Tests"].append([test_name, test_value])
   print(db)
   return


def print_directory(db, room_numbers):

   for patient, number in zip(db.values(), room_numbers):
       print("Patient {} is in room {}".format(get_full_name(patient), number))
   return


def get_patient_test_result(db, mrn, test_name):
   patient = get_patient_entry(db, mrn)
   if not patient:
       print("Patient does not exist")
       return False

   patient_tests = patient["Tests"]
   return find_result(patient_tests, test_name)


def find_result(tests, test_name):
   for test in tests:
       if test_name == test[0]:
           return test[1]
   else:
       return False


def get_full_name(patient):
   full_name = patient["First Name"] + " " + patient["Last Name"]
   return full_name


def print_database(db):
   for patient in db.values():
       print("MRN: {}, Full Name: {}, Age: {}".format(patient["MRN"], get_full_name(patient), patient["Age"]))
   return


def main_driver():
   db = {1: create_patient_entry("Anne", "Ables", 1, 34),
         2: create_patient_entry("Bob", "Boyles", 2, 45),
         3: create_patient_entry("Chris", "Chou", 3, 63)}

   print(db)
   print("Bob's Age: " + str(db[2]["Age"]))
   print("Patient MRN 1: " + str(get_patient_entry(db, 1)))
   add_test_to_patient(db, 1, "HDL", 120)
   print(db)

   room_numbers = ["103", "232", "333"]

   print_directory(db, room_numbers)
   print_database(db)

   HDL_test_result = get_patient_test_result(db, 1, 'HDL')
   print(HDL_test_result)

   return


if __name__ == '__main__':
   main_driver()
