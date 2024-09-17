import smtplib
import os
from dotenv import load_dotenv

load_dotenv("messages/secrets.env")

my_login = os.getenv('LOGIN')
my_password = os.getenv('PASSWORD')
my_name = os.getenv('NAME')

server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
server.login(my_login, my_password)


address_from = my_login
address_to = 'aza2004mat001@gmail.com'
my_name = my_name
friend_name = "Wan Sinchen"
website = "https://dvmn.org/referrals/tXhgJQxGiVJTQnmjihFw1AIww9SssU7qY3anusGW/"
letter = """\
From: {ad_from}
To: {ad_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {f_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на {website}?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → {website}
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(ad_from=address_from, ad_to=address_to, f_name=friend_name, my_name=my_name, website=website)

letter = letter.encode("UTF-8")

try:
    server.sendmail(my_login, 'aza2004mat001@gmail.com', letter)
    server.quit()
    print('sent')
except Exception:
    print("error")
