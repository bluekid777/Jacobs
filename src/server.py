#!/usr/bin/python

from multiprocessing import Process, Pipe
import Queue
import random
import string
import select
import socket
import sys
import threading


def generator(self):
    __pool = string.letters + string.digits
    return ''.join(random.choice(__pool) for i in xrange(32))


class Server:
    def __init__(self):
        self.host = ''
        self.port = 50000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except socket.error, (value, message):
            if self.server:
                self.server.close()
            print "Could not open socket: " + message
            sys.exit(1)

    def run(self):
        self.open_socket()
        input = [self.server, sys.stdin]
        running = 1
        while running:
            inputready, outputready, exceptready = select.select(input, [], [])

            for s in inputready:

                if s == self.server:
                    # handle the server socket
                    c = ClientHandler(self.server.accept())
                    c.start()
                    self.threads.append(c)

                elif s == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = 0

        # close all threads

        self.server.close()
        for c in self.threads:
            c.join()


class ClientHandler(threading.Thread):
    def __init__(self, (client, address)):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024

    def run(self):
        running = 1
        while running:
            data = self.client.recv(self.size)
            print data
            if data:
                self.client.send(data)
            else:
                self.client.close()
                running = 0


class Worker:
    def __init__(self, id, threads, infd, outfd):
        self.counter = 0
        self.id = id
        self.threads = threads
        self.fdin = infd
        self.fdout = outfd
        self.inqueue = Queue.Queue()
        self.outqueue = Queue.Queue()

    def listener(self):
        while True:
            try:
                next = self.fdin.recv()
                self.inqueue.put(next)
                self.counter += 1
            except:
                pass

    def reporter(self):
        while True:
            result = self.outqueue.get()
            try:
                self.fdout.send(result)
                self.outqueue.task_done()
            except:
                pass

    def processor(self):






class Factorizer():
    def __init__(self, p, t, addr):
        self.workers = p
        self.threadsperworker = t
        self.serveraddr = addr
        self.__WorkerList = dict(workerid='itemsprocesed/processhandle/pipefd')
        self.start()


    def __workerprocess(self, fd):
        ###################
        ###################
        __inqueue = Queue.Queue()
        __outqueue = Queue.Queue()
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
            self.__WorkerList[generator()] = [0, __process, __p]
        print self.__WorkerList


if __name__ == '__main__':
    s = Server()
    s.run()
	
