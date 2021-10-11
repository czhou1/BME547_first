import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

r = requests.get(server_name + "get_patients/cz124")

r1 = requests.get(server_name + "get_blood_type/M2")
r2 = requests.get(server_name + "get_blood_type/F7")

#print(r1.text, r2.text)

request_json = {"Name": 'cz124', "Match": 'Yes'}

r3 = requests.post(server_name + "match_check", json=request_json)
print(r3.text)