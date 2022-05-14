from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from familia.models import Family


def familiares(self):

    aux = Family.objects.all()
    fam = {'personas':aux}

    template = loader.get_template('template.html')

    document = template.render(fam)

    return HttpResponse(document)