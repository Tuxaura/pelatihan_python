import time


def send_emails():
    for i in range(10000000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
