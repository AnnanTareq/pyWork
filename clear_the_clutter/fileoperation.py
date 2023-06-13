import os
import shutil

question = input('What functionality do want to use?\n 1. add \n 2. delete \n ')

if question == '1':
    location = 'my files'
    req = input('What kind of file want to create?\n 1. .png \n 2. .txt \n 3. .jpg \n ')
    sub_folder = input('Enter folder name : ')  # takes an input and create a folder

    if req == '1':
        extension = '.png'
        limit = None
        try:
            os.makedirs(f'{location}/{sub_folder}', exist_ok=True)

            try:
                limit = int(input('How many files do you want to create? '))
            except ValueError:
                while limit == None:
                    try:
                        limit = int(input('Enter value again : '))
                    except ValueError:
                        print('Please try again!')

            i = 0
            while i < limit:
                print('from try block')
                f = open(f'{location}/{sub_folder}/Image{i}{extension}', 'x')
                f.close()
                i += 1

        except FileExistsError:
            print(f'Already folder: {sub_folder} had created')
            Path = f'{location}/{sub_folder}'
            if os.path.exists(Path):
                file_list = os.listdir(Path)
                specific_file_lst = []  # Store particular file
                specific_file_size = 0  #find particular files size
                for i in file_list:
                    if extension in i:
                        specific_file_lst.append(i)
                        specific_file_size += 1

                if specific_file_size < limit:  # work when folder contains files
                    last = specific_file_lst[-1].split('.png')
                    # print('last == ', last)
                    val = last[0][-1]
                    lower_limit = int(val) + 1
                    while lower_limit < limit:
                        print(f'creating rest of {limit - lower_limit} the files')
                        f = open(f'{location}/{sub_folder}/Image{lower_limit}{extension}', 'x')
                        f.close()
                        lower_limit += 1
                elif specific_file_size >= limit:
                    print(
                        'File creation unsuccessful because your desired file creating size is equal or less than existed file')

    elif req == '2':
        extension = '.txt'
        limit = None
        try:
            os.makedirs(f'{location}/{sub_folder}', exist_ok=True)
            try:
                limit = int(input('How many TEXT files do you want to create? '))
            except ValueError:
                while limit == None:
                    try:
                        limit = int(input('Enter value again : '))
                    except ValueError:
                        print('Please try again!')

            i = 0
            while i < limit:
                f = open(f'{location}/{sub_folder}/Text_file{i}{extension}', 'x')
                f.close()
                i += 1

        except FileExistsError:
            print(f'Already folder: {sub_folder} had created')
            # print(location, sub_folder)
            Path = f'{location}/{sub_folder}'
            if os.path.exists(Path):
                file_list = os.listdir(Path)
                particular_file = []
                pf_size = 0
                for item in file_list:
                    if extension in item:
                        particular_file.append(item)
                        pf_size += 1

                if pf_size < limit:  # work when folder contains files
                    last = particular_file[-1].split('.txt')
                    val = last[0][-1]
                    lower_limit = int(val) + 1
                    while lower_limit < limit:
                        print(f'creating rest of {limit - lower_limit} the files')
                        f = open(f'{location}/{sub_folder}/Text_file{lower_limit}{extension}', 'x')
                        f.close()
                        lower_limit += 1
                elif len(file_list) >= limit:
                    print(
                        'File creation unsuccessful because your desired file creating size is equal or less than existed file')

    elif req == '3':
        extension = '.jpg'
        limit = None
        try:
            os.makedirs(f'{location}/{sub_folder}', exist_ok=True)
            try:
                limit = int(input('How many JPG files do you want to create? '))
            except ValueError:
                while limit == None:
                    try:
                        limit = int(input('Enter value again : '))
                    except ValueError:
                        print('Please try again!')

            i = 0
            while i < limit:
                f = open(f'{location}/{sub_folder}/JPG_file{i}{extension}', 'x')
                f.close()
                i += 1

        except FileExistsError:
            print(f'Already folder: {sub_folder} had created')
            Path = f'{location}/{sub_folder}'
            if os.path.exists(Path):
                file_list = os.listdir(Path)
                specific_files = []
                sf_size = 0
                for item in file_list:
                    if extension in item:
                        specific_files.append(item)
                        sf_size += 1

                if sf_size < limit:  # work when folder contains files
                    last = specific_files[-1].split('.jpg')
                    val = last[0][-1]   # fethch the data to find what is the last number
                    lower_limit = int(val) + 1
                    while lower_limit < limit:
                        print('creating rest of the files')
                        f = open(f'{location}/{sub_folder}/JPG_file{lower_limit}{extension}', 'x')
                        f.close()
                        lower_limit += 1
                elif len(file_list) >= limit:
                    print('File creation unsuccessful because your desired file creating size is equal or less than existed file')


elif question == '2':
    location = 'my files'
    sub_folder = input('Enter your folder name to delete files from : ')
    Path = os.path.join(location, sub_folder)  # concatenate path
    if os.path.exists(Path):
        perm = input('Do you want to delete all the files or one by one? If want to delete all then press "1" : ')
        if perm == '1':
            lst = os.listdir(Path)
            i = 0
            while i < len(lst):
                os.remove(f'{Path}/{lst[i]}')
                i += 1
            else:
                permission = input('Do you want to delete empty folder? write "yes" : ')
                if permission.lower() == 'yes':
                    # os.remove(Path)
                    os.rmdir(Path)  #No need to handle error here, because while this block is executing, that time this should be empty
                    # shutil.rmtree(Path, ignore_errors=True)
        else:
            rmv_file = input('Removing file name: ')
            val = input('Which types of file want to delete? \n 1. .png \n 2. .txt \n 3. .jpg \n')
            if val == '1':
                ext = '.png'
                os.remove(f'{Path}/{rmv_file}{ext}')
            elif val == '2':
                ext = '.txt'
                os.remove(f'{Path}/{rmv_file}{ext}')
            elif val == '3':
                ext = '.jpg'
                os.remove(f'{Path}/{rmv_file}{ext}')
