import os

path = input('Enter the full path of the folder: \n>')

dir = [f for f in os.listdir(path) if os.path.isfile(f'{path}/{f}')]

extensions = []

def get_file_extension(f):
    return f.split('.')[len(f.split('.')) - 1]

for file in dir:
    file_extension = get_file_extension(file)
    if file_extension not in extensions:
        extensions.append(file_extension)

for extension in extensions:
    if os.path.isdir(f'{path}/{extension.upper()}') is False:
        os.mkdir(f'{path}/{extension.upper()}')

for file in dir:
    file_extension = get_file_extension(file)
    os.rename(f'{path}/{file}', f'{path}/{file_extension.upper()}/{file}')

print('Files were ordered successfully!')