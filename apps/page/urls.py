from django.urls import path
from .views import CMSView1,CMSView2,CMSView3,CMSView4,CMSView5,CMSAboutView

urlpatterns = [
    # CMS Dashboard Home Page
    path('cmshomesec1/',CMSView1.as_view(),name='update'),
    path('cmshomesec2/',CMSView2.as_view(),name='cmshomesec2'),
    path('cmshomesec3/',CMSView3.as_view(),name='cmshomesec3'),
    path('cmshomesec4/',CMSView4.as_view(),name='cmshomesec4'),
    path('cmshomesec5/',CMSView5.as_view(),name='cmshomesec5'),

    # CMS Dashboard About Page
    path('cmsabout/',CMSAboutView.as_view(),name='cmsabout')
]
