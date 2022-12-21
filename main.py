# An example chatbot: weather themed

weather = input("What is the weather like today? ")

if weather.lower() == "sunny" or weather.lower() == "hot":
    print("Great. I like the sun, but I hope it's not too hot.") 
elif weather.lower() == "rainy" or weather.lower()== "raining":
    print("I better take my umbrella with me when I go out")
else:
    response = input("Oh. Will I need a coat today? ")
    if response.lower() =="yes":
        print("Good thing you told me")
    elif response.lower() =="no":
        print("I'll leave it at home then")
    else:
        print("Ok")


