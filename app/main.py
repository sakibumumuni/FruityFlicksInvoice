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
        # get data from the form
         user_data = {
            'companyname': request.form.get('companyname'),
            'emailaddress': request.form.get('emailaddress'),
            'phonenumber': request.form.get('phonenumber'),
            'address': request.form.get('address'),
            'taxid': request.form.get('taxid'),
            'financialyear-startdate': request.form.get('financialyear-startdate'), 
            'financialyear-enddate': request.form.get('financialyear-enddate')
         }
         CODE_OS.insert_one(user_data)
        return render_template('base.html')

if __name__ == '__main__':
 port = int(os.environ.get('PORT', 5000))
 app.run(debug=True, host='0.0.0.0', port=port)
