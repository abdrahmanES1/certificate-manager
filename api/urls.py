from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path('diplomes', views.DiplomeList.as_view(), name='diplomes'),
    path('diplomes/<CNI>', views.search, name='one_diplomes'),
    path('diplomes/search/<CNI>-<filiere>-<type_diplome>',
         views.search_by, name='type_diplome'),
    path('filiere', views.get_all_filiere, name='filiere'),
    path('type_diplome', views.get_all_type_diplome, name='type_diplome'),
]
