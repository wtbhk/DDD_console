import urllib
import urllib2
import re

class Archive:
	def __init__(self, url):
		self.url = url

	def getAllMonth(self):
		html = self.request({'lite':2})
		arr = re.findall(r'data-month="([0-9]*)"', html)
		return arr

	def request(self, data=''):
		data = urllib.urlencode(data)
		r = urllib2.urlopen(self.url, data)
		return r.read()

	def getArchiveByMonth(self, month):
		html = self.request({'lite':1, 'month':month})
		arr = re.findall(r'<a class="post-meta" target="_blank" href="(.*)">', html)
		return arr

	def getAllArchive(self):
		month = self.getAllMonth()
		arr = {}
		for i in month:
			arr[i] = self.getArchiveByMonth(i)
		return arr

if __name__ == '__main__':
	a = Archive('http://1169028488.diandian.com/archive')
	print a.getAllMonth()
	print a.getArchiveByMonth(201407)
	print a.getAllArchive()