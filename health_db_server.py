from flask import Flask, request, jsonify

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


if __name__ == '__main__':
    app.run()
