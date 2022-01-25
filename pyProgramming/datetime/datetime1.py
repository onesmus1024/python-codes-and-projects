import datetime

now =datetime.datetime.now()
today = datetime.datetime.today()
diff =datetime.timedelta(days=20)
future=today+diff

print("now = {},\n today={},\n future = {}".format(now,today,future))

