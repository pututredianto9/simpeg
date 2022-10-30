from django.urls import path
from . import views
urlpatterns = [
    
    path('beranda/', views.beranda, name='beranda'),
    path('about/', views.about, name='about'),
    path('divisi/', views.getDivisi, name='divisi'),
    path('jabatan/', views.getJabatan, name='jabatan'),
    path('pegawai/', views.getPegawai, name='pegawai'),
    path('pegawai/formPegawai', views.formPegawai, name='formPegawai'),
    path('pegawai/createPegawai', views.createPegawai, name='createPegawai'),
    path('pegawai/editPegawai/<int:nip>/', views.editPegawai, name='formEditPegawai'),
    path('pegawai/deletePegawai/<int:nip>/', views.deletePegawai, name='deletePegawai'),
    path('exportcsv/', views.exportcsv, name='exportcsv'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('prosesLogin/', views.prosesLogin, name='prosesLogin'),
]