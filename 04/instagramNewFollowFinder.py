import instaloader

username = input("Username: ")

L = instaloader.Instaloader()
L.interactive_login(username)
profile = instaloader.Profile.from_username(L.context, "dehmovlaei")

f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line.strip())
f.close()

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower.username)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

f = open("followers.txt", "w")
for new_follower in new_followers:
    f.write(new_follower + "\n")
f.close()