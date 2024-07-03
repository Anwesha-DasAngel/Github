import random
lucky_num = random.randint(1,100)
random_text = ""
if  lucky_num >= 1 and lucky_num <=50:
    random_text = "You're lucky"
if lucky_num > 50 and lucky_num <=80:
   random_text = "You're unlucky"
if lucky_num == 100:
  random_text = "You've won"
else:
  print(f"You're lucky number is {lucky_num} : {random_text}")
