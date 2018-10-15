from functools import reduce
import operator
from django.forms import modelformset_factory
from django.shortcuts import render, render_to_response
from .models import Contacts
from django.http import HttpResponseRedirect
import django_tables2 as tables

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Contacts, address, SimpleTable
from django.template import loader, RequestContext
from django.db.models import Q
from .utils import create_search_filter
import csv
# Create your views here

def index(request):
    context = {}
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context, request))

def delete_data(request):
    Contacts.objects.all().delete()
    return HttpResponse("All data deleted")

def import_data(request):
    with open('polls/Contacts.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Contacts.objects.get_or_create(
            contact_id = row[0],
            first_name = row[1],
            middle_name = row[2],
            last_name = row[3],
            home_phone = row[4],
            cell_phone = row[5],
            home_address = row[6],
            home_city = row[7],
            home_state = row[8],
            home_zip = row[9],
            work_phone = row[10],
            work_address = row[11],
            work_city = row[12],
            work_state = row[13],
            work_zip = row[14],
            birth_date = row[15],
            )
    return HttpResponse("all objects loaded")
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def all_contacts(request):
    allContactObjects = Contacts.objects.order_by("-contact_id")
    template = loader.get_template('polls/allContacts.html')
    context = {
        'allContactObjects': allContactObjects,
    }

    return HttpResponse(template.render(context, request))

def search_contacts(request):
    search_text = request.GET.get('search_text', '')
    q_list = create_search_filter(search_text)
    if q_list:
        search_results = Contacts.objects.filter(reduce(operator.and_,q_list))
    else:
        search_results = []
    context = {
        'search_text': search_text,
        'search_items': len(search_results),
        'search_results': search_results
    }

    template = loader.get_template('polls/search_contacts.html')
    return HttpResponse(template.render(context, request))

def manage_contacts(request, contact_id):
    ContactFormSet = modelformset_factory(Contacts,
                                          fields=('first_name'
                                                  ,'middle_name'
                                                  ,'last_name'
                                                  ,'home_phone'
                                                  ,'cell_phone'
                                                  ,'home_address'
                                                  ,'home_city'
                                                  ,'home_state'
                                                  ,'home_zip'
                                                  ,'work_phone'
                                                  ,'work_address'
                                                  ,'work_city'
                                                  ,'work_state'
                                                  ,'work_zip'
                                                  ,'birth_date'
), max_num=1)
    if request.method == 'POST':
        formset = ContactFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/polls/all_contacts')
            # do something.
    else:
        formset = ContactFormSet(queryset=Contacts.objects.filter(contact_id = contact_id))
    return render(request, 'polls/manage_contacts.html', {'formset': formset, 'contact_id': contact_id})

def delete_contact(request, contact_id):
    Contacts.objects.filter(contact_id = contact_id).delete()
    return HttpResponseRedirect('/polls/all_contacts')

def list_addresses(request):
    all = address.objects.all()

    # for item in all:
    #
    #     if item.home_address or item.home_city or item.home_state or item.home_zip:
    #         add = address(contact_id=item, address_type='home', address=item.home_address,
    #                           city=item.home_city, state=item.home_city, zip=item.home_zip)
    #         add.save()
    #
    #     if item.work_address or item.work_city or item.work_state or item.work_zip:
    #         add = address(contact_id=item, address_type='work', address=item.work_address,
    #                           city=item.work_city, state=item.work_city, zip=item.work_zip)
    #         add.save()

def simple_list(request):
    queryset = address.objects.all()
    table = SimpleTable(queryset)
    return render(request, "polls/simple_list.html", {"table": table})

