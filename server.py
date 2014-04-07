#!/usr/bin/python

from multiprocessing import Process, Pipe
import Queue
import random
import string

class Factorizer():
	def __init__(self,p,t,addr):
		self.workers = p
		self.threadsperworker = t
		self.serveraddr = addr
		self.__WorkerList = dict(workerid='itemsprocesed/processhandle/pipefd')
		self.start()
		
		
	def __idgenerator(self):
		__pool = string.letters + string.digits
		self.new = 2
		return ''.join(random.choice(__pool) for i in xrange(32)) 
		
				
	def __workerprocess(self,fd):
		###################
		###################
		__inqueue = Queue.queue()
		__outqueue = Queue.queue()
		print 'worker'
		
	def __server(self):
		###################
		###Start a server##
		###################
		print 'server'
		
	def start(self):
		for i in range(self.workers):
			__p, __c = Pipe(True)
			__process = Process(target=self.__workerprocess, args=(__c,))
			__process.start()
			self.__WorkerList[self.__idgenerator()] = [0, __process, __p]	
		print self.__WorkerList
		
if __name__ == '__main__':
	f = Factorizer(2,3,4)
	
