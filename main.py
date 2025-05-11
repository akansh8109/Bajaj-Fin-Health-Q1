import requests

user_info = {
    "name": "Akansh Patil",
    "regNo": "0827AL221012",
    "email": "patilakansh@gmail.com"
}

gen_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
response = requests.post(generate_url, json=user_info)
response.raise_for_status()
data = response.json()

webhook_url = data["webhook"]
access_token = data["accessToken"]


final_query = {
    "finalQuery": "SELECT p.amount AS salary, e.first_name || ' ' || e.last_name AS name, FLOOR(EXTRACT(YEAR FROM AGE(CURRENT_DATE, e.dob))) AS age, d.department_name FROM Payments p JOIN Employee e ON p.emp_id = e.emp_id JOIN Department d ON e.department = d.department_id WHERE EXTRACT(DAY FROM p.payment_time) != 1 ORDER BY p.amount DESC LIMIT 1;"
}

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

sub_resp = requests.post(webhook_url, json=final_query, headers=headers)
sub_resp.raise_for_status()

print("Submission Response:", submit_response.text)
