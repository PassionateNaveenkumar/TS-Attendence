# Copyright (c) 2013, naveen and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data
def get_columns(filters):
	columns = [
		{
			"label":("Employee_Name"),
			"fieldtype": "Data",
			"fieldname": "employee_name"
		},
		{
			"label": ("Employee_Id"),
			"fieldtype": "Data",
			"fieldname": "employee_id"
		},
		{
			"label":("Date"),
			"fieldtype": "Date",
			"fieldname": "date"
		}

	]
	return columns
def get_conditions(filters):
	conditions = {}

	if filters.date:
		conditions["date"] = filters.date
		return conditions
def get_data(filters):

	data = []
	conditions = get_conditions(filters)
	attendence = frappe.db.get_all("TS Attendence", fields=["employee_name", "employee_id", "date"],
		filters=conditions, order_by='employee_name')

	for d in attendence:
		row = {"employee_name": d.employee_name, "employee_id": d.employee_id, "date": d.date}

		data.append(row)

	return data