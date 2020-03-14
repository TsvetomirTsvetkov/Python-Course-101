# cancellation_policy.py

from datetime import datetime, timedelta

def validate_conditions(conditions):
	cnt_hours = 0
	list_hours = []

	for elem in conditions:
		if type(elem) != dict:
			raise TypeError('Only elements of type dictionary allowed')
		if len(elem) == 2:
			try:
				hour = elem['hours']
				elem['percent']
			except:
				raise Exception('Invalid key.')

			if hour in list_hours or hour > 24 or hour < 0:
				raise Exception('Value error.')
			
			list_hours.append(hour)
			cnt_hours += 1

		elif len(elem) == 1:
			try:
				elem['percent']
			except:
				raise Exception('Invalid key.')

	if len(conditions) != cnt_hours + 1 :
		raise Exception ('Invalid conditions.')

def ensure_conditions(conditions):
	for elem in conditions:
		if 'hours' not in elem.keys():
			elem['hours'] = 0
	return conditions

def pair_conditions(conditions):
	result = []
	length = len(conditions)
	
	for index in range(0, length-1):
		result.append((conditions[index], conditions[index+1]))

	return result

def get_current_condition(pairs, start, now):
	time = start - now
	time = (int)(time.total_seconds() / 3600)

	for elem in pairs:
		lhs = elem[1]['hours']
		rhs = elem[0]['hours']

		if time > lhs and time <= rhs:
			return elem[1]['percent']
	
	return pairs[0][0]['percent']

def get_cancellation_fee(price, percent):
	return price*(percent/100)

def sort_conditions(conditions):
	return sorted(conditions, key = lambda x: x['hours'], reverse = True)

def cancellation_policy(conditions, price, start, now):
	if now >= start:
		raise Exception('Invalid booking start.')

	validate_conditions(conditions)

	ensured_conditions = ensure_conditions(conditions)

	sorted_conditions = sort_conditions(ensured_conditions)

	paired_conditions = pair_conditions(sorted_conditions)

	current_condition = get_current_condition(paired_conditions, start, now) 

	return get_cancellation_fee(price, current_condition)


def main():
	# Taken from the solution uploaded in the course's repository.
	
	now = datetime.now()
	booking_start = now + timedelta(hours=10)
	price = 1000
	conditions = [
		{'hours': 24, 'percent': 10},
		{'hours': 12, 'percent': 50},
		{'hours': 6, 'percent': 80},
		{'percent': 100}
	]

	result = cancellation_policy(
		conditions,
		price,
		booking_start,
		now
	)
	print(result)

if __name__ == '__main__':
	main()