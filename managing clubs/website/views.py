from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from  .forms  import SignUpForm
from .models import workers ,Worker
from .models import workers ,Worker, retrieve_data,call_insert_category_procedure as addCategorys,call_insert_club_procedure ,call_insert_coach_procedure as addCoaches,call_insert_contract_procedure as addConracts,call_insert_worker_procedure as addWorkers ,call_insert_player_info as addPInfo,call_insert_player_procedure as addPlayer
from .models import call_delete_from_table_procedure as deleteTable ,call_update_table_values_procedure as updateTable 

def home(request):
    # Check to if loggin in
    clubs, coaches, categories, contracts, players, player_infos, workers = retrieve_data()

    if request.method == 'POST':
       username = request.POST['Username']
       passwd = request.POST['password']
       #Authenticate

       user = authenticate(request, username=username, password=passwd)
       if user is not None:
         login(request,user)
         messages.success(request,"You Have Been Logged In") 
         return redirect('home')
       else:
          messages.success(request,"Error please try again")
   
    return render(request,'home.html',{'players':players})


def playerInfo(request):
    # Check to if loggin in
    clubs, coaches, categories, contracts, players, player_infos, workers = retrieve_data()

    if request.method == 'POST':
       username = request.POST['Username']
       passwd = request.POST['password']
       #Authenticate

       user = authenticate(request, username=username, password=passwd)
       if user is not None:
         login(request,user)
         messages.success(request,"You Have Been Logged In") 
         return redirect('home')
       else:
          messages.success(request,"Error please try again")
   
    return render(request,'player_info.html',{'player_infos':player_infos})

def loginUser(request):
   pass

def logoutUser(request):
   logout(request)
   messages.success(request,"You Have Been Logged Out...")
   return redirect('home')

def registerUser(request):

   if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         #authenticate and log in 
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         user = authenticate(username=username,password=password)
         login(request,user)
         messages.success(request,'You Have Successfully Registered!')
         return redirect('home')
   else:
         form = SignUpForm()

         return render(request,'register.html',{'form':form})
   
   return render(request,'register.html',{'form':form})


def delete(request , pk , tableName ,columnName):
   if request.user.is_authenticated:
      deleteTable(tableName,columnName,'=',pk)
      messages.success(request, "Record Deleted Successfully...")
      return redirect('home')
   else:
      messages.success(request, "You Must Be Logged In To Do That...")
      return redirect('home')



def AddPlayer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        club = request.POST.get('club id')
        category = request.POST.get('category id')
      

        addPlayer(name,surname,club,category)
        
        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You added new recorod successfully")
        return redirect('home')   
    return render(request, 'add.html')


