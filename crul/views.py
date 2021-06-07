from django.shortcuts import render
from bitlyshortener import Shortener
import requests
from .models import LinkCONTAINER
from django.contrib import messages
# Create your views here.

def crul_check(request):
	all_data = LinkCONTAINER.objects.all()
	if request.method =="POST":
		headers = {
		    'Authorization': 'Bearer 0456afc0a7bc25171f29a735616cfe3d9c8e0904',
		    'Content-Type': 'application/json',
		}

		data = { 
				"long_url":request.POST.get("link_short_input"),
		 		"domain": "bit.ly",
		 		"group_guid": "Bl655fA0nGi",
		 		
		 		}
		print(data)

		response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)
		# print('-----------------------------------',response.__dict__)
		value_single = response.json()
		print('This is url you have got-----------------------------------',value_single["link"])
		check_link_first = LinkCONTAINER.objects.filter(long_url=data['long_url']).first()
		if check_link_first:
			messages.error(request,"Url already present in Database")
			return render(request,'index.html',{'check_link_first':check_link_first})
		else:
			url_contain = LinkCONTAINER(long_url=data['long_url'],short_url=value_single["link"])
			url_contain.save()
			messages.success(request,"Url shorten successfully")



	return render(request,'index.html',{'all_data':all_data})



# def crul_check(request):
# 	if request.method == "POST":
# 		tokens_pool = ['0456afc0a7bc25171f29a735616cfe3d9c8e0904']
# 		shortener = Shortener(tokens=tokens_pool, max_cache_size=128)
# 		url = []
# 		get_url = request.POST.get('link_short_input')
# 		print("-This is get_url----------",get_url)
# 		if get_url == "":
# 			messages.error(request,"Please enter url in given field")
# 		else:
# 			url.append(get_url)
# 			print('THIS IS URL-------',url)
# 			sort_url = shortener.shorten_urls(url)
# 			for value in sort_url:
# 				print("sort url------------------------------------: ",value)
# 				if value.startswith('htt'):
# 					# url_contain = LinkCONTAINER(long_url=get_url,short_url=value)
# 					check_link_first = LinkCONTAINER.objects.filter(long_url=get_url).first()
# 					if check_link_first:
# 						messages.error(request,"Url already present in Database")
# 						return render(request,'index.html',{'check_link_first':check_link_first})
# 					else:
# 						url_contain.save()
# 						messages.success(request,"Url shorten successfully")
# 	return render(request,'index.html')