from flask import Flask, request, jsonify
from pymodm import connect

db = {}

app = Flask(__name__)


def add_patient_to_db(id, name, blood_type):
    new_patient = {
        "id": id,
        "name": name,
        "blood_type": blood_type,
        "tests": []
    }
    db[id] = new_patient
    print(db)


def add_test_to_patient(id, test_name, test_result):
    db[id]["tests"].append([test_name, test_result])
    print(db)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    in_data = request.get_json()
    answer = new_patient_driver(in_data)
    return jsonify(answer)


def new_patient_driver(in_data):
    validation = validate_input_data_add_patient(in_data)
    if validation is not True:
        return jsonify(validation), 400

    add_patient_to_db(in_data["id"],
                      in_data["name"],
                      in_data["blood_type"])

    return "Patient Successfully Added", 200


def validate_input_data_add_patient(in_data):
    if type(in_data) is not dict:
        return "Not a dict"

    expected_keys = ["id", "name", "blood_type"]
    expected_types = [int, str, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Missing {} Key".format(key)
        if type(in_data[key]) != value_type:
            return "Incorrect value type for key {}".format(key)
    return True


@app.route("/add_test", methods=["POST"])
def post_new_test():
    in_data = request.get_json()
    answer = new_test_driver(in_data)
    return jsonify(answer)


def new_test_driver(in_data):
    validation = validate_input_data_add_test(in_data)
    if validation is not True:
        return validation, 400

    add_test_to_patient(in_data["id"],
                        in_data["test_name"],
                        in_data["test_result"])

    return "Patient Test Added", 200


def validate_input_data_add_test(in_data):
    if type(in_data) is not dict:
        return "Not a dict"
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Missing {} Key".format(key)
        if type(in_data[key]) != value_type:
            return "Incorrect value type for key {}".format(key)

    if in_data["id"] not in db:
        return "Patient {} not in database".format(in_data["id"])
    return True


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results_driver(patient_id):
    validation = validate_patient_id(patient_id)
    if validation is not True:
        return validation, 400
    patient = db[int(patient_id)]
    return patient['tests'], 200


def validate_patient_id(patient_id):
    try:
        patient_id = int(patient_id)
    except ValueError:
        return "Input patient ID is not an integer"

    if patient_id not in db:
        return "Patient {} not in database".format(patient_id)

    return True


def init_server():
    
    return



if __name__ == '__main__':
    init_server()
    app.run()
