from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
import requests
# Create your views here.



def index(request):
    return HttpResponse("Welcome to DSE Website")


def scrape_company_code(request):
    page = requests.get(
    "https://dsebd.org/company_listing.php")
    soup = bs(page.content, 'html.parser')
    all_body_content = soup.find_all("div", {"class" : "BodyContent"})
    company_code = soup.find_all("a", {"class" : "ab1"})
    for com in all_body_content:
        code = com.find_all("a")
        for only_code in code:
            print(only_code.text.strip())
        
    # for code in company_code:
    #     print(code.text.strip())
    return HttpResponse("get the code")