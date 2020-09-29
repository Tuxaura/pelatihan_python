class User:
    user_count = 0

    def __init__(self, username):
        self.username = username
        User.user_count += 1


u1 = User("Budi")
print(u1.user_count)
u2 = User("Wati")
print(u2.user_count)
u3 = User("John")
print(u3.user_count)
