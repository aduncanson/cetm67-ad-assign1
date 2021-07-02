"""Testing the very simple RESTful API
Note: Ensure Flask server is running on http://127.0.0.1:5000/
      before running this script.
"""

import requests
import os
import json


BASE_URL = "https://h3uvgoj03j.execute-api.us-east-1.amazonaws.com/CETM67_Assign1/"

aws_access_key_id='ASIAYJCKGV2TQ4IFEUWH'
aws_secret_access_key='tsJv620ll9eKn5+JDzm1/4B4k5W34yVShewjruKu'
aws_session_token='FwoGZXIvYXdzEAsaDPL7L9wq58IYfXI/dyK+AW3PctCPjK68J+R+7ZbSB0knpphCY+iD+7Kprq/exYNth8Fs0QRhpQw/RRiV8JOFer0pDmohpONnu+6ZV38v+O589+uK4l0VGz0NlqP3edC8l8snOtTTkyRvMBW3P3e2DkcuKFl0yrW2qEWfJMBXk3z5uNWl01GZUJEheBKnRdo8Vj1jRtHPOjuJtRyq+2Lgloa578SMlFqnpZNXDQp4Eu/q8OcFVcDGWTsiVP6I3SpP9OIG7iIplMFw9zcxp7cojr/7hgYyLYB7y+5T14CGi1y9DWWKrSAOXb9ldfKig0XJuxJiKapXdehGI7Ze8Dff5pUooA=='
region_name='us-east-1'

# Test 1 - GET the home landing API
os.system("cls")
print()
print('#################################################################################')
print('Test 1 - GET the home landing API')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL)
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#This is the root of Adam Duncanson's CETM67 Assignment 1 API AWS pages
#    There are several extensions to this home page:
#        / (GET) - Home page
#        /customer (GET,POST) - Gathers customer details and creates new customers
#        /downloadPDF (GET) - Downloads PDF for print_id passed in
#        /empty-s3-bucket (GET,POST) - Empties the passed s3 bucket
#        /loan (GET,POST) - Gathers loan details and creates new loans
#        /loan/activate (GET,POST) - Activates or cancels a pending loan
#        /loan/close (GET,POST) - Closes an active loan
#        /reprint-letter (GET,POST) - regenerates previously created PDFs by their archived meta-data''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 2 - POST the home landing API
print()
print('#################################################################################')
print('Test 2 - POST the home landing API')
print('#################################################################################')
print()
print('Observed response:')
response = requests.post(BASE_URL)
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#403
#{"message":"Missing Authentication Token"}
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 3 - GET the customer API, no query string
print()
print('#################################################################################')
print('Test 3 - GET the customer API, no query string')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/customer')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#Add the query parameter 'customer_id' to the current URL to return information about the given customer_id.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 4 - GET the customer API, query string with invalid customer_id
print()
print('#################################################################################')
print('Test 4 - GET the customer API, query string with invalid \'customer_id\'')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/customer?customer_id=1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#Unable to get customer '1'. Error message: 'Item'
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 5 - POST the customer API, create a new customer
print()
print('#################################################################################')
print('Test 5 - POST the customer API, create a new customer')
print('#################################################################################')
print()
print('Observed response:')
print('''Use the API Gateway with below body:

{
    "name": {
        "title": "Mr",
        "first_name": "Adam",
        "middle_names": "McKinlay",
        "surname": "Duncanson"
    },
    "address": {
        "line1": "1 Address Street",
        "line2": "Address Town",
        "county": "Townshire",
        "postcode": "AB1 2CD"
    },
    "dob": "23/05/1994",
    "gender": "male",
    "loans": []
}''')



print()
print('Expected response (\'#\' indent):')

