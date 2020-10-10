import os.path
from solution import File

def main():
	path_to_file = 'some_filename'
	print("Is path exists: ", os.path.exists(path_to_file))

	file_obj = File(path_to_file)
	print("Is path exists: ", os.path.exists(path_to_file))
	print(file_obj.read())

	file_obj.write('some text')
	print(file_obj.read())

	file_obj.write('other text')
	print(file_obj.read())

	file_obj_1 = File(path_to_file + '_1')
	file_obj_2 = File(path_to_file + '_2')
	file_obj_1.write('line 1\n')
	file_obj_2.write('line 2\n')

	new_file_obj = file_obj_1 + file_obj_2

	print("Is instance: ", isinstance(new_file_obj, File))

	print("Print new_file_obj: \n",new_file_obj)

	print("Iter: ")
	for line in new_file_obj:
		print(ascii(line))  

if __name__ == '__main__':
	main()

