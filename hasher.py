import hashlib, zlib, csv, os, sys
import argparse
import subprocess
import difflib


parser = argparse.ArgumentParser(description='Welcome to Hasher!')
parser.add_argument(dest='rehash_value', action='store', nargs='?', help='Rehashes your directory and compares it to your cvs file')
parser.add_argument("--csvfile", "-o", help="Path to output new CSV to", type=str, dest='path_csv', nargs='?')
parser.add_argument("--directory", "-d", help="To be hashed directory", type=str, dest='path_directory', nargs='?')
parser.add_argument("--original", "-c", help="Specify path to original csv file", type=str, dest='original_csv', nargs='?')


args = parser.parse_args()



rootdir = args.path_directory # Dir path
csvdir = args.path_csv
original_csv= args.original_csv
rehash = args.rehash_value


#Rehashing Function

if (str(rehash) == "rehash"):

	def filename_hasher(subdir, file_name):
		full_path = subdir + '/' + file_name
		temp_list = []
		temp_list.append(file_name)
		temp_list.append(os.path.abspath(full_path))
		temp_list.append(hash_file(full_path, hashlib.md5()))
		temp_list.append(hash_file(full_path, hashlib.sha1()))
		temp_list.append(hash_file(full_path, hashlib.sha224()))
		temp_list.append(hash_file(full_path, hashlib.sha256()))
		temp_list.append(hash_file(full_path, hashlib.sha384()))
		temp_list.append(hash_file(full_path, hashlib.sha512()))
		return temp_list


	def hash_file(file_name, _type):
		BUFFER_SIZE = 64 * 1024 #Read 64k at a time to save memory
		hash_type = _type
		with open(file_name, 'rb') as f:
			buffer_s = f.read(BUFFER_SIZE)
			while len(buffer_s) > 0:
				hash_type.update(buffer_s)
				buffer_s = f.read(BUFFER_SIZE)

		hash_in_hex = hash_type.hexdigest()
		
		return hash_in_hex
		
	print os.getcwd() #show current dir

	temp_list = []


	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			temp_list.append(filename_hasher(subdir, file))

	column_header = ['Filename','Path','MD5','SHA1','SHA224','SHA256','SHA384','SHA512']
	with open(csvdir + 'Rehashed'+ '.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows([column_header])
		writer.writerows(temp_list)


	
	with open(csvdir+'Rehashed.csv', 'r') as hosts0:
   		with open(original_csv+'hashed.csv', 'r') as hosts1:
   			print 'compares'
   			diff = difflib.unified_diff(
   				hosts0.readlines(),
	            hosts1.readlines(),
	            fromfile='hosts0',
	            tofile='hosts1',)
   			for line in diff:
   				sys.stdout.write(line)
	            

				

	#subprocess.call([diff csvdir+'Rehashed.csv' original_csv ])



else:


####################################################################

	def filename_hasher(subdir, file_name):
		full_path = subdir + '/' + file_name
		temp_list = []
		temp_list.append(file_name)
		temp_list.append(os.path.abspath(full_path))
		temp_list.append(hash_file(full_path, hashlib.md5()))
		temp_list.append(hash_file(full_path, hashlib.sha1()))
		temp_list.append(hash_file(full_path, hashlib.sha224()))
		temp_list.append(hash_file(full_path, hashlib.sha256()))
		temp_list.append(hash_file(full_path, hashlib.sha384()))
		temp_list.append(hash_file(full_path, hashlib.sha512()))
		return temp_list


	def hash_file(file_name, _type):
		BUFFER_SIZE = 64 * 1024 #Read 64k at a time to save memory
		hash_type = _type
		with open(file_name, 'rb') as f:
			buffer_s = f.read(BUFFER_SIZE)
			while len(buffer_s) > 0:
				hash_type.update(buffer_s)
				buffer_s = f.read(BUFFER_SIZE)

		hash_in_hex = hash_type.hexdigest()
		
		return hash_in_hex
		
	print os.getcwd() #show current dir

	temp_list = []


	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			temp_list.append(filename_hasher(subdir, file))

	column_header = ['Filename','Path','MD5','SHA1','SHA224','SHA256','SHA384','SHA512']
	with open(csvdir + 'hashed'+ '.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows([column_header])
		writer.writerows(temp_list)



###############################################################






