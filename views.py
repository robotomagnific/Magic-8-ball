from django.shortcuts import render
from django.http import HttpResponse
from controller_test import key
from controller_test import value


def index(request):
    html = "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>Randomly Select an SI Strategy</title></head><body><div style='margin: 0 auto;max-width: 700px;'><h4>Magic 8 Chooses:</h4><dl><dt>%s</dt><dd>%s</dd></dl></div></body></html>" % (key, value)
    return HttpResponse(html)














