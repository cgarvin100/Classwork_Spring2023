import requests


"""
Get Request
"""

r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
print(r)
print(type(r))
print(r.status_code)
print(r.text)
branches = r.json()
print(branches)
for branch in branches:
    print(branch["name"])

outdata = {
   "name": "Christian Garvin",
   "net_id": "cgg18",
   "e-mail": "cgg18@duke.edu"
}

r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=outdata)
print(r.status_code)
print(r.text)

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json={"user": "gmoney", "message": "I knew the perc was fake, but i still ate it cuz im a gremlin"})
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Your boy, skinny p")
print(r.text)