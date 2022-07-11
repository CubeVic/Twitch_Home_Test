import time


def get_current_date():
	t = time.localtime()
	current_time = time.strftime("%d_%B_%Y_%H:%M:%S", t)
	return current_time


def clean_user_name(string_to_clean):
	name = []
	for c in string_to_clean:
		if c == "_":
			name.append(c)
		elif c.isascii() and c.isalnum():
			name.append(c)
	return "".join(name)

