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
      'clientname':request.form.get('clientname'),
      'clientemail':request.form.get('clientemail'),
      'clientaddress':request.form.get('clientaddress'),
     'invoice_number':request.form.get('invoicenumber'),
    'issuedate':request.form.get('issuedate'),
    'duedate':request.form.get('duedate'),
    'itemdescription':request.form.get('itemdescription'),
    'quantity':request.form.get('quantity'),
    'unitprice':request.form.get('unitprice'),
    'subtotal':request.form.get('subtotal'),
    'tax':request.form.get('tax'),
    'total':request.form.get('total')


           }
if __name__ == '__main__':
 port = int(os.environ.get('PORT', 5000))
 app.run(debug=True, host='0.0.0.0', port=port)
