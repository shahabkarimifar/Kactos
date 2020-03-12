# this file contains all the functions that i need them in my views and i write them myself
# sasha + utility => sutility
def get_client_ip(user_info):
	"""
		takes request variable as argument and returns client ip
	"""
	x_forwarded_for = user_info.META.get('HTTP_X_RORWARDED_FOR')

	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = user_info.META.get('REMOTE_ADDR')

	return ip


def pdf_verification(file_address):
	"""
		take file address and check file to be a real pdf file
		this function using python-magic module and from_file(as check_file) function from this module
	"""
	test_result = check_file(file_address)
	test_result = test_result.split(' ')[0]
	if test_resutl == 'PDF':
		return True
	else:
		return False