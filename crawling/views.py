from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django. views.generic import TemplateView
from django.template.context_processors import request, csrf
import urllib.request
from bs4 import BeautifulSoup
import re
import sys, os, csv, io
from django.views.decorators.csrf import requires_csrf_token, csrf_protect
from django.template.defaulttags import csrf_token
from crawling.forms import PostForm, UploadForm
from pip._vendor.requests.models import Request
from django.http.response import HttpResponseRedirect
import webbrowser
from django.core.urlresolvers import reverse
from crawling.models import Hasil_Pencarian_Keyword
# Create your views here.

# class HomePageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'index.html', context=None)
def homePageView(request):
    return render(request, 'index.html')

# class CrawlingView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'crawling.html', context=None)

def crawlingView(request):
    
    return render(request, 'crawling.html')
    
def hasil(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():        
            url1 = form.cleaned_data['url1']
            keyword1 = form.cleaned_data['keyword1']
          
    # membuat koneksi ke url 
    page= urllib.request.urlopen(url1)
    html = page.read()
 
    # membaca html
    soup = BeautifulSoup(html, "html.parser")
#======================================================================================================================
    # fungsi bs4
    test = soup.findAll(string=re.compile(keyword1, re.IGNORECASE))
    list_search = []
    for tag in test:    
        query = Hasil_Pencarian_Keyword(word_result=tag)
        query.save()
        list_search.append(tag)
    
    
    return render(request, 'hasil_keyword.html', {'list_search':list_search})

def upload_file(request):
    csv_file = request.FILES['csv_file']
    decoded_file = csv_file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    file1 = csv.reader(io_string, delimiter=',')
    header = next(file1)
    list_csv = []
    for row in file1:
        list_csv.append(row)
    return render(request, 'crawling.html', {'header':header, 'list_csv':list_csv})

def open_url(request):
    url2 = request.POST['url2']
    webbrowser.open(url2)

def buka_url(request):
    return render(request, 'buka_url.html')
    
     
def result(request):
    key_word1 = 'dki'
    url = 'https://search.detik.com/search?query='+key_word1+'&source=dcnav&siteid=2'

    # membuat koneksi ke url 
    page= urllib.request.urlopen(url)
    html = page.read()
    
    # membaca html
    soup = BeautifulSoup(html, "html.parser")
    
    #======================================================================================================================
    judul = soup.find_all("div", class_="title")
    tanggal = soup.find_all("span", class_="date")
    a = len(judul)
    # for i in range(a):
    #     print("title : "+judul[i].text.strip())
    #     konten = judul[i].find_all_next(text=True)
    #     print("Isi : "+konten[3].strip())
    #     print("Tanggal : "+tanggal[i].text.strip())
    #     print()
                
    os.chdir("C:/Users/Asus-PC/Desktop/")
    
    with open("detik1.csv", "w") as toWrite:
        writer = csv.writer(toWrite, delimiter=",")
        writer.writerow(["Judul", "Konten", "Tanggal"])
        for i in range(a):
            konten = judul[i].find_all_next(text=True)
            writer.writerow([judul[i].text.strip(), konten[3].strip(), tanggal[i].text.strip()])
        
          
    
    
    # def index(request):
    #     return HttpResponse("Hello, world.")