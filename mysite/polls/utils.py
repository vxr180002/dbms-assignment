import re
from django.db.models import Q

def create_search_filter(search_text):
    regex = r'\b\w+\b'
    search_strings = re.findall(regex, search_text)
    q_list = []
    for item in search_strings:
        search_filter_item = (Q(first_name__icontains=item) | Q(middle_name__icontains=item)
        | Q(last_name__icontains=item) | Q(home_phone__icontains=item)
        | Q(cell_phone__icontains=item) | Q(home_address__icontains=item)
        | Q(home_city__icontains=item) | Q(home_state__icontains=item)
        | Q(home_zip__icontains=item) | Q(work_phone__icontains=item)
        | Q(work_address__icontains=item) | Q(work_city__icontains=item)
        | Q(work_state__icontains=item) | Q(work_zip__icontains=item)
        | Q(birth_date__icontains=item))

        q_list.append(search_filter_item)

    return q_list