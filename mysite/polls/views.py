from functools import reduce
import operator
from django.forms import modelformset_factory
from django.shortcuts import render, render_to_response
from .models import Contacts
from django.http import HttpResponseRedirect
import django_tables2 as tables

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Contacts, address, phone, date, SimpleAddressTable, SimpleDateTable, SimplePhoneTable
from django.template import loader, RequestContext
from django.db.models import Q
from .utils import create_search_contact_id, get_contact_id_from_queryset
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
    allContactObjects = Contacts.objects.order_by("contact_id")
    template = loader.get_template('polls/allContacts.html')
    context = {
        'allContactObjects': allContactObjects
    }

    return HttpResponse(template.render(context, request))

def search_contacts(request):
    search_text = request.GET.get('search_text', '')
    contact_id_list = create_search_contact_id(search_text)
    if contact_id_list:
        search_results = Contacts.objects.filter(contact_id__in=contact_id_list)
        # Contacts.objects.filter(pk__in=[1, 4, 7])

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
    all = Contacts.objects.all()

    for item in all:
        if item.home_phone:
            area_code_temp = item.home_phone.replace('-','')[:3]
            number_temp = item.home_phone.replace('-','')[:3]
            add =phone(contact_id=item, phone_type = 'home', area_code= area_code_temp, number= number_temp)
            add.save()
        if item.work_phone:
            area_code_temp = item.work_phone.replace('-','')[:3]
            number_temp = item.work_phone.replace('-','')[:3]
            add = phone(contact_id=item, phone_type='work', area_code= area_code_temp, number= number_temp)
            add.save()
        if item.cell_phone:
            area_code_temp = item.cell_phone.replace('-','')[:3]
            number_temp = item.cell_phone.replace('-','')[:3]
            add = phone(contact_id=item, phone_type='cell', area_code= area_code_temp, number= number_temp)
            add.save()
        if item.birth_date:
            add = date(contact_id=item, date_type='birth date', date=item.birth_date)
            add.save()

        # this code adds initial addresses to the db
        # if item.home_address or item.home_city or item.home_state or item.home_zip:
        #     add = address(contact_id=item, address_type='home', address=item.home_address,
        #                       city=item.home_city, state=item.home_city, zip=item.home_zip)
        #     add.save()
        #
        # if item.work_address or item.work_city or item.work_state or item.work_zip:
        #     add = address(contact_id=item, address_type='work', address=item.work_address,
        #                       city=item.work_city, state=item.work_city, zip=item.work_zip)
        #     add.save()

def simple_list(request):
    queryset = address.objects.all()
    # table = SimpleTable(queryset)
    # return render(request, "polls/simple_list.html", {"table": table})
    context = {
        'search_results': queryset
    }
    template = loader.get_template('polls/simple_list.html')
    return HttpResponse(template.render(context, request))


def django_table(request):
    queryset = phone.objects.all()
    table = SimplePhoneTable(queryset)
    contact_list = phone.objects.filter(contact_id__lte=3).values_list('contact_id',flat=True)
    return render(request, "polls/django_table.html", {"table": table})

    #
    # contact_contact_id =
    # address_contact_id =
    # date_contact_id =
    # phone_contact_id =




    # all address views
def address_list(request, contact_id):
    queryset = address.objects.filter(Q(contact_id_id=contact_id))
    context = {
        'search_results': queryset,
        'contact_id': contact_id
    }
    template = loader.get_template('polls/addresses.html')
    return HttpResponse(template.render(context, request))

def manage_address(request, contact_id, address_id):
    addressFormSet = modelformset_factory(address,
                                          fields=('address_type',
                                                  'address',
                                                  'city',
                                                  'state',
                                                  'zip'
                                                  ), max_num=1)
    if request.method == 'POST':
        formset = addressFormSet(request.POST, request.FILES)
        if formset.is_valid():
            save_formset(contact_id, formset)
            return HttpResponseRedirect('/polls/address_list/%s' % contact_id)
            # do something.
    else:
        formset = addressFormSet(queryset=address.objects.filter(address_id=address_id))
    return render(request, 'polls/manage_address.html', {'formset': formset, 'address_id': address_id, 'contact_id':contact_id})


def save_formset(contact_id, formset):
    for form in formset:
        tempFormset = form.save(commit=False)
        tempFormset.contact_id_id = contact_id
        tempFormset.save()


def delete_address(request, address_id):
    deleted_address = address.objects.filter(Q(address_id=address_id))
    contact_id = get_contact_id_from_queryset(deleted_address)
    deleted_address.delete()
    return HttpResponseRedirect('/polls/address_list/%s' % contact_id)

    # all date views
def date_list(request, contact_id):
    queryset = date.objects.filter(Q(contact_id_id=contact_id))
    context = {
        'search_results': queryset,
        'contact_id': contact_id
    }
    template = loader.get_template('polls/dates.html')
    return HttpResponse(template.render(context, request))

def manage_date(request, contact_id, date_id):

    dateFormSet = modelformset_factory(date,
                                          fields=('date_type',
                                                  'date'
                                                  ), max_num=1)
    if request.method == 'POST':
        formset = dateFormSet(request.POST, request.FILES)
        if formset.is_valid():
            save_formset(contact_id, formset)
            return HttpResponseRedirect('/polls/date_list/%s' % contact_id)
            # do something.
    else:
        formset = dateFormSet(queryset=date.objects.filter(date_id=date_id))
    return render(request, 'polls/manage_date.html', {'formset': formset, 'date_id': date_id, 'contact_id':contact_id})

def delete_date(request, date_id):
    deleted_date = date.objects.filter(Q(date_id=date_id))
    contact_id = get_contact_id_from_queryset(deleted_date)
    deleted_date.delete()
    return HttpResponseRedirect('/polls/date_list/%s' % contact_id)

    # all phone views
def phone_list(request, contact_id):
    queryset = phone.objects.filter(Q(contact_id_id=contact_id))
    context = {
        'search_results': queryset,
        'contact_id': contact_id
    }
    template = loader.get_template('polls/phones.html')
    return HttpResponse(template.render(context, request))

def manage_phone(request,contact_id, phone_id):

    phoneFormSet = modelformset_factory(phone,
                                          fields=('phone_type',
                                                  'area_code',
                                                  'number'
                                                  ), max_num=1)
    if request.method == 'POST':
        formset = phoneFormSet(request.POST, request.FILES)
        if formset.is_valid():
            save_formset(contact_id, formset)
            return HttpResponseRedirect('/polls/phone_list/%s' % contact_id)
            # do something.
    else:
        formset = phoneFormSet(queryset=phone.objects.filter(phone_id=phone_id))
    return render(request, 'polls/manage_phone.html', {'formset': formset, 'phone_id': phone_id, 'contact_id':contact_id})

def delete_phone(request, phone_id):
    deleted_phone = phone.objects.filter(Q(phone_id=phone_id))
    contact_id = get_contact_id_from_queryset(deleted_phone)
    deleted_phone.delete()
    return HttpResponseRedirect('/polls/phone_list/%s' % contact_id)