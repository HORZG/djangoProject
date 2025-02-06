from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from mongo_connection import db  # Import the db object from mongo_connection.py


def register(request):
    if request.method == 'POST':
        # Get data from the form
        pseudo = request.POST.get('pseudo')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Basic validation (you can expand this as needed)
        if not all([pseudo, firstname, lastname, telephone, email, password]):
            return render(request, 'register.html', {'error': 'All fields are required.'})

        # Check if the user already exists
        if db.users.find_one({'email': email}):  # Check if email exists in the users collection
            return render(request, 'register.html', {'error': 'Email already exists.'})

        # Hash the password before storing it
        hashed_password = make_password(password)

        # Create and save the new user document
        user_data = {
            'pseudo': pseudo,
            'firstname': firstname,
            'lastname': lastname,
            'telephone': telephone,
            'email': email,
            'password': hashed_password  # Store hashed password
        }

        db.users.insert_one(user_data)  # Insert user data into users collection

        return redirect('/api/login/')  # Redirect to login page after successful registration

    return render(request, 'register.html')  # Render registration form if GET request


def homepage(request):
    return render(request, 'home.html')


def gotologinpage(request):
    return render(request, 'login.html')


def login_view(request):  # Renamed to avoid conflict with Django's built-in login function
    if request.method == 'POST':
        email = request.POST.get('email')
      
        hashed_password = request.POST.get('password')
        
       
        #
        user_data = db.users.find_one({'email': email})
        
       
        
        # 
        if user_data['email'] == email:
         
            if check_password(hashed_password, user_data['password']):
                print("Login successful")  
                request.session['user_email'] = email
               
                if  (request.session['user_email']):
                 print ('yess')
            

                
            # token à mettre en place
            return redirect('depenses')
            
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'depenses.html')  # Render login page for GET requests


    


def logout_view(request):
    # Clear specific session data
    del request.session['user_email']
    
    # Or logout entirely
    request.session.flush()  # Clears all session data
    
    return redirect('login')
