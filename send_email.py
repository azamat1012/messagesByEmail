import smtplib
import os
from dotenv import load_dotenv

load_dotenv("messages/secrets.env")

my_email = os.getenv('LOGIN')
my_password = os.getenv('PASSWORD')
my_name = os.getenv('NAME')

server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
server.login(my_email, my_password)


sender_email = my_email
sender_name = my_name
recipient_email = 'aza2004mat001@gmail.com'
recipient_name= "Wan Sinchen"
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
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(ad_from=sender_email, ad_to=recipient_email, f_name=recipient_name, my_name=sender_email, website=website)

letter = letter.encode("UTF-8")

try:
    server.sendmail(sender_email, recipient_email, letter)
    server.quit()
    print('sent')
except Exception:
    print("error")
