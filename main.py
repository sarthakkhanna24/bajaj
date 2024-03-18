import requests

# Create Investment Account
url1 = "https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/createAccount"
headers1 = {"Content-Type": "application/json"}
data1 = {
    "name": "Sarthak Khanna",
    "email": "sarthak1826.be21@chitkara.edu.in",
    "rollNumber": "2110991826",
    "phone": "8707314023"
}
response1 = requests.post(url1, json=data1, headers=headers1)
account_number = response1.json()["accountNumber"]
print(account_number);

# Research Bajaj Finserv
# (This step is not necessary as we are using a simulation API)

# Invest Wisely
url2 = "https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/buyStocks"
headers2 = {"Content-Type": "application/json", "bfhl-auth": "2110991826"}
data2 = {
    "company": "Bajaj Finserv",
    "currentPrice": 1200,  # Replace with the real current stock price
    "accountNumber": account_number,
    "githubRepoLink": "https://github.com/"  # Pass your github repo link here
}
response2 = requests.post(url2, json=data2, headers=headers2)
print(response2.json())