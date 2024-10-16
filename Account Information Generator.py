## Generates a random username, password and email for you to use :)

## pip install:
## prettytable
## mechanicalsoup
## bs4

import re
import os
import time
import random
import requests
import prettytable
import mechanicalsoup
import bs4 as beautifulsoup

my_Mail = None
my_Password = None
my_Username = None

my_logo = r"""
  ██╗   ██╗██████╗ ██╗███╗   ██╗███████╗ ██████╗ 
  ██║   ██║██╔══██╗██║████╗  ██║██╔════╝██╔═████╗
  ██║   ██║██████╔╝██║██╔██╗ ██║█████╗  ██║██╔██║
  ██║   ██║██╔══██╗██║██║╚██╗██║██╔══╝  ████╔╝██║
  ╚██████╔╝██║  ██║██║██║ ╚████║██║     ╚██████╔╝
  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝    
                            __               ___       __            
                            |__) \ /    |\ | |__  |  | |__)  /\  |    
                            |__)  |     | \| |___ \__/ |  \ /~~\ |___ 
            """

ESC = '\x1b'

def GetEmail():
    print(ESC + '[31m' + 'Generating email...')
    time.sleep(1)

    placebo = mechanicalsoup.StatefulBrowser()

    try:
        data = placebo.open("https://tempmailto.org/")
        source = data.text

        prettfied = beautifulsoup.BeautifulSoup(source, 'html.parser')

        for script in prettfied.find_all('script'):
            script_content = script.string

            if script_content:
                if re.search("@", script_content):
                    email_pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'

                    match = re.search(email_pattern, script_content)
                    
                    if match:
                        # Convert Match object to string (the full email)
                        matched_email = match.group(0)  # group(0) returns the entire match

                        print(ESC + '[32m' + "Successfully found email!")
                        time.sleep(1)

                        return matched_email
                    else:
                        print("No email found.")
    except:
        print("failure...")




def GeneratePassword():
    print(ESC + '[31m' + 'Generating password...')
    time.sleep(1)

    password = ""
    password_length = random.randint(10, 20)

    choices = {
        "chars" : [],
        "numbers" : [],
        "special_chars" : [],
    }

    choices["chars"].extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    choices["numbers"].extend("0123456789")
    choices["special_chars"].extend(r"!£$%^&()_+-=[]#';./,.")

    for i in range(password_length):
        what_list = random.randint(1,3)
        what_list -= 1
        true_index = 0

        for index, nil in choices.items():
            if true_index == what_list:
                needed_list = nil
                if type(needed_list) == list:
                    random_index = random.randint(0, len(needed_list) - 1)

                    new_value = needed_list[random_index]
                    password += new_value
            else:
                true_index += 1

    print(ESC + '[32m' + "Successfully generated password!")
    time.sleep(1)

    return password



def GenerateUsername():
    print(ESC + '[31m' + 'Generating username...')
    time.sleep(1)


    response = requests.get('https://randomuser.me/api/')
    data = response.json()

    added_characters = []
    added_characters.extend("abcdefghijklmnnopqrstuvwxyz1234567890")

    new_dude = ""

    for i in range(1, random.randint(2,4)):
        new_dude += added_characters[random.randint(0, (len(added_characters) - 1))]

    username = data['results'][0]['login']['username'] + new_dude

    print(ESC + '[32m' + "Successfully generated username!")
    time.sleep(1)

    return username



def Layout_Info(Username, Password, Email):
    layout_table = prettytable.PrettyTable()
    layout_table.add_column("Username", [Username])
    layout_table.add_column("Password", [Password])
    layout_table.add_column("Email", [Email])

    print(ESC + '[2J')
    print(ESC + '[37m' + " ")

    print(my_logo)
    print(layout_table)


my_Password = GeneratePassword()
my_Username = GenerateUsername()
my_Mail = GetEmail()

Layout_Info(my_Username, my_Password, my_Mail)


try:
    temp_directory = os.getenv('TEMP')

    file_name = 'My_Generated_Information.txt'
    file_path = os.path.join(temp_directory, file_name)
    
    with open(file_path, "w") as file:
        file.write(f"USERNAME: {my_Username}\n")
        file.write(f"PASSWORD: {my_Password}\n")
        file.write(f"EMAIL: {my_Mail}")

        print("Saved output to: ", file.name)
except:
    print("failed to open...")

Choice = input("\n")
