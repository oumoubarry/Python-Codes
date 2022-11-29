select_language = input("enter the language you want to tranlate \n")
	    
# Creating the dictionary english to french
english_french ={
    "beauty": "beaute",
    "hapiness" : "bonheur",
    "heaven" : "paradis",
    "plum" : "prune",
    "pineapple " : "ananas",
    "grapefruit" : "pamplemousse",
    "smile" : "sourire",
    "thank you" : "merci",
    "goodbye" : "aurevoir",
    "beach" : "plage",
    "meat" : "viande"
    }
# Creating the dictionary french to english	    
french_english ={
    "beaute": "beauty",
    "bonheur": "hapiness",
    "amour": "love",
    "paradis": "heaven",
    "prune": "plum",
    "ananas": "pineapple ",
    "pamplemousse": "grapefruit",
    "sourire": "smile" ,
    "merci": "thank you",
    "aurevoir": "goodbye",
    "plage": "beach",
    "viande": "meat"
    }
    	    
# Defining the function User selecting French
if select_language=="french":
    def translation(english_word):
        if english_word in english_french:
            print(translate)
        else:
            print(f"{english_word}  not found in current dictionary")

    english_word = input("Enter english word to lookup \n")
    translate = english_french.get(english_word)
# Recalling  the function
    translation(english_word)
    
# Defining the function when User selecting English
elif select_language=="english":
    def translation(french_word):
        if french_word in french_english:
            print(translate)
        else:
            print(f"{french_word}  not found in current dictionary")
	        
    french_word = input("Enter french word to lookup\n")
    translate = french_english.get(french_word)
# Recalling the function
    translation(french_word)
    
else:
    print("Unable to locate desired language in current dictionary")