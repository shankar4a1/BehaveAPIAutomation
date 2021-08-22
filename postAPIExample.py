from payLoad import *
import requests

from payLoad import *
from utilities.configurations import *
from utilities.resources import *

#
url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {"Content-Type": "application/json"}
query = 'select * from Books'
addBook_response = requests.post(url, json=addBookPayload("mant"), headers=headers, )
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)
# Delete Book -
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

    "ID": bookId
}, headers={"Content-Type": "application/json"},
                                    )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

# Authentication
se = requests.session()
se.auth = auth = ('rahulshettyacademy', getPassword())

url = "https://api.github.com/user"
github_response = requests.get(url, verify=False, auth=('rahulshettyacademy', getPassword()))

print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response.status_code)
