import bson.json_util

from flask import Flask, render_template, request
from pymongo import MongoClient
import os

import pymongo
app=Flask(__name__)
MONGO_URL = ('mongodb+srv://code_os:codeos285@cluster0.rcvvqsb.mongodb.net/?appName=Cluster0')
client =pymongo.MongoClient(MONGO_URL)
db = client.code_os_invoice_data
CODE_OS = db.CODE_OS
print(client.list_database_names())
     
@app.route('/company_data', methods=['POST', 'GET'])
def get_user_data():
        if request.method == 'POST':
        # get data from the , this is to send the company's details into our databse, so that we have access to their basic information, in case we deploy the system for them,
        # or better still to help keep track of anyone from the company who logs in to the sytem, so the company holds them accountable for any invoice they generated 
         user_data = {
            'companyname': request.form.get('companyname'),
            'emailaddress': request.form.get('emailaddress'),
            'phonenumber': request.form.get('phonenumber'),
            'address': request.form.get('address'),
            'taxid': request.form.get('taxid'),
            'financialyear-startdate': request.form.get('financialyear-startdate'), 
            'financialyear-enddate': request.form.get('financialyear-enddate'),
            'companylogo':request.form.get('companylogo')
         }
         CODE_OS.insert_one(user_data)
        return render_template('base.html')
@app.route('/invoice', methods=['POST', 'GET'])
def invoice():
   invoice_data = {
      'client_name':request.form.get('client_name'),
      'email_address':request.form.get('email_address'),
      'address':request.form.get('address'),
     'invoice_number':request.form.get('invoice_number'),
    'issue_date':request.form.get('issue_date'),
    'due_date':request.form.get('due_date'),
    'invoice_itemdescription':request.form.get('invoice_itemdescription'),
    'quantity':request.form.get('quantity'),
    'price':request.form.get('price'),
    'subtotal':request.form.get('subtotal'),
    'tax':request.form.get('tax'),
    'total':request.form.get('total')
     }
if __name__ == '__main__':
 port = int(os.environ.get('PORT', 5000))
 app.run(debug=True, host='0.0.0.0', port=port)
