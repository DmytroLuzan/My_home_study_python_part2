import zipfile
import os

folder_path = 'c:\\Users\\BlackEagle\\PycharmProjects\\MypythonProject\\folder'
zip_path = 'c:\\Users\\BlackEagle\\PycharmProjects\\MypythonProject\\folder\\test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

# my_zip.write('c:\\Users\\BlackEagle\\PycharmProjects\\MypythonProject\\folder\\1.txt', compress_type=zipfile.ZIP_DEFLATED, arcname='1.txt')
# my_zip.write('c:\\Users\\BlackEagle\\PycharmProjects\\MypythonProject\\folder\\1.txt', '1new.txt', compress_type=zipfile.ZIP_DEFLATED)

for folder, subfolders, files in os.walk(folder_path):
    # print(folder, files)
    # print(folder, subfolders, files)
    # print(folder, files)
    for file in files:
        if file == zip_name:    # Режим нужен только в том случае, если созд внутри папок архив, а не рядом с ним
            continue
        # print(os.path.join(folder, file)
        my_zip.write(os.path.join(folder, file),
        os.path.relpath(os.path.join(folder, file), folder_path),
        compress_type=zipfile.ZIP_DEFLATED)


my_zip.close()











