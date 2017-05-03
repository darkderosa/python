import zipfile
from common_zip import ZFile
import os

class Utils:
	"""Common functions class."""

	
	def zip_create(self, zfile, files):
		"""
		Create files to zfile.
		"""
		
		z = ZFile(zfile, 'w')
		z.addfiles(files)
		z.close()

	def zip_extract(self, zfile, path):
		"""
		Unzip the file to target path.
		If the path is empty, unzip to current path.
		"""

		z = ZFile(zfile)
		z.extract_to(path)
		z.close()

	def get_all_files(self, path, suffixes=[]):
		"""
		Get all files from target path, and those files will end with one of suffixes.
		Suffixes should like ['.txt', '.py']. If it's empty, will get all type of files.
		"""

		files = []
		#parent path, current folder(no path), filenames(no path)
		for parent, dirnames, filenames in os.walk(path):
			for filename in filenames:
				if len(suffixes) <= 0 or os.path.splitext(filename)[1] in suffixes:
					files.append(os.path.join(parent, filename))
					#print("the full name of the file is:" + os.path.join(parent,filename))

		return files

utils = Utils()
files = utils.get_all_files('Build')
utils.zip_create('temp.zip', files)

