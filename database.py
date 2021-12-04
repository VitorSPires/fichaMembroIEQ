import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyC21YMoaFu6S4QKjDHGP0TzESPOMaHCuMI",
    "authDomain": "teste-6b6db.firebaseapp.com",
    "databaseURL": "https://teste-6b6db-default-rtdb.firebaseio.com",
    "projectId": "teste-6b6db",
    "storageBucket": "teste-6b6db.appspot.com",
    "messagingSenderId": "237749929559",
    "appId": "1:237749929559:web:2b0da95b466b1b840ac512"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def salvarFicha(listaMembros):
    for membro in listaMembros:
        id = db.child("LastID").child("Membros").get().val() + 1
        db.child("LastID").child("Membros").set(id)
        db.child("Membros").child(id).child('NMCompleto').set(membro[0])
        db.child("Membros").child(id).child('DTNasc').set(membro[1])
        db.child("Membros").child(id).child('Telefone').set(membro[2])
        db.child("Membros").child(id).child('Email').set(membro[3])
