# Copyright (c) 2021, Kunal Mohite and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class NewWeather1(Document):
	pass
@frappe.whitelist()   
def weapi():   
    doc = frappe.get_doc({
         "doctype": "States",
         "state_name": "Goa",
         
         "child_table":[
             {
               "date": "30-07-2021",
               "temprature": "15",
               "season": "Winter",
             }
        ]
    })
    doc.insert()
    return "New Data Has Been Created successfully" 