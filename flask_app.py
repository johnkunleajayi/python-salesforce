from flask import Flask, render_template
from simple_salesforce import Salesforce

app = Flask(__name__)

# Salesforce credentials
username = 'email'
password = 'password'
security_token = 'token'
domain = 'login'

# Create Salesforce connection
def connect_salesforce():
    return Salesforce(username=username, password=password, security_token=security_token, domain=domain)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/accounts')
def accounts():
    try:
        sf = connect_salesforce()
        query = "SELECT Id, Name, Industry FROM Account LIMIT 10"
        records = sf.query(query)['records']
        return render_template('accounts.html', accounts=records)
    except Exception as e:
        return f"<h3>Error loading accounts:</h3><pre>{e}</pre>"

@app.route('/contacts')
def contacts():
    try:
        sf = connect_salesforce()
        query = "SELECT Id, FirstName, LastName, Email FROM Contact LIMIT 10"
        records = sf.query(query)['records']
        for r in records:
            r['FullName'] = f"{r.get('FirstName', '')} {r.get('LastName', '')}".strip()
        return render_template('contacts.html', contacts=records)
    except Exception as e:
        return f"<h3>Error loading contacts:</h3><pre>{e}</pre>"

@app.route('/opportunities')
def opportunities():
    try:
        sf = connect_salesforce()
        query = "SELECT Id, Name, StageName, CloseDate FROM Opportunity LIMIT 10"
        records = sf.query(query)['records']
        return render_template('opportunities.html', opportunities=records)
    except Exception as e:
        return f"<h3>Error loading opportunities:</h3><pre>{e}</pre>"

@app.route('/leads')
def leads():
    try:
        sf = connect_salesforce()
        query = "SELECT Id, Name, Status, FirstName, LastName, Company, Email FROM Lead LIMIT 10"
        records = sf.query(query)['records']
        return render_template('leads.html', leads=records)
    except Exception as e:
        return f"<h3>Error loading leads:</h3><pre>{e}</pre>"

@app.route('/cases')
def cases():
    try:
        sf = connect_salesforce()
        query = "SELECT Id, Subject, Status, Priority, ContactId FROM Case LIMIT 10"
        records = sf.query(query)['records']
        return render_template('cases.html', cases=records)
    except Exception as e:
        return f"<h3>Error loading cases:</h3><pre>{e}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
