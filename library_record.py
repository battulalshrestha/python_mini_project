
'''print("\n Library recorded system:")
    print("Noted the person name who have been entered:")
    print("Please note the name of the material each person brings when they come to the library.")
    print("Noted the time in which person to be entered:")
    print("Write the book name where person used to read while stay in library:")
    print("Noted the time how long person used to read this book while in library:")'''

'''print("\nLibrary Recording System:")
 print("Please note the following details for each person entering the library:")
 print("1. Record the name of each person as they enter.")
 print("2. Kindly note the name of the material each person brings with them.")
 print("3. Record the exact time of entry for each person.")
 print("4. Write down the title of the book the person chooses to read during their stay.")
 print("5. Note the duration of time the person spends reading this book while in the library.")
 print("6. Please note the time each person exits the library.")'''
'''
import json
def data_load():
  try:
    with open('library.txt','r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []
def save_data_load_help(vidios):
  with open('library.txt','w') as file:
     json.dump(vidios,file)

def list_all_record(vidios):
  for index, audio in enumerate(vidios, start=1):
    print('\n')
    print("*" * 90)
    print(f"{index}) {audio['name']}, material: {audio['material_name']}, entry name: {audio['entry_time']}, get book: {audio['get_book']}, duration time: {audio['duration_time']}, exit time: {audio['exit_time']}")
    print('\n')
    print('@' * 90)

def add_all_record(vidios):
  name = input("Enter the name of person as they enter the library:")
  material_name = input("Enter the name of material each person bring with them:")
  entry_time = input("Enter the exact time of entry for each person:")
  get_book = input("Enter the book title which the person chooses to read during their stay:")
  duration_time = input("Enter the duration of time the person spends reading this book while in the library:")
  exit_time = input("Enter the exit time o each person from the library:")
  vidios.append({'name':name,'material_name':material_name,'entry_time':entry_time,'get_book':get_book,'duration_time':duration_time,'exit_time':exit_time})
  save_data_load_help(vidios)
def update_all_vidio(vidios):
  list_all_record(vidios)
  index = int(input("Enter the recorded number to be uodated:"))
  if 1<=index<=len(vidios):
    name = input("Enter the name new of person as they enter the library:")
    material_name = input("Enter the new name of material each person bring with them:")
    entry_time = input("Enter the new exact time of entry for each person:")
    get_book = input("Enter the new book title which the person chooses to read during their stay:")
    duration_time = input("Enter the new duration of time the person spends reading this book while in the library:")
    exit_time = input("Enter the new exit time o each person from the library:")
    vidios[index-1] = {'name':name,'material_name':material_name,'entry_time':entry_time,'get_book':get_book,'durationtime':duration_time,'exittime':exit_time}
    save_data_load_help(vidios)
  else:
    print("Invalid index selected")   
def delete_all_vidio(vidios):
  list_all_record(vidios)
  index = int(input("Enter the record number to be deleted:"))
  if 1<= index<= len(vidios):
    del vidios[index-1]
    save_data_load_help(vidios)
  else:
    print("Invalid index choosed")


def main():
 vidios = data_load()
 while True:
  print("\nLibrary Recording System:")
  print("1) List of all detail record of library")
  print('2) Add the all detail of record list')
  print('3) update the  detail of record list')
  print('4) Delete the detail of record list')
  print('5) Exit') 
  choice = input("Enter the input choice:")
  match choice:
   case '1':
    list_all_record(vidios)
   case '2':
    add_all_record(vidios)
   case '3': 
    update_all_vidio(vidios)
   case '4':
    delete_all_vidio(vidios)
   case _:
    break
if __name__ == "__main__":
   main()
'''

import json

def data_load():
    try:
        with open('library.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_load_help(videos):
    with open('library.txt', 'w') as file:
        json.dump(videos, file)

def list_all_record(videos):
    for index, record in enumerate(videos, start=1):
        print('\n')
        print("*" * 90)
        print(f"{index}  {record['name']}, material: {record['material_name']}, entry time: {record['entry_time']}, get book: {record['get_book']}, duration time: {record['duration_time']}, exit time: {record['exit_time']}")
        print('\n')
        print('@' * 90)

def add_all_record(videos):
    name = input("Enter the name of person as they enter the library: ")
    material_name = input("Enter the name of material each person brings with them: ")
    entry_time = input("Enter the exact time of entry for each person: ")
    get_book = input("Enter the book title which the person chooses to read during their stay: ")
    duration_time = input("Enter the duration of time the person spends reading this book while in the library: ")
    exit_time = input("Enter the exit time of each person from the library: ")
    videos.append({'name': name, 'material_name': material_name, 'entry_time': entry_time, 'get_book': get_book, 'duration_time': duration_time, 'exit_time': exit_time})
    save_data_load_help(videos)

def update_all_video(videos):
    list_all_record(videos)
    index = int(input("Enter the recorded number to be updated: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new name of person as they enter the library: ")
        material_name = input("Enter the new name of material each person brings with them: ")
        entry_time = input("Enter the new exact time of entry for each person: ")
        get_book = input("Enter the new book title which the person chooses to read during their stay: ")
        duration_time = input("Enter the new duration of time the person spends reading this book while in the library: ")
        exit_time = input("Enter the new exit time of each person from the library: ")
        videos[index-1] = {'name': name, 'material_name': material_name, 'entry_time': entry_time, 'get_book': get_book, 'duration_time': duration_time, 'exit_time': exit_time}
        save_data_load_help(videos)
    else:
        print("Invalid index selected")

def delete_all_video(videos):
    list_all_record(videos)
    index = int(input("Enter the record number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_load_help(videos)
    else:
        print("Invalid index chosen")

def main():
    videos = data_load()
    while True:
        print("\nLibrary Recording System:")
        print("1) List all detail records of the library")
        print('2) Add all details to the record list')
        print('3) Update the detail of the record list')
        print('4) Delete the detail of the record list')
        print('5) Exit')
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                list_all_record(videos)
            case '2':
                add_all_record(videos)
            case '3':
                update_all_video(videos)
            case '4':
                delete_all_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice, please enter a number between 1 and 5")

if __name__ == "__main__":
    main()
