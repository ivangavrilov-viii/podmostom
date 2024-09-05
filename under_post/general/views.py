from django.shortcuts import render
import general.names as names_file
# from decouple import config
import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# gmail_user = config('email_from')
# gmail_password = config('email_from_password')
# gmail_to = config('email_to')


# smtp_server = smtplib.SMTP("smtp.gmail.com", 25)
# smtp_server.starttls()
# smtp_server.login("gavrilovivan2001@gmail.com", "55JolP-eRnq-08")


def mail(email_to, subject, text):

    # https://support.google.com/a/answer/2956491?sjid=4983347348702673248-EU
    msg = MIMEMultipart()

    msg["From"] = "gavrilovivan2001@gmail.com"
    msg["To"] = email_to
    msg["Subject"] = subject

    msg.attach(MIMEText(text, "plain"))
    smtp_server.sendmail("gavrilovivan2001@gmail.com", "gavrilovivan008@gmail.com", msg.as_string())
    smtp_server.quit()


def index(request):
    """ View for main page """

    names = names_file.index_page('ru')
    photo_list = list()

    for index in range(10):
        photo_list.append(f"/media/circle_photo/{index}.png")

    context = {
        'photos': photo_list,
        'names': names,
    }

    return render(request, 'index.html', context)


def football_view(request):
    names = names_file.football_page('ru')
    success_send = False
    photo_list = list()

    for index in range(0, 6):
        photo_list.append(f"/media/football_circle_photos/{index + 1}.JPG")

    if request.method == 'POST':
        success_send = True
        mail("gavrilovivan008@gmail.com", "Тестовое письмо", "Привет! Это тестовое письмо, отправленное с помощью Python 😊")

    context = {
        'names': names,
        'success_send': success_send,
        'photos': photo_list
    }
    return render(request, 'football.html', context)


def basketball_view(request):
    names = names_file.basketball_page('ru')
    success_send = False
    photo_list = list()

    for index in range(0, 11):
        photo_list.append(f"/media/basketball_circle_photos/{index + 1}.JPG")

    if request.method == 'POST':
        success_send = True

    context = {
        'names': names,
        'success_send': success_send,
        'photos': photo_list
    }
    return render(request, 'basketball.html', context)


def history_view(request):
    names = names_file.history_page('ru')
    photo_list = list()
    for index in range(10):
        photo_list.append(f"/media/circle_photo/{index}.png")

    context = {
        'photos': photo_list,
        'names': names,
    }
    return render(request, 'history.html', context)


def policy_view(request):
    names = names_file.policy_page('ru')

    context = {
        'names': names,
    }
    return render(request, 'policy.html', context)
