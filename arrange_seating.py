# Ray Riga - Lead Data Engineer application
import json

guest_list = [
'a',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'l',
'm',
'n',
]

planner_preferences = [
	{
		"preference": "avoid",
		"guests": ["a", "b"]
	},
	{
		"preference": "avoid",
		"guests": ["c", "d"]
	},
	{
		"preference": "avoid",
		"guests": ["e", "f"]
	},
	{
		"preference": "avoid",
		"guests": ["g", "h"]
	},

	{
		"preference": "pair",
		"guests": ["i", "j"]
	},
	{
		"preference": "pair",
		"guests": ["k", "l"]
	},
	{
		"preference": "pair",
		"guests": ["m", "n"]
	},]


num_tables = 2

def arrange_seating(num_tables, guest_list, planner_preferences):
	
	tables = {}
	table_num = 0
	while num_tables:
		table_num = table_num + 1
		tables[f'table_{table_num}'] = []
		num_tables = num_tables - 1
	pair_prefs = [p for p in planner_preferences if p['preference'] is 'pair']
	avoid_prefs = [p for p in planner_preferences if p['preference'] is 'avoid']
	guests_with_prefs_set = set()
	for pref in planner_preferences:
		for guest in pref['guests']:
			guests_with_prefs_set.add(guest)
	guests_with_no_prefs = []
	for guest in guest_list:
		if guest not in guests_with_prefs:
			guests_with_no_prefs.append(guest)
	guests_with_prefs = list(guests_with_prefs_set)

	current_table = 1
	for pref in pair_prefs:
		# seat pair at tables round robin
		if current_table > num_tables:
			current_table = 1
		tables[f'table_{current_table}'].extend(pref['guests'])
		current_table = current_table + 1

	for pref in avoid_prefs:
		# seat pair at tables round robin
		if current_table > num_tables:
			current_table = 1
		tables[f'table_{current_table}'].extend(pref['guests'])
		current_table = current_table + 1

	for guest in guests_with_no_prefs:
		# seat one at table round robin
		if current_table > num_tables:
			current_table = 1
		tables[f'table_{current_table}'].append(guests)

	return json.dumps(tables)

def test_arrange_seating:
	result_object = json.loads(arrange_seating(num_tables, guest_list, planner_preferences))

def assure_prefs_at_table(table):
	# on a per table basis, confirm that all prefs are respected by going through each
	# guest and "looking ahead"

