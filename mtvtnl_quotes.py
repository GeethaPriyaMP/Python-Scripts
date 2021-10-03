import requests,json

def getMotivationalMessage():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    res = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(res.text)
    msg =  jsonText["quoteText"] + "-" + jsonText["quoteAuthor"] 
    
    return msg


def sendQuotes():
    quote = getMotivationalMessage()
    print(quote)
    
sendQuotes()