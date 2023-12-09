# https://codeforces.com/contest/1907/problem/B
n, result = int(input()), []
for _ in range(n):
    string, ignore_lowercase, ignore_uppercase, answer = input(), 0, 0, []
    for i in range(len(string) - 1, -1, -1):
    	s = string[i]
    	if s == 'b':
    		ignore_lowercase += 1
    	elif s == 'B':
    		ignore_uppercase += 1
    	else:
    		if s.isupper() and ignore_uppercase > 0:
    			ignore_uppercase -= 1
    		elif not s.isupper() and ignore_lowercase > 0:
    			ignore_lowercase -= 1
    		else:
    			answer.append(s)
    answer.reverse()
    result.append("".join(answer))
print(*result, sep='\n')
