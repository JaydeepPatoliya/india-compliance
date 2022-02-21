from . import __version__ as app_version

app_name = "india_compliance"
app_title = "India Compliance"
app_publisher = "Resilient Tech"
app_description = "ERPNext app to simplify compliance with Indian Rules and Regulations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "india.compliance@resilient.tech"
app_license = "GNU General Public License (v3)"
required_apps = ["erpnext"]

doctype_js = {
    "Item": "india_compliance/gst_india/client_scripts/item.js",
    "Supplier": "india_compliance/gst_india/client_scripts/supplier.js",
    "Customer": "india_compliance/gst_india/client_scripts/customer.js",
    "Sales Order": "india_compliance/gst_india/client_scripts/sales_order.js",
    "Delivery Note": "india_compliance/gst_india/client_scripts/delivery_note.js",
    "Purchase Order": "india_compliance/gst_india/client_scripts/purchase_order.js",
    "Journal Entry": "india_compliance/gst_india/client_scripts/journal_entry.js",
    "Payment Entry": "india_compliance/gst_india/client_scripts/payment_entry.js",
    "Sales Invoice": "india_compliance/gst_india/client_scripts/sales_invoice.js",
    "Purchase Receipt": "india_compliance/gst_india/client_scripts/purchase_receipt.js",
    "Purchase Invoice": "india_compliance/gst_india/client_scripts/purchase_invoice.js",
}

doctype_list_js = {
    "Sales Invoice": "india_compliance/gst_india/client_scripts/sales_invoice_list.js",
}

doc_events = {}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/india_compliance/css/india_compliance.css"
# app_include_js = "/assets/india_compliance/js/india_compliance.js"

# include js, css files in header of web template
# web_include_css = "/assets/india_compliance/css/india_compliance.css"
# web_include_js = "/assets/india_compliance/js/india_compliance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "india_compliance/public/scss/website"

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "india_compliance.utils.jinja_methods",
# 	"filters": "india_compliance.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "india_compliance.install.before_install"
# after_install = "india_compliance.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "india_compliance.uninstall.before_uninstall"
# after_uninstall = "india_compliance.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "india_compliance.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"india_compliance.tasks.all"
# 	],
# 	"daily": [
# 		"india_compliance.tasks.daily"
# 	],
# 	"hourly": [
# 		"india_compliance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"india_compliance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"india_compliance.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "india_compliance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "india_compliance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "india_compliance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"india_compliance.auth.validate"
# ]
