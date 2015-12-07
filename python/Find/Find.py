'''
	Author: Jarrod McEvers
	  File: find.py
	  Desc: A linux-like find command that looks for files that
			match a given pattern
'''
import os
import logging

class Find:
	searchFor = ''
	searchCount = 0
	filesSearched = 0
	filepath = ''
	matches = []

	def __init__(self, searchFor, filepath):
		self.setSearchFor(searchFor)
		self.setFilepath(filepath)
	
	def getSearchFor(self):
		return self.searchFor

	def setSearchFor(self, searchFor):
		self.searchFor = searchFor.lower()
	
	def getFilepath(self):
		return self.filepath
	
	def setFilepath(self, filepath = '.'):
		# if path given is real, use it
		# else, use the current directory
		if os.path.exists(filepath):
			self.filepath = filepath
		else:
			self.filepath = '.'
	
	def getMatches(self):
		return self.matches

	def getSearchCount(self):
		return self.searchCount
	
	def getFilesSearched(self):
		return self.filesSearched

	def find(self, filepath):
		try:
			filesInDirectory = os.listdir(filepath)
		except:
			filesInDirectory = None
			logging.info('Could not retrieve file directory contents for ' + filepath)
			
		if filesInDirectory != None:
			for filename in filesInDirectory:
				self.filesSearched += 1
				path = os.path.join(filepath, filename)
				if self.searchFor in path.lower():
					self.matches.append(path)
					self.searchCount += 1
					print path
				if os.path.exists(path) and os.path.isdir(path):
					self.find(path)
