import re
import random
import requests
import prettytable
import mechanicalsoup
import bs4 as beautifulsoup

my_Mail = None
my_Password = None
my_Username = None

def GetEmail():
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

                        return matched_email
                    else:
                        print("No email found.")
    except:
        print("failure...")




def GeneratePassword():
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
    return password



def GenerateUsername():
    response = requests.get('https://randomuser.me/api/')
    data = response.json()

    added_characters = []
    added_characters.extend("abcdefghijklmnnopqrstuvwxyz1234567890")

    new_dude = ""

    for i in range(1, random.randint(2,4)):
        new_dude += added_characters[random.randint(0, (len(added_characters) - 1))]

    username = data['results'][0]['login']['username'] + new_dude
    return username



def Layout_Info(Username, Password, Email):
    layout_table = prettytable.PrettyTable()
    layout_table.add_column("Username", [Username])
    layout_table.add_column("Password", [Password])
    layout_table.add_column("Email", [Email])
    print(layout_table)


my_Password = GeneratePassword()
my_Username = GenerateUsername()
my_Mail = GetEmail()

Layout_Info(my_Username, my_Password, my_Mail)

Choice = input("\n")
