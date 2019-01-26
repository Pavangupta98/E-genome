from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from.models import Committee
from django.http import JsonResponse

@csrf_exempt
def committeeLogin(request):
    response_json = {}
    email = request.POST.get("emlc")
    print(email)
    try:
    	if request.method=="POST":
	    	if Committee.objects.filter(email=email).exisits():
	    		committee_instance = Committee.objects.filter(email=email)
	    		print(committee_instance)
	    		password = request.POST.get("pwd2")
	    		if str(password)== committee_instance.password:
	    			response_json["success"] = True
	    			response_json["message"] = "Successfully Loggedin."
	    		else:
	    			response_json["success"] = False
	    			response_json["message"] = "Something wrong in the password."
	    	else:
	    		response_json["success"] = False
	    		response_json["message"] = "email doesnt exiast. Kindly register first before logging in."
    except Exception as e:
    	print(e)
    	message = "exception - " + e
    	response_json["success"] = False
    	response_json["message"] = message

    return JsonResponse(response_json)

@csrf_exempt
def committeeRegistration(request):
	response_json = {}
	
	try:
		if request.method == "POST":
			email = request.POST.get("eml1")
			if Committee.objects.filter(email=email).exisits():
				response_json["success"] = False
				response_json["message"] = "Please try to log in as you have already register"
			else:
				committee_instance = Committee.objects.create(email=email)
				committee_instance.password = request.POST.get("pwd3")
				committee_instance.institute_name = request.POST.get("inst")
				committee_instance.state = request.POST.get("state")
				committee_instance.city = request.POST.get("city")
				committee_instance.commmittee_name = request.POST.get("c_name")
				committee_instance.description = request.POST.get("desc")
				committee_instance.committee_type = request.POST.get("type")
				committee_instance.last2activities1 = request.Files.get("file_1")
				committee_instance.last2activities2 = request.Files.get("file_2")
				committee_instance.self_certification = request.Files.get("file_3")
				committee_instance.save()

				response_json["success"] = True
				response_json["message"] = "Successfully Registered"

		else:
			response_json["success"] = False
			response_json["message"] = "Not Post method"

	except Exception as e:
		print(e)
		message = "Exception - " + str(e)
		response_json["success"] = False
		response_json["message"] = message 

	return JsonResponse(response_json)

	