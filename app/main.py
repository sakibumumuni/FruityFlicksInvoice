import bson.json_util
import base64
from flask import Flask, render_template, request, session
from pymongo import MongoClient
import os

import pymongo
app=Flask(__name__)
MONGO_URL = ('mongodb+srv://code_os:codeos285@cluster0.rcvvqsb.mongodb.net/?appName=Cluster0')
client =pymongo.MongoClient(MONGO_URL)
db = client.code_os_invoice_data
CODE_OS = db.CODE_OS
print(client.list_database_names())
     # This was to get user data from the first page, and then save it in the database, so that I can retrieve it when I need to generate an invoice for the company
@app.route('/company_data', methods=['POST', 'GET'])
def get_user_data():
        if request.method == 'POST': 
         user_data = {
            'companyname': request.form.get('companyname'),
            'emailaddress': request.form.get('emailaddress'),
            'phonenumber': request.form.get('phonenumber'),
            'address': request.form.get('address'),
            'taxid': request.form.get('taxid'),
            'financialyear-startdate': request.form.get('financialyear-startdate'), 
            'financialyear-enddate': request.form.get('financialyear-enddate'),  
         }
         logo = request.files.get('logo') # this is to get the logo from the form, and then I will encode it and save it in the database, so that I can retrieve it when I need to generate an invoice for the company
         if logo:
           logo_data = logo.read() # read the logo data as bytes, so that I can encode it and save it in the database, so that I can retrieve it when I need to generate an invoice for the company
           encode_logo = base64.b64encode(logo_data).decode('utf-8')
           user_data['logo'] = encode_logo # add logo into the same document as the user data, so that I can retrieve it when I need to generate an invoice for the company
         db.CODE_OS.insert_one(user_data)  # I encoded the logo and saved it in the database, so that I can retrieve it when I need to generate an invoice for the company

        return render_template('base.html') # this information here will be in the base.html template, which is the first page that the user will see when they open the app, and then when they click on the "Create Invoice" button, it will take them to the createinvoice.html template, where they can fill in the invoice details and generate an invoice for their company
@app.route('/invoice', methods=['POST', 'GET'])
def invoice():
   if request.method == 'POST':
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
      user = db.CODE_OS.find_one({'_id': session['user_id']}) # this is to retrieve the company logo from the database, so that I can display it on the invoice template, when I generate an invoice for the company
      encode_logo = user['logo']

      return render_template('createinvoice.html', encode_logo = encode_logo)
   #return render_template('createinvoice.html', encode_logo = encode_logo) # this information here will be in the createinvoice.html template
if __name__ == '__main__':
 port = int(os.environ.get('PORT', 5000))
 app.run(debug=True, host='0.0.0.0', port=port)
