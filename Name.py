import os


def sort_file(directory):
    files = []

    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            try:
                open_time = os.path.getatime(file_path)
                files.append((file_path, open_time))
            except Exception as e:
                print(f'Error {file_path}:{e}')
    sorted_files = sorted(files, key=lambda x: x[1])

    return sorted_files

#Путь к python_file
directory_path = r'C:\Users\zymer\Desktop\sorted'

sorted_files = sort_file(directory_path)

#Путь к txt
output_file_path = r'C:\Users\zymer\Desktop\sorted.txt'

with open(output_file_path, 'w') as output_file:
    for file_path, open_time in sorted_files:
        output_file.write(f'{file_path} - {open_time}\n')

#Путь к txt
os.startfile('C:\\Users\\zymer\\Desktop\\sorted.txt')

print(f'Perfect save: {output_file_path}')
