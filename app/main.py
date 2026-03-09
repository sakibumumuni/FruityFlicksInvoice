import bson.json_util
import base64
from flask import Flask, redirect, render_template, request, session
from pymongo import MongoClient
from dotenv import load_dotenv # this is to handle the .env file, which is used to store the environment variables, such as the MongoDB connection string, so that I can access it in my code, and then I can use it to connect to the MongoDB database
import os

import pymongo
load_dotenv() # loads the .env file, so that I can access the environment variables, such as the MongoDB connection string, which is stored in the .env file, and then I can use it to connect to the MongoDB database, and then I can save the user data in the database
app=Flask(__name__, static_folder='static', template_folder='templates') 
MONGO_URL = os.environ.get('MONGO_URL')
print(MONGO_URL)
client =pymongo.MongoClient(MONGO_URL)
db = client.code_os_invoice_data
CODE_OS = db.CODE_OS
     # This was to get user data from the first page, and then save it in the database, so that I can retrieve it when I need to generate an invoice for the company
@app.route('/userdata/v1.0', methods=['POST', 'GET'])
def get_user_data():
      encode_logo = None # SO IT DOES NOT RETURN AN ERROR IF I HAVE NOT INSERED AN IMAGE YET
      if request.method == 'POST': 
         logo = request.files.get('logo') # this is to get the logo from the form, and then I will encode it and save it in the database, so that I can retrieve it when I need to generate an invoice for the company
         if logo and logo.filename:
          logo_data = logo.read() # read the logo data as bytes, so that I can encode it and save it in the database, so that I can retrieve it when I need to generate an invoice for the company
          encode_logo = base64.b64encode(logo_data).decode('utf-8')
          logo_mime = logo.content_type # tells the browser the type of image the user uploaded
         else:
          existing = db.CODE_OS.find_one(sort=[("_id", -1)]) # finding alraedy existing image in the database if no image was uploaded again
          encode_logo = existing.get('logo') if existing else None # encodes already existing logo
          logo_mime = existing.get("logo_mime") if existing else None # getting the image type of the already existing logo n the database
         # This runs for both cases (new logo or existing logo)
         user_data = {
            'companyname': request.form.get('companyname'),
            'emailaddress': request.form.get('emailaddress'),
            'phonenumber': request.form.get('phonenumber'),
            'address': request.form.get('address'),
            'taxid': request.form.get('taxid'),
            'financialyear-startdate': request.form.get('financialyear-startdate'), 
            'financialyear-enddate': request.form.get('financialyear-enddate'), 
            'logo':encode_logo, # I passes the encoded logo back into the user_data dictional so as to retain it on the home page
            'logo_mime': logo_mime  
         }
         user_data['logo'] = encode_logo # this is to add the encoded logo into the user data dictionary, so that I can save it in the database, and then I can retrieve it when I need to generate an invoice for the company
         db.CODE_OS.insert_one(user_data)  # this is to save the user data in the database, so that I can retrieve it when I need to generate an invoice for the company, and then when the user fills in the company data on the first page, which is the base.html template, and then when they click on the "Save & Continue" button, it will take them to the createinvoice.html template, where they can fill in the invoice details and generate an invoice for their company

         return redirect('/createinvoice') # this is to redirect the user to the createinvoice.html template, where they can fill in the invoice details and generate an invoice for their company, after they have filled in the company data on the first page, which is the base.html template, and then when they click on the "Save & Continue" button, it will take them to the createinvoice.html template, where they can fill in the invoice details and generate an invoice for their company
         
      return render_template('base.html') # this information here will be in the base.html template, which is the first page that the user will see when they open the app, and then when they click on the "Create Invoice" button, it will take them to the createinvoice.html template, where they can fill in the invoice details and generate an invoice for their company
@app.route('/createinvoice', methods=['POST', 'GET'])
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
         'total':request.form.get('total')
      }
      db.CODE_OS.insert_one(invoice_data) 
   logo_fetch = db.CODE_OS.find_one({"logo": {"$exists": True, "$ne": None}}, sort=[("_id", -1)]) # get the latest document from the databse with a logo stored in it
   return render_template('createinvoice.html', logo_fetch = logo_fetch) 

if __name__ == '__main__':
 port = int(os.environ.get('PORT', 5000))
 app.run(debug=True, host='0.0.0.0', port=port)
