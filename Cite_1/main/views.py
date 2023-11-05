from django.shortcuts import render


def index(reguest):
    return render(reguest, 'main/index.html')


def about(reguest):
    return render(reguest, 'main/about.html')


def we(reguest):
    return render(reguest, 'main/we.html')


def school(reguest):
    return render(reguest, 'main/school.html')