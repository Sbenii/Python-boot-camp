from collections import defaultdict
d={'a':10}
print(d['a'])
d=defaultdict(lambda:0)
print(d['Wrong key!!'])