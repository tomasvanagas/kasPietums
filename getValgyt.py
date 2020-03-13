from facebook_scraper import get_posts
from datetime import date

today = str(date.today()).split(" ")[0] 

print("[*] ==== Soul ====")
for post in get_posts('Restoranas.Soul', pages=1):
	print(post['time'])
	print()
	print(post['text'])
	break


print("\n[*] ==== Salonas ====")
for post in get_posts('SalonasRestobar', pages=1):
	time = str(post['time'])
	if(today in str(time)):
		print(post['time'])
		print()
		print(post['text'])
		break
