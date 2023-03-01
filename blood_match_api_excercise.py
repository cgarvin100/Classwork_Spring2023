import requests

url = "http://vcm-7631.vm.duke.edu:5002"

ids = requests.get(url+"/get_patients/cgg18")
print(ids.text)

don_id = ids.text[10:12]
rec_id = ids.text[27:29]

don_blood_type = requests.get(url + "/get_blood_type/"+don_id)
rec_blood_type = requests.get(url + "/get_blood_type/"+rec_id)

print("Donor Blood Type: {}".format(don_blood_type.text))
print("Recipient Blood Type: {}".format(rec_blood_type.text))
print("Is Match: No")

result = {"Name": "cgg18", "Match":  "No"}
r = requests.post(url+"/match_check", json=result)
print("Result: " + r.text)



