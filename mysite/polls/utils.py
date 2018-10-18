import re
from django.db.models import Q
from functools import reduce
import operator

from .models import Contacts, address, phone, date


def create_search_contact_id(search_text):
    regex = r'\b\w+\b'
    search_strings = re.findall(regex, search_text)
    contact_id_list = []

    q_list_contacts = []
    if search_text:
        for item in search_strings:
            search_filter_item = (Q(first_name__icontains=item) | Q(middle_name__icontains=item)
                                | Q(last_name__icontains=item) )
            q_list_contacts.append(search_filter_item)

        contact_contact_id = list(Contacts.objects.filter(reduce(operator.and_, q_list_contacts))
                                  .values_list('contact_id', flat=True))

        q_list_address = []
        for item in search_strings:
            search_filter_item = (Q(address_type__icontains=item) | Q(address__icontains=item)
                                | Q(state__icontains=item) | Q(city__icontains=item) | Q(zip__icontains=item))
            q_list_address.append(search_filter_item)

        address_contact_id = list(address.objects.filter(reduce(operator.and_, q_list_address))
                                  .values_list('contact_id',flat=True))

        q_list_phone = []
        for item in search_strings:
            search_filter_item = (Q(phone_type__icontains=item) | Q(area_code__icontains=item)
                                  | Q(number__icontains=item))
            q_list_phone.append(search_filter_item)

        phone_contact_id = list(phone.objects.filter(reduce(operator.and_, q_list_phone))
                                .values_list('contact_id',flat=True))

        q_list_date = []
        for item1 in search_strings:
            search_filter_item = (Q(date_type__icontains=item1)
                                  | Q(date__icontains=item1))
            q_list_date.append(search_filter_item)

        date_contact_id = list(date.objects.filter(reduce(operator.and_, q_list_date)).values_list('contact_id',
                                                                                                        flat=True))

        contact_id_list = list(set(contact_contact_id + address_contact_id + phone_contact_id + date_contact_id))

    return contact_id_list


def get_contact_id_from_queryset(queryset):
    for item in queryset:
        contact_id = item.contact_id_id
        return contact_id