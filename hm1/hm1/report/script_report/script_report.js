// Copyright (c) 2016, naveen and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Script Report"] = {
	"filters": [
		{
		fieldname:"date",
		label: __("Date"),
		fieldtype: "Date",
		default: frappe.defaults.get_user_default("date")
	}
	]
};
