import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

request_json = {"name": "Celina Zhouet", "net_id": "cz124", "e-mail": "cz124@duke.edu"}
r = requests.post(server_name + "student", json=request_json)