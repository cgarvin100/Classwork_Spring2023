def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age, []]
    return new_patient

def get_patient_entry(db, mrn):
    for patient in db:
        if patient[1] == mrn:
            return patient
    return False

def add_test_to_patient(db, mrn, test_name, test_value):
    patient = get_patient_entry(db, mrn)
    if patient is False:
        print("Patient does not exist")
        return
    patient[3].append([test_name, test_value])
    print(db)
    return

def print_directory(db, room_numbers):
    for i,patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))

    print("\n----------Method 2----------\n")

    for patient,number in zip(db, room_numbers):
        print("Patient {} is in room {}".format(patient[0], number))
    return

def get_patient_test_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    if patient == False:
        print("Patient does not exist")
        return False
    
    pateint_tests = patient[3]
    return find_result(pateint_tests, test_name)


def find_result(tests, test_name):
    for test in tests:
        if test_name == test[0]:
            return test[1]
    else:
        return False


def main_driver():
    db = []
    db.append(create_patient_entry("Anne Ables", 1, 34))
    db.append(create_patient_entry("Bob Boyles", 2, 45))
    db.append(create_patient_entry("Chris Chou", 3, 63))

    print(db)
    print("Bob's Age: " + str(db[1][2]))
    print("Patient MRN 1: " + str(get_patient_entry(db, 1)))
    add_test_to_patient(db, 1, "HDL", 120)
    print(db)

    room_numbers = ["103", "232", "333"]

    print_directory(db, room_numbers)

    HDL_test_result  = get_patient_test_result(db, 1, 'HDL')
    print(HDL_test_result)

    return

if __name__ == '__main__':
    main_driver()