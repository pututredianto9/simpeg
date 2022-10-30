import imp
import re
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Pegawai, Divisi, Jabatan
from . functions.functions import *
import csv
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

def beranda(request):
    return render(request, 'beranda.html')
def about(request):
    return render(request, 'about.html')

@login_required
def getPegawai(request):
    pegawai_list = Pegawai.objects.all()
    template = 'pegawai.html'
    context = {
        'pegawai_list':pegawai_list
    }
    return render(request, template, context)
    
@login_required
def getJabatan(request):
    jabatan_list = Jabatan.objects.all()
    template = 'jabatan.html'
    context = {
        'jabatan_list':jabatan_list
    }
    return render(request, template, context)

@login_required
def getDivisi(request):
    divisi_list = Divisi.objects.all()
    template = 'divisi.html'
    context = {
        'divisi_list':divisi_list
    }
    return render(request, template, context)

@login_required
def formPegawai(request):
    #pegawai_list = Pegawai.objects.all()
    template = 'form_pegawai.html'
    divisi_list = Divisi.objects.all()
    jabatan_list = Jabatan.objects.all()
    context = {
        'divisi_list' : divisi_list,
        'jabatan_list' : jabatan_list,
    }
    return render(request, template, context)
def createPegawai(request):
    if request.method == 'POST':
        if request.FILES:
            handle_uploaded_file(request.FILES['foto'])

        nip = request.POST['nip']
        nama = request.POST['nama']
        alamat = request.POST['alamat']
        email = request.POST['email']
        gender = request.POST['gender']
        jabatan = request.POST['jabatan']
        divisi = request.POST['divisi']
        foto = request.FILES['foto']

        p = Pegawai()
        p.nip = nip
        p.nama = nama
        p.alamat = alamat
        p.email = email
        p.gender = gender
        p.jabatan_id = jabatan
        p.divisi_id = divisi
        p.foto = foto
        p.save()
    pegawai_list = Pegawai.objects.all()
    template = 'pegawai.html'
    context = {
        'pegawai_list':pegawai_list
    }
    return render(request, template, context)
        
def editPegawai(request,nip):
    #pegawai_list = Pegawai.objects.all()
    template = 'form_edit_pegawai.html'
    edit_pegawai = Pegawai.objects.filter(nip=nip)
    divisi_list = Divisi.objects.all()
    jabatan_list = Jabatan.objects.all()
    context = {
        'edit_pegawai': edit_pegawai,
        'divisi_list' : divisi_list,
        'jabatan_list' : jabatan_list,
    }
    if request.method == 'POST':
        print("UPDATED HERE")
        return updatePegawai(request,nip=nip)
    else:
        return render(request, template, context)

def updatePegawai(request,nip="",action=""):
    if request.FILES:
        handle_uploaded_file(request.FILES['foto'])
        nip = request.POST['nip']
        nama = request.POST['nama']
        alamat = request.POST['alamat']
        email = request.POST['email']
        gender = request.POST['gender']
        jabatan = request.POST['jabatan']
        divisi = request.POST['divisi']
        foto = request.FILES['foto']

        Pegawai.objects.filter(nip=nip).update(nip=nip,nama=nama,alamat=alamat,email=email,gender=gender,jabatan_id=jabatan,divisi_id=divisi,foto=foto)
        return redirect('/app/pegawai/')

def deletePegawai(request, nip):
    if request.method == "GET":
        Pegawai.objects.filter(nip=nip).delete()
        return redirect('/app/pegawai/')
    
def exportcsv(request):
    p = Pegawai.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=pegawai.csv'
    writer = csv.writer(response)
    writer.writerow(['NIP','Nama', 'Gender','Alamat','Divisi','Jabatan'])
    pegs = p.values_list('nip','nama','gender','alamat','jabatan_id','divisi_id')
    for data in pegs:
        writer.writerow(data)
    return response

def login(request):
    return render(request, 'login.html')

def prosesLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('/app/pegawai/')
        else:
            return HttpResponse("<script> alert('maaf username dan password salah'); history.go(-1); </script>")

def logoutUser(request):
    logout(request)
    return redirect('/app/beranda/')