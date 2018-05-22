def parseMeters(s):
	s = str(s)
	if s.find('ft') != -1:
		i = s.find('ft')
		s = str(round(int(s[:i]) * 0.3048, 1)) + 'm'
		return s
	else:  # Assume m
		if s.find('m') != -1:
			return s
		else:
			return s + 'm'

def parseCelcius(s):
	s = str(s)
	if s.find('F') != -1:
		i = s.find('F')
		s = str(round((int(s[:i]) - 32) * 5 / 9, 1)) + 'C'
		return s
	else:  # Assume C
		if s.find('C') != -1:
			return s
		else:
			return s + 'C'

def parseKilos(s):
	s = str(s)
	if s.find('lb') != -1:
		i = s.find('lb')
		s = str(round(int(s[:i]) * 0.453592, 1)) + 'kg'
		return s
	else:  # Assume kg
		if s.find('kg') != -1:
			return s
		else:
			return s + 'kg'
