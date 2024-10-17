from django.shortcuts import render,HttpResponse
from . import d
i = -1
scorel = 0
timer = 21
def home(request):
    x = True
    
    while x:
        global i
        if i <=16:
            i += 1
            return render(request,'home.html',{'word':d.synonyms[i]['word'],'value1':d.synonyms[i]['option'][0],'value2':d.synonyms[i]['option'][1],'value3':d.synonyms[i]['option'][2],'value4':d.synonyms[i]['option'][3],'score':scorel,'left':timer})
            



def check(request):
     global i,scorel
     p = 0
     global timer
     clicked_button = request.POST.get('button', None)
     if clicked_button == '1':
           p = 1
     elif clicked_button == '2':
           p = 2
     elif clicked_button == '3':
           p = 3
     elif clicked_button == '4':
           p = 4
            
     if p == d.synonyms[i]['answer']:
      scorel += 1
     timer -= 1
     if i <=19:
            i +=1
            
            return render(request,'home.html',{'word':d.synonyms[i]['word'],'value1':d.synonyms[i]['option'][0],'value2':d.synonyms[i]['option'][1],'value3':d.synonyms[i]['option'][2],'value4':d.synonyms[i]['option'][3],'score':scorel,'left':timer})
     else:
         
            p = int(scorel/(21/100))
            if p < 30:
               
                 return render(request,'afterquiz.html',{'scoreli':int(scorel/(21/100)),'photo':"sad"})
                  
            else:
                 return render(request,'afterquiz.html',{'scoreli':int(scorel/(21/100)),'photo':"congra"})
   