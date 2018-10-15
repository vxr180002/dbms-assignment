from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import', views.import_data, name='import_data'),
    path('delete', views.delete_data, name='delete_data'),
    # ex: /polls/all_contacts
    path('all_contacts', views.all_contacts, name='all_contacts'),
    # ex: /polls/search_contacts
    path('search_contacts', views.search_contacts, name='search_contacts'),
    path('manage_contacts/<int:contact_id>', views.manage_contacts, name='manage_contacts'),
    path('delete_contact/<int:contact_id>', views.delete_contact, name='delete_contact'),
    path('list', views.list_addresses, name='list_address')
    ,path('simple', views.simple_list, name='simple_list')
]
