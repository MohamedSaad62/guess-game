from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random as rd
users = {}
class user:
    def __init__(self):
        self.random = 0
        self.data = []
        self.len = 0
        self.stat = 0
    def set_random(self):
       
        self.random = rd.randrange(1,501)


def index(request):
    req_headers = request.META
    x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for_value:
        ip_addr = x_forwarded_for_value.split(',')[-1].strip()
    else:
        ip_addr = req_headers.get('REMOTE_ADDR')
    ip_addr = str(ip_addr)    
    if ip_addr not in users.keys():
        users[ip_addr] = user()
        users[ip_addr].set_random()
    
    
    if request.method == 'POST':    
        if 'guess' in request.POST:
            guess = int (request.POST['guess'])
            users[ip_addr].data.append(guess)
            users[ip_addr].len += 1
            if guess == users[ip_addr].random:
                users[ip_addr].stat = 1
        elif 'again' in request.POST:
            users[ip_addr].set_random()
            users[ip_addr].data.clear()
            users[ip_addr].stat = 0
            users[ip_addr].len = 0
            

    context = {}
    context['user'] = users[ip_addr]   
    return render(request, 'game1.html', context)
