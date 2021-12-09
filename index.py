import datetime
import stream

print("Welcome to the python-stream project!")
YOUR_API_KEY=input("Enter the stream API Key:")
API_KEY_SECRET=input("Enter the API secret:")

client = stream.connect(YOUR_API_KEY, API_KEY_SECRET)
print("Client connected successfully!\n")
print("Make sure that you have feed groups inside your getstream dashboard!\n")
print("For more info refer to https://getstream.io\n")


user=input("Enter Your Feed Group Name:")
user_id=input("Enter your App id:")
user_feed_1 = client.feed(user, user_id)

def default_feed():
    result = user_feed_1.get(limit=5, id_lt="e561de8f-00f1-11e4-b400-0cc47a024be0")
    print(result)

def delete_feed():
    remove_activity=input("Remove Activity?[Y/N]:")
    if remove_activity in "Yy":
        user_feed_1.remove_activity("e561de8f-00f1-11e4-b400-0cc47a024be0")
    else:
        pass

def create_activity():
    activity_data = {
        'actor': input("Enter Actor(Example:1):"), 
        'verb': input("Enter Verb(Example:'tweet'):"), 
        'object': input("Enter Object(Example:1):"), 
        'foreign_id': input("Enter foriegn_id(Example:'tweet:1'):")
        }
    activity_response = user_feed_1.add_activity(activity_data)

def remove_activity():
    user_feed_1.remove_activity(foreign_id=input("Enter foriegn_id(Example:'tweet:1'):"))

def follow_feed():
    user_feed_1.follow(input("Enter feedname:"), input("Enter appid:"))

def unfolow_feed():
    user_feed_1.unfollow(input("Enter feedname:"), input("Enter appid:"))

def you_follow():
    print("You follow:")
    following = user_feed_1.following(offset=0, limit=2)
    print(following)
def your_followers():   
    print("Your followers:")
    followers = user_feed_1.followers(offset=0, limit=10)
    print(followers)

def menu():
    print("MENU:")
    print("1. Get Feed Activity")
    print("2. Delete Activity")
    print("3. Add Activity")
    print("4. Remove Activity")
    print("5. Follow Feed")
    print("6. Unfollow Feed")
    print("7. List of your following")
    print("8. List of followers")
    command=input("Enter the No. associated with command:")
    if command in "1":
        default_feed()
    elif command in "2":
        delete_feed()
    elif command in "3":
        create_activity()
    elif command in "4":
        remove_activity()
    elif command in "5":
        follow_feed()
    elif command in "6":
        unfolow_feed()
    elif command in "7":
        you_follow()
    elif command in "8":
        your_followers()
    else:
        print("Error! Try again!")
        menu()
    again=input("Want to execute 2nd command?[Y/N]:")
    if again in "Yy":
        menu()
    elif again in "Nn":
        print("Bye!")
    else:
        print("Oh no! Invalid input! Bye!")
menu()