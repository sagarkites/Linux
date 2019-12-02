import urllib2
'''Reads the data from the url and prints the Response'''
a = urllib2.urlopen('site')
b = a.read()
