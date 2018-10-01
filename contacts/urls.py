from django.conf.urls import url
from contacts.views import ContactList, ContactCreate, ContactDetail, ContactEdit

urlpatterns = [
    url(r'^all/$', ContactList.as_view(), name='all_contacts'),
    url(r'^(?P<pk>\d+)/$', ContactDetail.as_view(), name='contact'),
    url(r'^(?P<pk>\d+)/edit$', ContactEdit, name='contact_edit'),
    url(r'^add$', ContactCreate.as_view(), name='contact_add'),
]
