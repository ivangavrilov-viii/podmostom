from django.shortcuts import render
import general.names as names_file


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
        email_to_send = 'podmostom.msk@gmail.com'
        email_from = 'nikityuk.info@gmail.com'
        success_send = True

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