def updatePl(request ,pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        club = request.POST.get('club id')
        category = request.POST.get('category id')
        

        #table_name, column_name, new_value, condition_column, condition_operator, condition_value
        if name:
          updateTable("player","_NAME",name,"PLAYER_ID","=",pk)
        if surname:
          updateTable("player","SURNAME",surname,"PLAYER_ID","=",pk)
        if club:
          updateTable("player","CLUB_ID",club,"PLAYER_ID","=",pk)
        if category:
           updateTable("player","CATEGORY_ID",category,"PLAYER_ID","=",pk)


        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You have successfully updated the record.")
        return redirect('home')   
    return render(request, 'updatePl.html',{'pk':pk})


def updateInfo(request ,pk):
    if request.method == 'POST':
        postion = request.POST.get('postion')
        foot = request.POST.get('foot')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        goals = request.POST.get('goals')
        assists = request.POST.get('assists')
        matches = request.POST.get('matches')
        yellow_card = request.POST.get('yellow_card')
        red_card = request.POST.get('red_card')

        
        #player_id, position, foot, height, weight, goals, assists, matches, yellow_card, red_card
        #table_name, column_name, new_value, condition_column, condition_operator, condition_value
        if postion:
          updateTable("player_info","POSITION",postion,"PLAYER_ID","=",pk)
        if foot:
          updateTable("player_info","FOOT",foot,"PLAYER_ID","=",pk)
        if height:
          updateTable("player_info","HEIGHT",height,"PLAYER_ID","=",pk)
        if weight:
           updateTable("player_info","WEIGHT",weight,"PLAYER_ID","=",pk)
        if goals:
           updateTable("player_info","GOALS",goals,"PLAYER_ID","=",pk)
        if assists:
           updateTable("player_info","ASSISTS",assists,"PLAYER_ID","=",pk)
        if matches:
           updateTable("player_info","MATCHES",matches,"PLAYER_ID","=",pk)
        if yellow_card:
           updateTable("player_info","YELLOW_CARD",yellow_card,"PLAYER_ID","=",pk)

        if red_card:
           updateTable("player_info","RED_CARD",red_card,"PLAYER_ID","=",pk)



        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You have successfully updated the record.")
        return redirect('playerInfo')   
    return render(request, 'updateInfo.html',{'pk':pk})

def updateClub(request ,pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        number_of_players = request.POST.get('number_of_players')
        cups = request.POST.get('cups')
        stadium = request.POST.get('stadium')
        date_of_establishment = request.POST.get('date_of_establishment')
      # CLUB_ID int AI PK 
      # _NAME varchar(255) 
      # CUPS int 
      # NUMBERS_OF_PLAYERS int 
      # STADIUM varchar(255) 
      # DOE
         # club_id, name, number_of_players, cups, stadium, date_of_establishment
        #table_name, column_name, new_value, condition_column, condition_operator, condition_value
        if name:
          updateTable("club","_NAME",name,"CLUB_ID","=",pk)
        if number_of_players:
          updateTable("club","NUMBERS_OF_PLAYERS",number_of_players,"CLUB_ID","=",pk)
        if cups:
          updateTable("club","CUPS",cups,"CLUB_ID","=",pk)
        if stadium:
           updateTable("club","STADIUM",stadium,"CLUB_ID","=",pk)
        if date_of_establishment:
           updateTable("club","DOE",date_of_establishment,"CLUB_ID","=",pk)


        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You have successfully updated the record.")
        return redirect('clubs')   
    return render(request, 'updateClub.html',{'pk':pk})

def addInfos(request):
    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        position = request.POST.get('position')
        foot = request.POST.get('foot')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        goals = request.POST.get('goals')
        assists = request.POST.get('assists')
        matches = request.POST.get('matches')
        yellow_card = request.POST.get('yellow_card')
        red_card = request.POST.get('red_card')

        
        #player_id, position, foot, height, weight, goals, assists, matches, yellow_card, red_card
        #table_name, column_name, new_value, condition_column, condition_operator, condition_value
        addPInfo(player_id,position,foot,height,weight,goals,assists,matches,yellow_card,red_card)
       


        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You Added new recorod successfully")
        return redirect('playerInfo')   
    return render(request, 'addInfos.html')


def clubs(request):
    
    # Check to if loggin in
    clubs, coaches, categories, contracts, players, player_infos, workers = retrieve_data()

    if request.method == 'POST':
       username = request.POST['Username']
       passwd = request.POST['password']
       #Authenticate

       user = authenticate(request, username=username, password=passwd)
       if user is not None:
         login(request,user)
         messages.success(request,"You Have Been Logged In") 
         return redirect('home')
       else:
          messages.success(request,"Error please try again")
   
    return render(request,'clubs.html',{'clubs':clubs})

def addClub(request ):
    if request.method == 'POST':
        name = request.POST.get('name')
        number_of_players = request.POST.get('number_of_players')
        cups = request.POST.get('cups')
        stadium = request.POST.get('stadium')
        date_of_establishment = request.POST.get('date_of_establishment')
      # CLUB_ID int AI PK 
      # _NAME varchar(255) 
      # CUPS int 
      # NUMBERS_OF_PLAYERS int 
      # STADIUM varchar(255) 
      # DOE
         # club_id, name, number_of_players, cups, stadium, date_of_establishment
        #table_name, column_name, new_value, condition_column, condition_operator, condition_value
     
        call_insert_club_procedure(name,cups,number_of_players,stadium,date_of_establishment)

        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You Added new recorod successfully")
        return redirect('clubs')   
    return render(request, 'addClub.html')

def coach(request):
    
    # Check to if loggin in
    clubs, coaches, categories, contracts, players, player_infos, workers = retrieve_data()

    if request.method == 'POST':
       username = request.POST['Username']
       passwd = request.POST['password']
       #Authenticate

       user = authenticate(request, username=username, password=passwd)
       if user is not None:
         login(request,user)
         messages.success(request,"You Have Been Logged In") 
         return redirect('home')
       else:
          messages.success(request,"Error please try again")
   
    return render(request,'coach.html',{'coaches':coaches})

def updateCoach(request ,pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        cups = request.POST.get('cups')
        experience = request.POST.get('experience')
        age = request.POST.get('age')
        club = request.POST.get('club_id')
        category = request.POST.get('category_id')
      # CLUB_ID int AI PK 
      # _NAME varchar(255) 
      # CUPS int 
      # NUMBERS_OF_PLAYERS int 
      # STADIUM varchar(255) 
      # DOE
         # club_id, name, number_of_players, cups, stadium, date_of_establishment
        #table_name, column_name, new_value, condition_column, condition_operator, condition_value
        if name:
          updateTable("coach","_NAME",name,"COACH_ID","=",pk)
        if surname:
          updateTable("coach","SURNAME",surname,"COACH_ID","=",pk)
        if cups:
          updateTable("coach","NUMBER_OF_CUPS",cups,"COACH_ID","=",pk)
        if age:
           updateTable("coach","_OLD",age,"COACH_ID","=",pk)
        if experience:
           updateTable("coach","EXPERIENCE",experience,"COACH_ID","=",pk)
        if club:
           updateTable("coach","CLUB_ID",club,"COACH_ID","=",pk)
        if category:
           updateTable("coach","CATEGORY_ID",category,"COACH_ID","=",pk)


        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You have successfully updated the record.")
        return redirect('coach')   
    return render(request, 'updateCoach.html',{'pk':pk})


def addCoach(request ):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        cups = request.POST.get('cups')
        experience = request.POST.get('experience')
        age = request.POST.get('age')
        club = request.POST.get('club_id')
        category = request.POST.get('category_id')
      # CLUB_ID int AI PK 
      # _NAME varchar(255) 
      # CUPS int 
      # NUMBERS_OF_PLAYERS int 
      # STADIUM varchar(255) 
        addCoaches(name,surname,age,experience,cups,club,category)


        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You Added new recorod successfully")
        return redirect('coach')   
    return render(request, 'addCoach.html')

def worker(request):
    
    # Check to if loggin in
    clubs, coaches, categories, contracts, players, player_infos, workers = retrieve_data()

    if request.method == 'POST':
       username = request.POST['Username']
       passwd = request.POST['password']
       #Authenticate

       user = authenticate(request, username=username, password=passwd)
       if user is not None:
         login(request,user)
         messages.success(request,"You Have Been Logged In") 
         return redirect('home')
       else:
          messages.success(request,"Error please try again")
   
    return render(request,'worker.html',{'workers':workers})

def addWorker(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        occupation = request.POST.get('occupation')
        salary = request.POST.get('salary')
        tel = request.POST.get('tel')
        club = request.POST.get('club_id')
      # CLUB_ID int AI PK 
      # _NAME varchar(255) 
      # CUPS int 
      # NUMBERS_OF_PLAYERS int 
      # STADIUM varchar(255) 
      # worker_id, name, surname, occupation, salary, tel, club_id
        addWorkers(name,surname,occupation,salary,tel,club)


        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You Added new recorod successfully")
        return redirect('worker')   
     return render(request, 'addWorker.html')


def updateWorker(request ,pk):
     if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        occupation = request.POST.get('occupation')
        salary = request.POST.get('salary')
        tel = request.POST.get('tel')
        club = request.POST.get('club_id')
    
        if name:
          updateTable("worker","_NAME",name,"WORKER_ID","=",pk)
        if surname:
          updateTable("worker","SURNAME",surname,"WORKER_ID","=",pk)
        if occupation:
          updateTable("worker","OCCUPATION",occupation,"WORKER_ID","=",pk)
        if salary:
           updateTable("worker","SALARY",salary,"WORKER_ID","=",pk)
        if tel:
           updateTable("worker","TEL",tel,"WORKER_ID","=",pk)
        if club:
           updateTable("worker","CLUB_ID",club,"WORKER_ID","=",pk)




        
        
        messages.success(request,"You have successfully updated the record.")
        return redirect('worker')   
     return render(request, 'updateWorker.html',{'pk':pk})

def category(request):
    
    # Check to if loggin in
    clubs, coaches, categories, contracts, players, player_infos, workers = retrieve_data()

    if request.method == 'POST':
       username = request.POST['Username']
       passwd = request.POST['password']
       #Authenticate

       user = authenticate(request, username=username, password=passwd)
       if user is not None:
         login(request,user)
         messages.success(request,"You Have Been Logged In") 
         return redirect('home')
       else:
          messages.success(request,"Error please try again")
   
    return render(request,'category.html',{'categories':categories})

    
def addCategory(request):
     if request.method == 'POST':
        level = request.POST.get('level')
        cups = request.POST.get('cups')
        number_of_players = request.POST.get('number_of_players')
        club_id = request.POST.get('club_id')
       
      # category_id, level, cups, number_of_players, club_id
      # CLUB_ID int AI PK 
      # _NAME varchar(255) 
      # CUPS int 
      # NUMBERS_OF_PLAYERS int 
      # STADIUM varchar(255) 
      # worker_id, name, surname, occupation, salary, tel, club_id
        addCategorys(level, cups, number_of_players, club_id)


        # Process the data (e.g., save to database, perform some action, etc.)
        # For demonstration, we'll just return a response with the data.
        
        messages.success(request,"You Added new recorod successfully")
        return redirect('category')   
     return render(request, 'addCategory.html')

def updateCategory(request ,pk):
     if request.method == 'POST':
        level = request.POST.get('level')
        cups = request.POST.get('cups')
        number_of_players = request.POST.get('number_of_players')
        club_id = request.POST.get('club_id')
      
        if level:
          updateTable("category","_LEVEL",level,"CATEGORY_ID","=",pk)
        if cups:
          updateTable("category","CUPS",cups,"CATEGORY_ID","=",pk)
        if number_of_players:
          updateTable("category","NUMBERS_OF_PLAYERS",number_of_players,"CATEGORY_ID","=",pk)
        if club_id:
           updateTable("category","CLUB_ID",club_id,"CATEGORY_ID","=",pk)
     




        
        
        messages.success(request,"You have successfully updated the record")
        return redirect('category')   
     return render(request, 'updateCategory.html',{'pk':pk})

def contract(request):
    
    # Check to if loggin in
    clubs, coaches, categories, contracts, players, player_infos, workers = retrieve_data()

    if request.method == 'POST':
       username = request.POST['Username']
       passwd = request.POST['password']
       #Authenticate

       user = authenticate(request, username=username, password=passwd)
       if user is not None:
         login(request,user)
         messages.success(request,"You Have Been Logged In") 
         return redirect('home')
       else:
          messages.success(request,"Error please try again")
   
    return render(request,'contract.html',{'contracts':contracts})

def updateContract(request ,pk):
     if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        penal_clause = request.POST.get('penal_clause')
        salary = request.POST.get('salary')
       

        if start_date:
          updateTable("contract","START_DATE",start_date,"PLAYER_ID","=",pk)
        if end_date:
          updateTable("contract","END_DATE",end_date,"PLAYER_ID","=",pk)
        if penal_clause:
          updateTable("contract","PENAL_CLAUSE",penal_clause,"PLAYER_ID","=",pk)
        if salary:
           updateTable("contract","SALARY",salary,"PLAYER_ID","=",pk)
     


        
        
        messages.success(request,"You have successfully updated the record")
        return redirect('contract')   
     return render(request, 'updateContract.html',{'pk':pk})


def addContract(request):
     if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        penal_clause = request.POST.get('penal_clause')
        salary = request.POST.get('salary')
        player_id = request.POST.get('player_id')
        club_id = request.POST.get('club_id')
      
        addConracts(player_id, start_date, end_date, penal_clause,salary,club_id)


     
        
        messages.success(request,"You Added new recorod successfully")
        return redirect('contract')   
     return render(request, 'addContract.html')