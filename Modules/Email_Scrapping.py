try:
    from GUI.Config import *
except BaseException:
    #??modify the sys path?? but not important now.
    from Config import *

    
class GetEmail(Variables):
    def __init__(self):
        Variables.__init__(self)
        pass

    def test(self):
        return "Hello World"

    #--Single Email--
    def get(self, url):
        
        #---Online Request---
        while True:
            try:
                response = requests.get(url)
                break
            except BaseException as e:
                print(e)
                counter += 1
                if counter == 10:
                    return """
                    Error while getting the server response, Please contact the provider
                    Please Make sure you have good and stable internet connection, then retry"""
                    break
        
        
        #---To Text---
        while True:
            try:
                textHtml = response.text
                break
            except BaseException as e:
                print(e)
                counter += 1
                if counter == 10:
                    return """Error while getting the HTML in Text Format, Please contact the provider
                    Propably this website can't be scrapped"""
                    break

        #---Parsing---
        while True:
            try:
                parsedHtml = BeautifulSoup(textHtml, 'html.parser')
                break
            except BaseException as e:
                print(e)
                counter += 1
                if counter == 10:
                    return """Error while parsing the HTML, Please contact the provider
                    Please Check the log file of this operation"""
                    break
        
        #--Getting Data--
        while True:
            try:
                #--Rgx Trial--
                for email2 in re.findall(EMAIL_REGEX, textHtml):
                    if email2 not in tempList and len(email2) >=10: 
                        tempList.append(email2) 
                #--scrapping trial--                        
                for a in parsedHtml.find_all('a'):
                    #--href trial--
                    aHref = str(a.get('href'))
                    if aHref.startswith('mailto'):
                        email = aHref[7:]
                        if email not in tempList and len(email2) >=10:
                            tempList.append(email)
                break
            except BaseException as e:
                print(e)
                counter += 1
                if counter == 10:
                    return "Error while Getting the data"
                    break
        #--Format the list--
        if len(tempList) == 0:
            return "No emails Found"
        elif len(tempList) > 0:
            emailString = str()
            for em in tempList:
                if em not in emailString:  
                    emailString = emailString + em + "\n"
        
        return emailString, tempList


    #--Multible Emails--
    def gets(self, listOfUrls):

        for url in listOfUrls:
            if 'url' in url or 'Url' in url or 'URL' in url:
                continue
            email = get(url)
            
        
        return email
    

    def readData(self, path):
        try:
            Book = load_workbook(path)
            Sheet = Book.active
            return Sheet
        except BaseException as e:
            return ""
    

    def writeData(self, listofList, path):
        try:
            Book = Workbook()
            Sheet = Book.active

            #--write--
            try:
                for row in listofList:
                    if "list" in str(type(row)):
                        Sheet.append(row)
                    else:
                        Sheet.append([row])
            except BaseException as e:
                return None
            
            #--save--
            try:
                #-make the path-
                temp = str()
                Id = int()
                for id, char in enumerate(path):
                    if char == "\\":
                        Id = id
                Path = path[:Id+1]
                #--save--
                Book.save(f"{Path}Emails.xlsx")
            except BaseException as e:
                return None
            

            return Sheet

        except BaseException as e:
            return ""
