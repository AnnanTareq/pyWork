import requests
import schedule
import time

def send_messase():
  resp = requests.post('https://textbelt.com/text', {
    'phone': '+1(202)3449368',
    'message': 'Hey Roni, this is joy. hahahaha',
    'key': 'textbelt',
  })

  print(resp.json())


schedule.every(15).seconds.do(send_messase())

while True:
  schedule.run_pending()
  time.sleep(1)



