def test():
    patient_id = 123
    patient_name = "Test"
    patient_BT = "O+"
    from health_db_server import add_patient_to_db, add_test_to_patient
    add_patient_to_db(patient_id, patient_name, patient_BT)
    test_name = "HDL"
    test_val = 150
    add_test_to_patient(patient_id, test_name, test_val)
    