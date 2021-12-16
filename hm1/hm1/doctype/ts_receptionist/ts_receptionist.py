# Copyright (c) 2021, naveen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TS_Receptionist(Document):
	pass
@frappe.whitelist(allow_guest=True)
def nav():
	name=frappe.get_all("TS_Receptionist")
	return name


	#thirvusoft/frappe-bench/apps/hm1/hm1/hm1/doctype/ts_receptionist/ts_receptionist.py
	#hm1/hm1/doctype/ts_receptionist/ts_receptionist
	#192.168.1.120