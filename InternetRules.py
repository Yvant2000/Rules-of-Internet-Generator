

with open ("Rules of internet.txt","r",errors='ignore') as txt :
    text = txt.read ()

r = text.split ("\n\n")




def get_my_rule (search,rules) :
    
    rule = "No rules have been found. No exeptions."
    about = []
    other = []
    a = 0

    for thing in rules :
        ok = thing.replace("â™¥","♥").replace("â™¦","♦").replace ("Î»","λ").replace("Å‘","ő").replace("Ã¶","ö").replace("Ð˜","И").replace("â˜¢","☢").replace ("âˆž","∞").replace ("Î©","Ω").replace ("â€™","'").replace ("Ë™suoá´‰Ê‡dÇÉ”xÇ oN","˙suoᴉʇdǝɔxǝ oN")
        #ok = thing.encode('latin1','replace').decode('utf-8','ignore')
        ok = ok.replace ("Chuck Norris","(Chuck Norris)")
        element = ("@" + ok + "@")
        

        if ("@" + search + ". ") in element and a == 0 :
            rule = ok
            a = 1

        elif ("@" + search + ".") in element and not ok == rule :
            other.append (ok)
            
        else :
            simple = element.replace ("."," ").replace ("!"," ").replace ("("," ").replace (")"," ").replace ("#"," ").replace (","," ")
            if (" " + search.replace ("."," ") + " ") in simple and not (ok == rule or ok in other) and not ("." + search + "." ) in element :about.append (ok)

            
            
    print ("\n\n\n___Rule : " + search +"___\n")
    print (rule)

    if not other == [] :
        
        print ("\n___Other Rules :___\n")
        for i in range (len(other)) : print (other[i])
        
    if not about == [] :
        print ("\n___Related rules :___\n")
        for i in range (len(about)) : print (about[i])

while True :
    s = ""
    while s == "" : s = input("\n\n\n___Type here the rule (or keyword) you are looking for :___\n\n--> rule ")
    get_my_rule (s,r)
    input("\n\n(press enter)\n")