print('''#200
#Customer created! Customer ID is 1
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 6 - GET the customer API, query string with valid customer_id
print()
print('#################################################################################')
print('Test 6 - GET the customer API, query string with valid \'customer_id\'')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/customer?customer_id=1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#{"loans": [], "customer_id": "1", "address": {"county": "Townshire", "postcode": "AB1 2CD", "line2": "Address Town", "line1": "1 Address Street"}, "name": {"title": "Mr", "first_name": "Adam", "middle_names": "McKinlay", "surname": "Duncanson"}, "gender": "male", "dob": "23/05/1994"}
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 7 - GET the loan API with no query string
print()
print('#################################################################################')
print('Test 7 - GET the loan API with no query string')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/loan')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#Add the query parameter 'loan_id' to the current URL to return information about the given loan_id.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 7.5 - GET the loan API, query string with invalid loan_id
print()
print('#################################################################################')
print('Test 7.5 - GET the loan API, query string with invalid \'loan_id\'')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/loan?loan_id=1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#Unable to find loan 1. Error message: 'Item'
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 8 - POST the loan API, create a new loan
print()
print('#################################################################################')
print('Test 8 - POST the loan API, create a new loan')
print('#################################################################################')
print()
print('Observed response:')
print('''Use the API Gateway with below query string and body:

customer_id=1

{
    "amount": "2000.00",
    "brand": "Lloyds",
    "start_date": "01/01/2021",
    "end_date": "31/12/2021",
    "letters": []
}''')


print()
print('Expected response (\'#\' indent):')

print('''#200
#"Loan created in pending status. Loan ID is 1"
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 9 - GET the loan API, query string with valid loan_id
print()
print('#################################################################################')
print('Test 9 - GET the loan API, query string with valid loan_id')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/loan?loan_id=1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#{"product": "DXC ", "loan_status": "Pending customer confirmation", "end_date": "31/12/2021", "start_date": "01/01/2021", "letters": [], "amount": "2000.00", "customer_id": "1", "brand": "Lloyds", "loan_id": "1"}
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 10 - GET the customer API, query string with valid customer_id and view loans
print()
print('#################################################################################')
print('Test 10 - GET the customer API, query string with valid customer_id and view loans')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/customer?customer_id=1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#{{"loans": ["1"], "customer_id": "1", "address": {"county": "Townshire", "postcode": "AB1 2CD", "line2": "Address Town", "line1": "1 Address Street"}, "name": {"title": "Mr", "first_name": "Adam", "middle_names": "McKinlay", "surname": "Duncanson"}, "gender": "male", "dob": "23/05/1994"}
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 11 - POST the loan API, where customer has existing loan
print()
print('#################################################################################')
print('Test 11 - POST the loan API, where customer has existing loan')
print('#################################################################################')
print()
print('Observed response:')
print('''Use the API Gateway with below query string and body:

customer_id=1

{
    "amount": "2000.00",
    "brand": "Lloyds",
    "start_date": "01/01/2021",
    "end_date": "31/12/2021",
    "letters": []
}''')


print()
print('Expected response (\'#\' indent):')

print('''#200
#"This customer already has a loan at status 'Pending customer confirmation'. Loan ID is 1"
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 12 - GET the activate loan API with no query strings
print()
print('#################################################################################')
print('Test 13 - GET the activate loan API with no query strings')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/loan/activate')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#This API activates or cancels a loan passed in the query string 'loan_id' via the POST method ONLY. Passed in the body needs to be a field 'new_status'. If it is set to 'Active' the loan will activate and generate a Welcome letter, else it will cancel.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 13 - POST the activate loan API with query strings and cancel status
print()
print('#################################################################################')
print('Test 13 - POST the activate loan API with query strings and cancel status')
print('#################################################################################')
print()
print('Observed response:')
print('''Use the API Gateway with below query string and body:

loan_id=1

{
    "new_status": "Cancel"
}''')


print()
print('Expected response (\'#\' indent):')

print('''#200
#The new status for Loan 1 is 'Cancelled'.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 14 - GET the loan API, query string with valid loan_id and view status
print()
print('#################################################################################')
print('Test 14 - GET the loan API, query string with valid loan_id and view status')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/loan?loan_id=1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#{"product": "DXC ", "loan_status": "Cancelled", "end_date": "31/12/2021", "start_date": "01/01/2021", "letters": [], "amount": "2000.00", "brand": "Lloyds", "customer_id": "1", "loan_id": "1"}
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 15 - POST the activate loan API with query strings and cancel status to cancel a cancelled loan
print()
print('#################################################################################')
print('Test 15 - POST the activate loan API with query strings and cancel status to cancel a cancelled loan')
print('#################################################################################')
print()
print('Observed response:')
print('''Use the API Gateway with below query string and body:

loan_id=1

{
    "new_status": "Cancel"
}''')


print()
print('Expected response (\'#\' indent):')

print('''#200
#Loan 1 is not pending and cannot receive any action via this API call.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 16 - Create a new loan and POST the activate loan API with query strings and active status
print()
print('#################################################################################')
print('Test 16 - Create a new loan and POST the activate loan API with query strings and active status')
print('#################################################################################')
print()
print('Observed response:')
print('''Use the API Gateway with below query string and body:

customer_id=1

{
    "amount": "2000.00",
    "brand": "Lloyds",
    "start_date": "01/01/2021",
    "end_date": "31/12/2021",
    "letters": []
}


Use the API Gateway with below query string and body:

loan_id=2

{
    "new_status": "Active"
}''')


print()
print('Expected response (\'#\' indent):')

print('''#200
#"Loan created in pending status. Loan ID is 2"
#
#200
#The new status for Loan 3 is 'Active'.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 17 - GET the loan API, query string with valid loan_id and view letters
print()
print('#################################################################################')
print('Test 17 - GET the loan API, query string with valid loan_id and view letters')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/loan?loan_id=2')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#{"product": "DXC ", "loan_status": "Active", "end_date": "31/12/2021", "start_date": "01/01/2021", "letters": ["1"], "amount": "2000.00", "brand": "Lloyds", "customer_id": "1", "loan_id": "2"}
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 18 - GET the close loan API
print()
print('#################################################################################')
print('Test 18 - GET the close loan API')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/loan/close')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#This API closes a loan passed in the query string 'loan_id' via the POST method ONLY.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 19 - POST the close loan API with query strings with inactive loan_id
print()
print('#################################################################################')
print('Test 19 - POST the close loan API with query strings with inactive loan_id')
print('#################################################################################')
print()
print('Observed response:')
response = requests.post(BASE_URL + '/loan/close?loan_id=1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#Loan 1 is not active and cannot receive any action via this API call.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 20 - POST the close loan API with query strings with active loan_id
print()
print('#################################################################################')
print('Test 20 - POST the close loan API with query strings with active loan_id')
print('#################################################################################')
print()
print('Observed response:')
response = requests.post(BASE_URL + '/loan/close?loan_id=2')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#Loan 2 is now closed.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 21 - GET the loan API, query string with valid loan_id and view letters
print()
print('#################################################################################')
print('Test 21 - GET the loan API, query string with valid loan_id and view letters')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/loan?loan_id=2')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#{"product": "DXC ", "loan_status": "Closed", "end_date": "31/12/2021", "start_date": "01/01/2021", "letters": ["1", "2"], "amount": "2000.00", "brand": "Lloyds", "customer_id": "1", "loan_id": "2"}
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 22 - GET the empty S3 bucket API
print()
print('#################################################################################')
print('Test 22 - GET the empty S3 bucket API')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/empty-s3-bucket')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#This API empties the given bucket passed in the query string 'bucket_name' via the POST method ONLY.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 23 - POST the empty S3 bucket API, query string with invalid bucket name
print()
print('#################################################################################')
print('Test 23 - POST the empty S3 bucket API, query string with invalid bucket name')
print('#################################################################################')
print()
print('Observed response:')
response = requests.post(BASE_URL + '/empty-s3-bucket?bucket_name=printed-documents1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#Unable to delete all objects from bucket 'printed-documents1'. Error message: An error occurred (NoSuchBucket) when calling the ListObjects operation: The specified bucket does not exist
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 24 - POST the empty S3 bucket API, query string with valid bucket name
print()
print('#################################################################################')
print('Test 24 - POST the empty S3 bucket API, query string with valid bucket name')
print('#################################################################################')
print()
print('Observed response:')
print('View \'printed-documents\' bucket before and after. Enter to continue...')
os.system("pause")
response = requests.post(BASE_URL + '/empty-s3-bucket?bucket_name=printed-documents')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#All objects deleted from bucket 'printed-documents'.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 25 - GET the reprint API
print()
print('#################################################################################')
print('Test 25 - GET the reprint API')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/reprint-letter')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#This API regenerates the PDF for the l passed in the query string 'print_id' via the POST method ONLY.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 26 - POST the reprint API, query string with valid print_id
print()
print('#################################################################################')
print('Test 26 - POST the reprint API, query string with valid print_id')
print('#################################################################################')
print()
print('Observed response:')
print('View \'printed-documents\' bucket before and after. Enter to continue...')
os.system("pause")
response = requests.post(BASE_URL + '/reprint-letter?print_id=1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#Letter 1 has been reprinted.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 27 - GET the download API, with no query string
print()
print('#################################################################################')
print('Test 27 - GET the download API, with no query string')
print('#################################################################################')
print()
print('Observed response:')
response = requests.get(BASE_URL + '/downloadpdf')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#This API downloads a PDF of based passed query string 'print_id' via the GET method ONLY.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")
# Test 28 - GET the download API, with valid query string
print()
print('#################################################################################')
print('Test 28 - GET the download API, with valid query string')
print('#################################################################################')
print()
print('Observed response:')
print('Check download folder before and after. Enter to continue...')
os.system("pause")
response = requests.get(BASE_URL + '/downloadpdf?print_id=1')
print(response.status_code)
print(response.text)


print()
print('Expected response (\'#\' indent):')

print('''#200
#Downloaded file 'print_id_1.pdf'.
''')

print()
print('---------------------------------------------------------------------------------')
os.system("pause")
os.system("cls")