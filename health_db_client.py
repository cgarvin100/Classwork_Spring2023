import requests

if __name__ == '__main__':
    server = "http://127.0.0.1:5000"

    patient = {"id": 1, "name": "Christian", "blood_type": "A+"}

    r = requests.post(server+"/new_patient", json=patient)
    print(r.status_code)
    print(r.text)

    test = {"id": 1, "test_name": "BPM", "test_result": 160}
    r = requests.post(server + "/add_test", json=test)
    print(r.status_code)
    print(r.text)

    r = requests.get(server + "/get_results/1")
    print(r.status_code)
    print(r.text)


