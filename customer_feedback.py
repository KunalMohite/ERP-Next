# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CustomerFeedback(Document):
      pass

    #def validate(self):
     #   frappe.msgprint("Hello from 'validate' event")
        

    #def before_save(self):
    #frappe.msgprint("Hello from 'before_save' event")

    #def before_insert(self):
    #   frappe.msgprint("Hello from 'before_insert' event")

    #def after_insert(self):
    #  frappe.msgprint("Hello from 'after_insert' event")

    #def on_update(self):
    #  frappe.msgprint("Hello from 'on_update' event")

    #def before_submit (self):
    # frappe.msgprint("Hello from 'before_submit' event")

    #def on_submit(self):
    #   frappe.msgprint("Hello from 'on_submit' event")

    #def on_cancel(self):
    #   frappe.msgprint("Hello from 'on_cancel' event")

    #def after_delete(self):
    #frappe.msgprint("Hello from 'after_delete' event")
    
    

    #-----------frappe.db.get_value(doctype, name, fieldname) 
    # //to fetch the field name values from other documents
#@frappe.whitlist()
#def get_value(self):
    #first_name, last_name = frappe.db.get_value('Customer Feedback', 'Rahul', ['first_name','last_name'])
   # frappe.msgprint(("The Selected Doctype First Name is {0} and Last Name is {1}").format(first_name,last_name))
      

    #-------frappe.db.set_value(doctype, name, fieldname, value)
    # to set or change the values of particular doctype
    
    #def validate(self):
      # self.set_value()bmitable.
    # def set_value(self):
    #   frappe.db.set_value('Customer Feedback','Rahul','last_name', 'Jain')
    

    #--------frappe.get_doc(doctype, name)
      
        #def validate(self):
            #self.get_document()
        
        #def get_document(self):
            #get a single doctype
            #doc = frappe.get_doc('Customer Feedback','Rahul')
            #frappe.msgprint(("The Customer Selected Field Name is {0}").format(doc.first_name))
      
       
       
   #---------------- frappe.new_doc(doctype)
   
@frappe.whitelist()   
def newapi():
    doc = frappe.new_doc('Customer Feedback')
    doc.first_name = 'Tanu'
    doc.last_name = 'Sharma'
    doc.rating = 3
    doc.save(ignore_permissions=True)
    frappe.db.commit()
    return "New Data Has Been Created successfully"
           
    #def validate(self):
           #frappe.delete_doc('Customer Feedback', 'Rahul')
           
           
           
           
#------------frappe.db.sql(query, filters, as dict)


    #def validate(self):
         #  self.yup()
    #def yup(self):
     #      data = frappe.db.sql("""
     #                              last_name
      #                           FROM 
     #                                'tabCustomer Feedback'
      #                           WHERE
      #                               enable = 1
      #                          """, as_dict=1)
      #     for d in data:
     #             frappe.msgprint(("The Parent FirstName is {0} and LastName is {1}").format(d.first_name,d.last_name))
      



        