# Print out the last name of the 2nd employee.

db_resources = {"employees": [{"firstName" : "John", "lastName" : "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"fistName" : "Peter", "lastName": "Jones"}],
"owners": [{"fistName": "Jack", "lastName" : "Petter"},
            {"firstName": "Jessy", "lastName": "Petter"}]
}

print(db_resources["employees"][1]["lastName"])
