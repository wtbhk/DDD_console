from archive import Archive
from download import Download
import os
import re

def print_(str):
	print str

print 'Loading...'

if not os.path.exists('./DDD') : os.makedirs('./DDD')
d = Download()
config = open('./config.txt')
blogger = []
while True:
	line = config.readline()
	if not line:
		break
	blogger.append(line[:-1])

for i in blogger:
	if not os.path.exists('./DDD/'+i) : os.makedirs('./DDD/'+i)
	all_ids = os.listdir('./DDD/' + i)
	a = Archive('http://' + i + '.diandian.com/archive')
	d.reg_callback(print_)
	archives = a.getAllArchive()
	for j in archives:
		for k in archives[j]:
			print k
			try:
				if re.search(r'post\/.*\/(.*)', k).group(1) not in all_ids:
					d.add(k)
			except:
				print 'err:'+k


d.start()




'''
a = Archive('http://1169028488.diandian.com/archive')
d = Download()
d.reg_callback(print_)
archives = a.getAllArchive()
for i in archives:
	for j in archives[i]:
		d.add(j)

d.start()
'''
