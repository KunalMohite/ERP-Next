import frappe
@frappe.whitelist(allow_guest=True)
def kunal():
    #return frappe.db.sql("select * from tabCustomer Feedback")
    
    #return frappe.db.get_list("select * from tabCustomer Feedback")
    
    #return frappe.get_all("Customer Feedback")
    
    #return frappe.db.count('Customer Feedback')
    
    return frappe.get_installed_apps()
    
    #return frappe.get_meta('Customer Feedback').fields 
    
    #return frappe.form_dict
    
    #return frappe.db.exists('Customer Feedback','Rahul')
    
