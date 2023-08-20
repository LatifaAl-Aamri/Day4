# problem of the day 4
"""
Mohammed wanted to find out if the person he was talking to online
was a girl or a boy by their username by this method:
charecters in the username is single ---> user is a boy
otherwise is a girl.
"""
def determine_gender(username):
    if len(username) == 1:
        return "boy"
    else:
        return "girl"

def main():
    username = input("Enter the username: ")
    gender = determine_gender(username)
    print(f"The user is a {gender}.")

if __name__ == "__main__":
    main()
    