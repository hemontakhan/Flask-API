from flask import Flask,jsonify,request

api = Flask(__name__)

contacts=[
   {
       "id" : 1,
       "name" : "name",
       "number" : "number",
        "done" : False
   },
   {
       "id" : 2,
       "name" : "name",
       "number" : "number",
       "done" : False
   }

]

@api.route('/')
def Namaste():
  return 'Namaste'

@api.route('/add-contact', methods=['POST'])
def add_contact():
 if not request.json:
      return jsonify({
          "status" : "error",
          "message" : "add your contacts"
      },400)

 contact=[
     {
        "id": contacts[-1]['id']+1,
        "name": request.json("name"),
        "number": request.json.get("number",""),
        "done" : False
     }
 ]

 contacts.append(contact)
 return jsonify({
    "status": "Succesful",
    "message" : "Contact added successfully"
})

@api.route('/view-contact')
def view_contact():
    return jsonify({
        "data" : contacts
    })

if __name__ == '__main__':
    api.run(debug=True)
