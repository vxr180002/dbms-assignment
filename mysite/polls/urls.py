from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import', views.import_data, name='import_data'),
    path('delete', views.delete_data, name='delete_data'),
    # ex: /polls/all_contacts
    path('list', views.list_addresses, name='list_address'),
    path('simple', views.simple_list, name='simple_list'),
    path('django_table', views.django_table, name='django_table'),

    # urls for contact handling
    path('all_contacts', views.all_contacts, name='all_contacts'),
    path('search_contacts', views.search_contacts, name='search_contacts'),
    path('manage_contacts/<int:contact_id>', views.manage_contacts, name='manage_contacts'),
    path('delete_contact/<int:contact_id>', views.delete_contact, name='delete_contact'),

    # urls for address handling
    path('address_list/<int:contact_id>', views.address_list, name='address_list'),
    path('manage_address/<int:contact_id>/<int:address_id>', views.manage_address, name='manage_address'),
    path('delete_address/<int:address_id>', views.delete_address, name='delete_address'),

    # urls for date handling
    path('date_list/<int:contact_id>', views.date_list, name='date_list'),
    path('manage_date/<int:contact_id>/<int:date_id>', views.manage_date, name='manage_date'),
    path('delete_date/<int:date_id>', views.delete_date, name='delete_date'),

    # urls for phone handling
    path('phone_list/<int:contact_id>', views.phone_list, name='phone_list'),
    path('manage_phone/<int:contact_id>/<int:phone_id>', views.manage_phone, name='manage_phone'),
    path('delete_phone/<int:phone_id>', views.delete_phone, name='delete_phone')
]
