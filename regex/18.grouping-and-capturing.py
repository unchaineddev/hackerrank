# https://www.hackerrank.com/challenges/alternative-matching/problem

Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)([a-z]|[A-Z])+$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())