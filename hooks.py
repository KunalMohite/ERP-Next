from . import __version__ as app_version

app_name = "assignment"
app_title = "Assignment"
app_publisher = "Kunal Mohite"
app_description = "This app is for testing purpose only"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@kunal.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/assignment/css/assignment.css"
#app_include_js = "/assets/assignment/js/assignment.js"

# include js, css files in header of web template
web_include_css = "/assets/assignment/css/assignment.css"
web_include_js = "/assets/assignment/js/assignment.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "assignment/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "assignment.install.before_install"
# after_install = "assignment.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "assignment.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
   "Customer Feedback":{
	   # When : function to call
       'validate':"assignment.assignment.doctype.customer_feedback.send_sms"
   } 
 }

# Scheduled Tasks
# ---------------

scheduler_events = {
    
    "cron":{
		"*\1 * * * *":[
			"assignment.tasks.cron"
		]
	},
 	"all": [
 		"assignment.tasks.all"
 	],
 	"daily": [
 		"assignment.tasks.daily"
 	],
 	"hourly": [
 		"assignment.tasks.hourly"
 	],
 	"weekly": [
 		"assignment.tasks.weekly"
 	],
 	"monthly": [
 		"assignment.tasks.monthly"
 	]
 }

# Testing
# -------

# before_tests = "assignment.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "assignment.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "assignment.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"assignment.auth.validate"
# ]


test_string = 'value'
test_list = ['value']
test_dict = {
    'key': 'value'
}

# Portal Sidebar
portal_menu_items = [
    {"title": "Sidebar one", "route": "/all-products", "role": "Customer"},
    {"title": "Sidebar two", "route": "/all-products", "role": "Customer"},
    {"title": "Sidebar three", "route": "/all-products", "role": "Customer"},
]

# Add Calendars
calendars = ["Event Managment"]

# Website 404
website_catch_all = 'not_found'