from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    path('upload',views.docx1,name='upload'),
    path('Docx1',views.docx1,name='Docx1'),
    path('Docx2',views.docx2,name='Docx2'),
    path('Latex',views.Latex,name='Latex'),
    path('show1',views.show1,name='show1'),
    path('show2',views.show2,name='show2'),
    path('show3',views.show3,name='show3'),
    path('show4',views.show4,name='show4'),
    path('show5',views.show5,name='show5'),
    path('show6',views.show6,name='show6'),
    path('show7',views.show7,name='show7'),
    path('show1_docx2',views.show1_docx2,name='show1_docx2'),
    path('show2_docx2',views.show2_docx2,name='show2_docx2'),
    path('show3_docx2',views.show3_docx2,name='show3_docx2'),
    path('show4_docx2',views.show4_docx2,name='show4_docx2'),
    path('show5_docx2',views.show5_docx2,name='show5_docx2'),
    path('show6_docx2',views.show6_docx2,name='show6_docx2'),
    path('show7_docx2',views.show7_docx2,name='show7_docx2'),
    path('show1_latex',views.show1_latex,name='show1_latex'),
    path('show2_latex',views.show2_latex,name='show2_latex'),
    path('show3_latex',views.show3_latex,name='show3_latex'),
    path('show4_latex',views.show4_latex,name='show4_latex'),
    path('show5_latex',views.show5_latex,name='show5_latex'),
    path('show6_latex',views.show6_latex,name='show6_latex'),
    path('show7_latex',views.show7_latex,name='show7_latex')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    path('show1',views.show1,name='show1'),
    path('show2',views.show2,name='show2'),
    path('show3',views.show3,name='show3'),
    path('show4',views.show4,name='show4'),
    path('show5',views.show5,name='show5'),
    path('show6',views.show6,name='show6')
"""
