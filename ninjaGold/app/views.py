from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    #initialize
    if ('count' not in request.session):
        request.session['count'] = 0
        request.session['log'] = []
        request.session['color'] = []

    return render(request, "index.html")

def process_money(request):
    winloss = 0

    if (request.POST['crypto'] == "bitcoin"):
        winloss = random.randint(-10,2)
        if (winloss < 0):
            #note: the .insert(0,value) is used here instead of append because we are using flexbox in the reverse direction. So we need to prepend values instead of apend them and we do that by inserting into the 0th position
            request.session['log'].insert(0,[f"Whoops! There was a fork and you lost {winloss} Bitcoin!", 'red'])
        elif (winloss > 0):
            request.session['log'].insert(0,[f"Nice! Mined {winloss} Bitcoin!", 'green'])
        else:
            request.session['log'].insert(0,["Sorry! You didn't find any Bitcoin this time!", 'gray'])
        request.session['count'] += winloss
        
    elif (request.POST['crypto'] == "ethereum"):
        winloss = random.randint(-100,100)
        if (winloss < 0):
            request.session['log'].insert(0,[f"Whoops! There was a fork and you lost {winloss} Ethereum!",'red'])
        elif (winloss > 0):
            request.session['log'].insert(0,[f"Nice! Mined {winloss} Ethereum!", 'green'])
        else:
            request.session['log'].insert(0,["Sorry! You didn't find any Ethereum this time!", 'gray'])
        request.session['count'] += winloss
    elif (request.POST['crypto'] == "rpl"):
        winloss = random.randint(-500,400)
        if (winloss < 0):
            request.session['log'].insert(0,[f"Whoops! There was a fork and you lost {winloss} Ripple!",'red'])
        elif (winloss > 0):
            request.session['log'].insert(0,[f"Nice! Mined {winloss} Ripple!",'green'])
        else:
            request.session['log'].insert(0,["Sorry! You didn't find any Ripple this time!",'gray'])
        request.session['count'] += winloss
    elif (request.POST['crypto'] == "chainlink"):
        winloss = random.randint(-200,200)
        if (winloss < 0):
            request.session['log'].insert(0,[f"Whoops! There was a fork and you lost {winloss} Chainlink!",'red'])
        elif (winloss > 0):
            request.session['log'].insert(0,[f"Nice! Mined {winloss} Chainlink!", 'green'])
        else:
            request.session['log'].insert(0,["Sorry! You didn't find any Chainlink this time!", 'gray'])
        request.session['count'] += winloss
    

    return  redirect ('/')

def clear(request):
    request.session.clear()

    return redirect('/')