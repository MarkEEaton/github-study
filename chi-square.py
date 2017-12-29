import json
from scipy.stats import chisquare

with open('processedlanguages.json', 'r') as f:
	data = json.loads(f.read())

ll = data['librarians']
rl = data['randoms']

librarians_languages = [
	ll['JavaScript'],
	ll['Python'],
	ll['Ruby'],
	ll['HTML'],
	ll['PHP'],
	ll['CSS'],
	ll['Java'],
	ll['Shell'],
	ll['C++'],
	ll['C'],
	ll['R'],
	ll['C#']]

randoms_languages = [
	rl['JavaScript'],
	rl['Python'],
	rl['Ruby'],
	rl['HTML'],
	rl['PHP'],
	rl['CSS'],
	rl['Java'],
	rl['Shell'],
	rl['C++'],
	rl['C'],
	rl['R'],
	rl['C#']]

print(chisquare(librarians_languages, f_exp=randoms_languages))
