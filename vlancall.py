import requests
import getpass
import json

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
username = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload)

TJson = json.loads(response.text)
token = TJson['Token']

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/topology/vlan/vlan-names"

payload={}
headers = {
  'Accept': 'application/json',
  'X-Auth-Token': token,
  'Authorization': 'Bearer ' + token,
  'Cookie': 'JSESSIONID=dve3goehf04014zwruyyhd2bd'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
