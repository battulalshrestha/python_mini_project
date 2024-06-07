'''function = open('hello.txt','w')
try:
    function.write("hello nishan how are you now . are you passionately laearning django nice keep it up")
finally:
    function.close()
with open('hello.txt','w') as function:
    function.write("hello nishan how are you now . are you passionately laearning django nice keep it up")'''
'''json can be use  as store and transfer the data 
load data - data load in the format of string i.e key value pair mapping {} 
and is similar to dictionary
json .load() takes the file object . a json object has the key value pair .the key are the string
and the value pair may be in json type
syntax : json.load(file_object)

json dump 
json module in the python provide the method called as dump() . which conve
rt the python object in to the json and it is slight varient of dump() method 
enumerate in python 
for eg:
 list = [{'name': 'nishan', 'clz': 'ncit'}, {'home': 'gorkha', 'lives': 'chysal'}]

'''


'''import json
def load_data():
  try: 
    with open('youtube.txt','r') as file:
      test = json.load(file)
      #print(type(test))
      return test

  except FileNotFoundError:
    return []
def save_data_helper(vidioharu):
  with open("youtube.txt",'w') as file:
    json.dump(vidioharu,file)

def playlist_all_vidio(vidioharu):
   for index, vidio in enumerate(vidioharu,start=1):
     print('\n')
     print('@' * 90)
     print(f'{index}){vidio['name']} ,Duration:{vidio['time']}')
     print('\n')
     print('@' * 90)
def get_vidios(vidioharu):
    
    name= input("Enter the youtube  vidio name: ")
    time = input("Enter the uploaded youtube vidio time: ")
    vidioharu.append({'name':name,'time':time})
    save_data_helper(vidioharu)

def post_vidios(vidioharu):
  playlist_all_vidio(vidioharu)
  index = int(input("Enter the vidio number to be post:"))
  if 1<= index<= len(vidioharu):
    name = input("Enter the vidios name to be post from playlist:")
    time = input("Enter the vidios at the time  to be post from the playlist:")
    vidioharu[index-1] = {'name':name,'time':time}
def update_vidio(vidioharu):
  playlist_all_vidio(vidioharu)
  index = int(input("Enter the vidio number to update:"))
  if 1<= index <= len(vidioharu):
    name =input("Enter the new vidio name:")
    time = input("Enter the new vidio name:")
    vidioharu[index-1] = {'name':name,'time':time}
    save_data_helper(vidioharu)
  else:
    print("invalid index selected")
def delete_vidio(vidioharu):
  playlist_all_vidio(vidioharu)
  index = int(input("Enter the vidio number to delete:"))
  if 1<= index <= len(vidioharu):
    del vidioharu[index-1]
    save_data_helper(vidioharu)
  else:
    print("invalid index selected:")

def main():
 vidioharu = load_data()
 while True:
  print(" \nYoutube vidio manager| Choose the below option \n")
  print("1) playlist of all youtube vidios")
  print("2) Get a youtube vidios")
  print("3) Post the youtube vidios")
  print("3) Update the youtube vidio details")
  print("4) Delete the youtube")
 
  print("5) Exit the app")

 # takin the choice from the user as input method
  choice = input("Enter your choice:")
 # if choice  == "1" or if choice == "2" can use but in stead of it we can use match choice
  match choice:
    case '1':
      playlist_all_vidio(vidioharu)
    case '2':
      get_vidios(vidioharu)
    case '3':
     post_vidios(vidioharu)
    case '4':
     update_vidio(vidioharu)
    case '5':
     delete_vidio(vidioharu)
    case '6':
     break
    case _:
     # this is the wildcard of the pattern and it never fail to match
     print("Invalid choice")
if __name__ == "__main__":
   main()'''



import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(vidioharu):
    with open("youtube.txt", 'w') as file:
        json.dump(vidioharu, file)

def playlist_all_vidio(vidioharu):
    for index, vidio in enumerate(vidioharu, start=1):
        print('\n')
        print('@' * 90)
        print(f"{index}) {vidio['name']} , Duration: {vidio['time']}")
        print('\n')
        print('@' * 90)

def add_vidios(vidioharu):
    name = input("Enter the YouTube video name: ")
    time = input("Enter the uploaded YouTube video time: ")
    vidioharu.append({'name': name, 'time': time})
    save_data_helper(vidioharu)

def post_vidios(vidioharu):
    playlist_all_vidio(vidioharu)
    index = int(input("Enter the video number to post: "))
    if 1 <= index <= len(vidioharu):
        name = input("Enter the video's name to be posted from the playlist: ")
        time = input("Enter the video's time to be posted from the playlist: ")
        vidioharu[index-1] = {'name': name, 'time': time}
        save_data_helper(vidioharu)

def update_vidio(vidioharu):
    playlist_all_vidio(vidioharu)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(vidioharu):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        vidioharu[index-1] = {'name': name, 'time': time}
        save_data_helper(vidioharu)
    else:
        print("Invalid index selected")

def delete_vidio(vidioharu):
    playlist_all_vidio(vidioharu)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(vidioharu):
        del vidioharu[index-1]
        save_data_helper(vidioharu)
    else:
        print("Invalid index selected")

def main():
    vidioharu = load_data()
    while True:
        print(" \nYouTube Video Manager | Choose an option below \n")
        print("1) Playlist of all YouTube videos")
        print("2) Get a YouTube video")
        print("3) Post a YouTube video")
        print("4) Update the YouTube video details")
        print("5) Delete the YouTube video")
        print("6) Exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                playlist_all_vidio(vidioharu)
            case '2':
                add_vidios(vidioharu)
            case '3':
                post_vidios(vidioharu)
            case '4':
                update_vidio(vidioharu)
            case '5':
                delete_vidio(vidioharu)
            case '6':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
