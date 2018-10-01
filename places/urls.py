from django.conf.urls import url
from places.views import CityCreate, CityDetail, CityList, CityEdit, CountryCreate, CountryEdit

urlpatterns = [

    url(r'^all/$', CityList.as_view(), name='all_places'),
    url(r'^(?P<pk>\d+)/$', CityDetail.as_view(), name='place'),
    url(r'^(?P<pk>\d+)/edit$', CityEdit.as_view(), name='place_edit'),
    url(r'^(?P<pk>\d+)/countryedit$', CountryEdit.as_view(), name='country_edit'),
    url(r'^addcity$', CityCreate.as_view(), name='place_add'),
    url(r'^addcountry$', CountryCreate.as_view(), name='country_add'),
]
