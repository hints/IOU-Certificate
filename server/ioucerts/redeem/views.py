# Create your views here.

from django.http import HttpResponse

def home(request):
  return HttpResponse("Hello, world. You're at the poll index.")

def redeem(request, redeem_code):
  print 'code: ', redeem_code
  redeemer = request.GET.get('email', '')
  return HttpResponse("Code: " + redeem_code + '\nRedeemer: ' + redeemer)

def redeemed(request):
  email = request.GET.get('email', '')
  return HttpResponse('Getting redeemed codes for: ' + email)

def sync(email):
  email = request.GET.get('email', '')
  return HttpResponse('Syncing for: ' + email)

def create_user(request):
  email = request.GET.get('email', '')
  return HttpResponse("Created user with seed:" + email)
