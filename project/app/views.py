from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,"index.html")



def evaluate(request):
    if request.method == "POST" :
        mat = request.POST.get("maths")
        science = request.POST.get("science")
        computer = request.POST.get("comp")
        print(mat,science,computer)
        percentagemath = (int(mat)*100) / 100
        percentagescience = (int(science)*100) / 100
        percentagecomputer = (int(computer)*100) / 100
        print(percentagemath)
        print(percentagescience)
        print(percentagecomputer)
        print(type(percentagescience))

        if(percentagemath >= 33 and percentagescience >= 33 and percentagecomputer >= 33):
            overall = percentagecomputer + percentagemath + percentagescience
            aggregate = (overall*100)/300
            if aggregate < 40:
                return HttpResponse(f"Maths Marks : {mat} \n Science Marks : {science} \n Computer Marks : {computer} \n You are failed because your aggregate is less than 40%")
            else:
                return HttpResponse(f"Maths Marks : {mat} \n Science Marks : {science} \n Computer Marks : {computer} \n You are passed")   
        else:
            return HttpResponse(f"Maths Marks : {mat} \n Science Marks : {science} \n Computer Marks : {computer} \n You are failed since one sunject is less than 33%")
                
    

    return render(request,"index.html")
