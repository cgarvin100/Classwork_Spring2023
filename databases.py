def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age]
    return new_patient


def main_driver():
    db = []
    db.append(create_patient_entry("Anne Ables", 1, 34))
    db.append(create_patient_entry("Bob Boyles", 2, 45))
    db.append(create_patient_entry("Chris Chou", 3, 63))
    print(db)
    print("Bob's Age: " + str(db[1][2]))
    print("PAtirn MRN 1: " + str(get_patient_entry(db, 1)))

def get_patient_entry(db, mrn):
    for patient in db:
        if patient[1] == mrn:
            return patient
    return None

if __name__ == '__main__':
    main_driver()