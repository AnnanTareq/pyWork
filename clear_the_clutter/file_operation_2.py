import os
class file_operation:
    def __init__(self, name, location, sub_location, types, size):
        self.name = name
        self.location = location
        self.sub_location = sub_location
        self.types = types
        try:                        #this block use to prevent wrong user input
            self.size = int(size)
        except ValueError:
            # self.size = None
            while True:
                try:
                    self.size = int(input('Your given value is wrong, enter again : '))
                    break
                except ValueError:
                    print('Please try again')

    def add_file(self):

        try:
            os.makedirs(f'{self.location}/{self.sub_location}', exist_ok=True)

            i = 0
            while i < self.size:
                f = open(f'{self.location}/{self.sub_location}/{self.name}{i}.{self.types}', 'x')
                f.close()
                i += 1

        except FileExistsError:
            print(f'Already folder: {self.sub_location} had created')
            Path = f'{self.location}/{self.sub_location}'
            if os.path.exists(Path):
                file_list = os.listdir(Path)    # go to the file and read all the files name
                specific_file_lst = []  # Store particular file
                specific_file_size = 0  # find particular files size
                for i in file_list:
                    if self.types in i:
                        specific_file_lst.append(i)
                        specific_file_size += 1

                if specific_file_size < self.size:  # work when folder contains files
                    last = specific_file_lst[-1].split(f'.{self.types}')
                    # print('last == ', last)
                    val = last[0][-1]   # store last created files number
                    lower_limit = int(val) + 1  # already existed files next number
                    while lower_limit < self.size:
                        print(f'creating rest of {self.size - lower_limit} the files')
                        f = open(f'{self.location}/{self.sub_location}/{self.name}{lower_limit}.{self.types}', 'x')
                        f.close()
                        lower_limit += 1
                elif specific_file_size >= self.size:
                    print('File creation unsuccessful because your desired file creating size is equal or less than existed file')




class file_operation_delete(file_operation):
    def __init__(self, name, location, sub_location, types, size):
        super().__init__(name, location, sub_location, types, size)
        # self.sequence = sequence

    def delete_file(self, sequence):
        Path = os.path.join(self.location, self.sub_location)  # concatenate path
        if os.path.exists(Path):
            os.remove(f'{Path}/{self.name}{sequence}.{self.types}')
            print(f'{self.name}{sequence}.{self.types} removed successfully!!!')
        else:
            print('Not found!')

    def delete_all_files(self):
        Path = os.path.join(self.location, self.sub_location)
        lst = os.listdir(Path)
        i = 0
        while i < len(lst):
            os.remove(f'{Path}/{lst[i]}')
            i += 1
        else:
            permission = input('Do you want to delete empty folder? write "yes" : ')
            if permission.lower() == 'yes':
                # os.remove(Path)
                os.rmdir(Path)  # No need to handle error here, because while this block is executing, that time this should be empty
                # shutil.rmtree(Path, ignore_errors=True)

    def rename_files(self, new_name, old_file_type):
        Path = os.path.join(self.location, self.sub_location)
        files_lst = os.listdir(Path)
        # file_type = input('What type of files do you want to make order? ')
        # desired_file_lst = list()
        # self.types = file_type

        i = 0
        for item in files_lst:
            if old_file_type in item:
                # desired_file_lst.append(item)
                os.rename(f'{Path}/{item}', f'{Path}/{new_name}{i}.{old_file_type}')
                i += 1
        print('Done!!!')


while True:
    question = input('What you want to do?\n 1. add \n 2. delete \n 3. Rename \n 4. exit \n')
    if question == '1' or question.lower() == 'add':
        name = input('Please enter FILES name: ')
        folder_name = input('Please enter FOLDER name : ')
        sub_folder_name = input('Please enter sub folder name : ')
        extension_name = input('Enter files type : ')
        size = input('Enter how many files you want to create : ')
        fo = file_operation(name, folder_name, sub_folder_name, extension_name, size)
        fo.add_file()
    elif question == '2' or question == 'delete':
        name = input('Please enter delete FILES name: ')
        folder_name = input('Please enter FOLDER name : ')
        sub_folder_name = input('Please enter sub folder name : ')
        extension_name = input('Enter files type : ')

        ques = input('Do you want to delete all files then write "YES" or press any key : ')

        if ques.lower == 'yes':
            del_files = file_operation_delete(name, folder_name, sub_folder_name, extension_name, size = 0)
            del_files.delete_all_files()

        else:
            seq = input('Enter files sequence number : ')
            del_file = file_operation_delete(name, folder_name, sub_folder_name, extension_name, size=0)
            del_file.delete_file(seq)

    elif question == '3' or question == 'rename':
        new_file_name = input('Enter new file name : ')
        type_of_file = input('Enter what types of file you want to edit EXAMPLE: .txt : ')
        loc = input('Enter location name : ')
        sub_loc = input('Enter sub location name : ')

        d = file_operation_delete(name='', location=loc, sub_location=sub_loc, types='', size=0)
        d.rename_files(new_file_name, type_of_file)

    elif question == '4' or question == 'exit':
        break
