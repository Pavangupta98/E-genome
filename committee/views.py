from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from.models import Committee
from django.http import JsonResponse

@csrf_exempt
def committeeLogin(request):
    response_json = {}
    email = json.loads(request.body.decode("utf-8"))["email"]
    print(email)
    try:
    	if request.method=="POST":
	    	if Committee.objects.filter(email=email).exisits():
	    		committee_instance = Committee.objects.filter(email=email)
	    		print(committee_instance)
	    		password = json.loads(request.body.decode("utf-8"))["password"]
	    		if str(password)== committee_instance.password:
	    			response_json["success"] = True
	    			response_json["message"] = "Successfully Loggedin."
	    		else:
	    			response_json["success"] = False
	    			response_json["message"] = "Something wrong in the password."
	    	else:
	    		response_json["success"] = False
	    		response_json["message"] = "email doesnt exiast. Kindly register first before logging in."
	    else:
	    	response_json["success"] = False
	    	response_json["message"] = "wrong method"
	  
    except Exception as e:
    	print(e)
    	message = "exception - " + e
    	response_json["success"] = False
    	response_json["message"] = message

    return JsonResponse(response_json)
    
