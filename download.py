import urllib
import urllib2
import Queue
import re
import time
import threading
import os


class Download:
	def __init__(self):
		self.queue = Queue.Queue()
		self.stop_flag = False

	def start(self):
		self.stop_flag = False
		for i in range(10):
			threading.Thread(target = self.download).start()

	def add(self, url):
		self.queue.put(url)

	def stop(self):
		self.stop_flag = True
				
	def isEmpty(self):
		return self.queue.empty()

	def reg_callback(self, func):
		self.callback = func

	def download(self):
		while True:
			if self.stop_flag or self.isEmpty() : break
			url = ''
			try:
				url = self.queue.get(False)
			except:
				time.sleep(1)
			try:
				if url:
					if __name__ == '__main__' : print url
					base_path = './DDD/' + re.search(r'(\w*)\.', url).group(1) + '/' + re.search(r'post\/.*\/(.*)', url).group(1) + '/'
					#base_path = './DDD/blogger/id/'
					html = urllib.urlopen(url).read()
					if __name__ == '__main__' : print html
					imgs_ = re.findall(r'"(http:\/\/m[0-9]\.img\.srcdd\.com(\/\w*)*\.[a-zA-Z]{3,4})"', html)
					imgs = []
					for i in imgs_:
						imgs.append(i[0])
					if __name__ == '__main__' : print imgs
					if not os.path.exists(base_path) : os.makedirs(base_path)
					for i in imgs:
						if __name__ == '__main__' : print i
						path = base_path + re.search(r'([0-9a-zA-Z]{32}_.*\..*)', i).group(0)
						if __name__ == '__main__' : print path
						f = file(path, 'wb')
						f.write(urllib.urlopen(i).read())
						f.close()
						self.callback(str(threading.currentThread().getName()) + '|' + str(self.queue.qsize()) + '|' + path)
			except:
				pass
		

if __name__ == '__main__':
	def foo():
		pass
	d = Download()
	d.reg_callback(foo)
	arr = [
		'http://1169028488.diandian.com/post/2013-08-03/40052930842', 
		'http://1169028488.diandian.com/post/2013-08-03/40053726567', 
		'http://1169028488.diandian.com/post/2013-08-03/40052540015', 
		'http://1169028488.diandian.com/post/2013-08-03/40053310095', 
		'http://1169028488.diandian.com/post/2013-08-03/40053725424', 
		'http://1169028488.diandian.com/post/2013-08-03/40052466937', 
		'http://1169028488.diandian.com/post/2013-08-03/40053090755']
	for i in arr:
		d.add(i)
	d.start()
	time.sleep(10)
	d.stop()
