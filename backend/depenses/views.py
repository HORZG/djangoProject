
from mongo_connection import db  # Import the db object from mongo_connection.py
from django.shortcuts import render, redirect
from datetime import datetime
from bson.objectid import ObjectId  # Import ObjectId for MongoDB document ID handling



def gotoadddepense(request):
    return render(request, 'adddepense.html')
# FONCTion création
def adddepense(request):
    if request.method == 'POST':
        # Get data from the form
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        current_date_and_time = datetime.now()
        createdAt = current_date_and_time.strftime("%Y-%m-%d %H:%M:%S")
        user_email = request.POST.get('userEmail')  # Get the user email 

        
        # Basic validation (you can expand this as needed)
        if not all([title, description, amount, createdAt,user_email]):
            return render(request, 'adddepense.html', {'error': 'All fields are required.'})
        else:
            depense_data = {
            'title': title,
            'description': description,
            'amount': amount,
            'createdAt': createdAt,
            'userEmail': user_email,
             }

        db.depenses.insert_one(depense_data)
        return redirect('depenses')  # Render registration form if GET request


def alldepenses(request):  # Add request parameter here
    
    all_depenses = db.depenses.find()  # Retrieve all depenses from MongoDB
    
    # Create a list of depenses with renamed _id
    depenses_list = []
    for dep in all_depenses:
        depense_data = {
            'id': str(dep['_id']),  # Rename _id to id and convert ObjectId to string
            'title': dep['title'],
            'description': dep['description'],
            'amount': dep['amount'],
            'createdAt': dep['createdAt'],
            
        }
        depenses_list.append(depense_data)
    return render(request, 'depenses.html', {'depenses': depenses_list})

def delete_depense(request, depense_id):
    
    db.depenses.delete_one({'_id': ObjectId(depense_id)})
    return redirect('depenses')  


def gotoupdate(request):
    return render(request, 'updatedepense.html')
    

def update_depense(request, depense_id):
    depense = db.depenses.find_one({'_id': ObjectId(depense_id)})  

    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        # maj depense
        db.depenses.update_one(
            {'_id': ObjectId(depense_id)},
            {'$set': {
                'title': title,
                'description': description,
                'amount': amount,
                'createdAt': depense['createdAt'],  # Keep the original createdAt value
            }}
        )

        return redirect('depenses')  # Redirection à toues les dépenses

    return render(request, 'updatedepense.html', {'depense': depense}) 