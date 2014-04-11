#!/usr/bin/python

import sys
import Queue
import threading

pool = []

def factors(n):
	x = []
	while n%2 == 0:
		x.append(2)
		n = n/2
	for i in range(3,n+1,2):
		if n%i == 0:
			x.append(i)
			n = n/i
	if n > 2:
		x.append(n)
	return x

queue = Queue.Queue()
out_queue = Queue.Queue()


class ThreadedFactorizer(threading.Thread):
	def __init__(self,queue, out_queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.out_queue = out_queue

	def run(self):
		while True:
			next_ = self.queue.get()
			tag, num = next_.split(' ')
			facs = factors(long(num))
			self.out_queue.put(dict([(next_ ,facs)]))
			self.queue.task_done()

def main():
	if len(sys.argv) < 3:
		exit()

	try:
		num_workers = int(sys.argv[2])
	except:
		exit()

	x = sys.stdin.readlines()

	for item in x:
		pool.append(item.strip())

	for i in range(num_workers):
		t = ThreadedFactorizer(queue, out_queue)
		t.setDaemon(True)
		t.start()

	for item in pool:
		queue.put(item)

	queue.join()

	while not out_queue.empty():
		item = out_queue.get()
		for key, value in item.iteritems():
			print "%s =" %key,
			for i in value:
				print i,
			print ""
		out_queue.task_done()

main()
