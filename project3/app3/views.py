from django. http import  HttpResponse
def showIndex(request) :
    message='''
             <html>
                 <body bgcolor="red">
                 
                    <h1 style = "color:white"> 
                                   <font size="8">
                    
                    welcome to django class
                    </font>
                    
                    </h1>
                    
                  
                  </body>
             </html>
    '''
    return HttpResponse(message)