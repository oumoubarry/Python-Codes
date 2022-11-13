# Language selection
select_language = input("enter the language you want to tranlate \n")

# Creating the dictionary english to french

english_french ={
"beauty": "beaute",
"hapiness" : "bonheur",
"love" : "amour",
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

# User selecting french
if select_language=="french":
    english_word = input("Enter english word to lookup \n")
    translate = english_french.get(english_word)
    if english_word in english_french:
        print(translate)
    elif english_word not in english_french:
        print(f"{english_word}  not found in current dictionary")

# User selecting english
elif select_language=="english":
    french_word = input("Enter french word to lookup\n")
    translation = french_english.get(french_word)
    if french_word in french_english:
        print(translation)
    elif french_word not in french_english:
        print(f"{french_word}  not found in current dictionary")

# if seletec language is not in the dictionary  
else:
    print("Unable to locate desired language in current dictionary")