from django.http import HttpResponse
from django.shortcuts import render
from setuptools import Require

class Theme :
    
    def url(request, menu, pages):
        url = 'theme'
        html = 'XXX1'
        print("menu : ",menu)
        print("page : ",pages)
        
        context = {
            'url': url,
            'menu': menu,
            'pages': pages,
        }
        
        if (menu == "index" or menu == "home") and pages == "x":   
            return render(request, './'+url+'/game/index.html', context)
        elif menu == "main" and pages == "x":
            return render(request, './'+url+'/game/main.html', context)
        elif menu == "pages" :
            if pages == "1" :
                return render(request, './'+url+'/game/'+menu+'/1_categories-list.html', context)
            elif pages == "2" :
                return render(request, './'+url+'/game/'+menu+'/2_categories-grid.html', context)
            elif pages == "3" :
                return render(request, './'+url+'/game/'+menu+'/3_typography.html', context)
            elif pages == "4" :
                return render(request, './'+url+'/game/'+menu+'/4_details-post-default.html', context)
            elif pages == "5" :
                return render(request, './'+url+'/game/'+menu+'/5_details-post-gallery.html', context)
            elif pages == "6" :
                return render(request, './'+url+'/game/'+menu+'/6_details-post-review.html', context)
            elif pages == "7" :
                return render(request, './'+url+'/game/'+menu+'/7_contact.html', context)
            else : 
                # return HttpResponse("개발 진행중 2022.02.22 "+menu)
                return render(request, './'+url+'/game/404.html', context)
        else : 
            # return HttpResponse("개발 진행중 2022.02.22 "+menu)
            return render(request, './'+url+'/game/404.html', context)
        