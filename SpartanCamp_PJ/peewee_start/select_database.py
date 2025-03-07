from database import Thread


threads = Thread.select()
print(threads[0].name)
print(threads[1].name)

threads = Thread.select().where(Thread.name == "satoshi").get()
print(threads.name, threads.title, threads.body)
