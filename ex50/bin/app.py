import os
from flask import Flask, jsonify

app = Flask(__name__)
  
members = [{
                "id":1,
                "name":"john",
                "lastname": "Doe",
                "age":46,
                "gender":"Male",
                "family_id":[2,3,8,9]
                },
            {
                "id":2,
                "name":"jane",
                "lastname": "Doe",
                "age":45,
                "gender":"female",
                "family_id":[1,3]
                },
             {
                "id":3,
                "name":"jimmy",
                "lastname": "Doe",
                "age":20,
                "gender":"Male",
                "family_id":[1,2]
                },
            {
                "id":4,
                "name":"marco",
                "lastname": "Doe",
                "age":47,
                "gender":"Male",
                "family_id":[5,6]
                },
            {
                "id":5,
                "name":"janere",
                "lastname": "Doe",
                "age":48,
                "gender":"female",
                "family_id":[4,6,7]
                },
             {
                "id":6,
                "name":"jully",
                "lastname": "Doe",
                "age":22,
                "gender":"Male",
                "family_id":[4,5,7]
                },
             {
                "id":7,
                "name":"june",
                "lastname": "Doe",
                "age":5,
                "gender":"Male",
                "family_id":[3,6]
                },
             {
                "id":8,
                "name":"jean",
                "lastname": "Doe",
                "age":81,
                "gender":"Male",
                "family_id":[1]
                },
             {
                "id":9,
                "name":"ginna",
                "lastname": "Doe",
                "age":88,
                "gender":"Female",
                "family_id":[1]
                }
            
        ]

@app.route('/',methods=['GET'])

def themembers():
    return jsonify (members)
      
      
@app.route('/members/<int:member_id>',methods=['GET'])

def getmember(member_id):
    for i in members:
        if i['id'] == member_id:
        	i["family"] = map(lambda fid: get_member_simple(fid),i["family_id"])
        	return jsonify (i)

def get_member_simple(id):
	for i in members:
		if i['id'] == id:
			return i

@app.route('/membersage',methods=['GET'])			

def age():
	theages = map(lambda obj: obj['age'],members)
	theagesArray =sorted(theages)
        return jsonify(theagesArray)
		
		
        
    
    

    

  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))