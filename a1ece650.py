from __future__ import division
import re
import sys




# YOUR CODE GOES HERE
'''
def main():
    ### YOUR MAIN CODE GOES HERE

    ### sample code to read from stdin.
    ### make sure to remove all spurious print statements as required
    ### by the assignment
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        print 'read a line:', line

    print 'Finished reading input'
    # return exit code 0 on successful termination
    sys.exit(0)
'''

class line():
    
    def __init__(self,a,b,c,d):
        self.x1 = float(a)
        self.x2 = float(c)
        self.y1 = float(b)
        self.y2=  float(d)
    def gradient(self):
        try:
            return (self.y2  - self.y1) / (self.x2 - self.x1)
        except ZeroDivisionError:
            print"Zero error occured at x1", self.x1, " x2 ",self.x2
            #return     
    def equation(self):
        self.y = self.y2 - (self.gradient()*self.x2)
        return self.y
def intersection(custom_line1,custom_line2,V,Intersection_Vertex):
    '''
    The following if condition checks for intesection of 2 OverLapping Line segments of 2 different streets
    
    if(custom_line1.x1==custom_line2.x1 and custom_line1.x2==custom_line2.x2 and custom_line1.y1==custom_line2.y1 and custom_line1.y2==custom_line2.y2) :
        if((custom_line1.x1,custom_line1.y1) not in V.values()):
            V[len(V)+1] = (custom_line1.x1,custom_line1.y1)
            return V
     '''

    
    x_max_Line_1 = max(custom_line1.x1,custom_line1.x2)
    x_max_Line_2 = max(custom_line2.x1,custom_line2.x2)
    y_max_Line_1 = max(custom_line1.y1,custom_line1.y2)
    y_max_Line_2 = max(custom_line2.y1,custom_line2.y2)
    x_min_Line_1 = min(custom_line1.x1,custom_line1.x2)
    x_min_Line_2 = min(custom_line2.x1,custom_line2.x2)
    y_min_Line_1 = min(custom_line1.y1,custom_line1.y2)
    y_min_Line_2 = min(custom_line2.y1,custom_line2.y2)
    
    if(custom_line1.x1==custom_line1.x2 or custom_line2.x1==custom_line2.x2):
        if(custom_line1.x1==custom_line1.x2 and custom_line2.x1!=custom_line2.x2):
            xInt = custom_line1.x1
            L2m  = custom_line2.gradient()
            L2y1 = custom_line2.equation()
            yInt = L2m*xInt + L2y1
            if(yInt>= y_min_Line_2 and yInt <= y_max_Line_2 and yInt >= y_min_Line_1 and yInt <= y_max_Line_1):
                V,Intersection_Vertex = Vertex(xInt,yInt,custom_line1,custom_line2,V,Intersection_Vertex)
                #print "Vertix function processed in 1st condition"
        elif(custom_line1.x1!=custom_line1.x2 and custom_line2.x1==custom_line2.x2 ):
            xInt = custom_line2.x1
            L1m  = custom_line1.gradient()
            L1y1 = custom_line1.equation()
            yInt = L1m*xInt +L1y1
            if(yInt>= y_min_Line_2 and yInt <= y_max_Line_2 and yInt >= y_min_Line_1 and yInt <= y_max_Line_1):
                V,Intersection_Vertex = Vertex(xInt,yInt,custom_line1,custom_line2,V,Intersection_Vertex)
                #print "Vertix function processed in 2nd condition"
        return V,Intersection_Vertex
    else:
    
        L1x = custom_line1.x1
        L1y = custom_line1.y1    
        L1m = custom_line1.gradient()
        L1y1 = custom_line1.equation()
        L2x = custom_line2.x1
        L2y = custom_line2.y1
        L2m = custom_line2.gradient()
        L2y1= custom_line2.equation()
        if(L2m==L1m):
            "No Intersection as parallel line"
            return V,Intersection_Vertex
        xInt=(L1y1-L2y1)/(L2m-L1m)
        yInt = L1m*xInt + L1y1
        yTest = L2m*xInt + L2y1
        if(yInt==yTest and yInt>=y_min_Line_1 and yInt<= y_max_Line_1 and xInt >=x_min_Line_1 and xInt<=x_max_Line_1 and yInt>=y_min_Line_2 and yInt<= y_max_Line_2 and xInt >= x_min_Line_2 and xInt <= x_max_Line_2):
            V,Intersection_Vertex = Vertex(xInt,yInt,custom_line1,custom_line2,V,Intersection_Vertex)
            '''
            print "Vertix function processed in 3rd condition"
            print "xInt and yInt ", xInt,yInt
            print "lin1_x1 line1_y1 line1_x2 line1_y2",custom_line1.x1, custom_line1.y1, custom_line1.x2,custom_line1.y2
            print "lin2_x1 line2_y1 line2_x2 line2_y2",custom_line2.x1, custom_line2.y1, custom_line2.x2,custom_line2.y2
            '''
        else:
            print "No Intersection"
    return V,Intersection_Vertex

def same_street(V,I_V,TotalStreets,StreetList):
    Vlist = V.values()
    I_Vlist = I_V.values()
    edges =[]
    '''
    for i in range(len(I_Vlsit)):
        for k in range(len(Vlist)):
    '''
    ks = 0
    for key in I_V:
        #print "Key in  I_V", key
        ks = key
        for key in V:
            yes_edge = 0
            #print"Key in V", key
            if(V[key]!=I_V[ks]):
                #print"When V not equal to IV then V and IV = ",V[key],I_V[ks]
                for i in range(len(StreetList)):
                    for k in range(len(TotalStreets[StreetList[i]])):
                        outputt = 0
                        '''
                        print"V[key] is ",V[key]
                        print"I_V[ks] is ",I_V[ks]
                        print"TotalStreets[StreetList[i][k]] is ", TotalStreets[StreetList[i]][k]
                        '''
                        outputt = Vertix_Check(V[key],I_V[ks],TotalStreets[StreetList[i]][k])
                        if(outputt == 1):
                            break
                    if(outputt == 1):
                        #print "Both Vertices lie on the same street, vertices are V and Vintersection = ", V[key], I_V[ks] ,"Street is ",StreetList[i]
                        yes_edge = No_Vertix_Between( V[key], I_V[ks],StreetList[i],V)
                        
            if(yes_edge == 1):
                if((ks,key) not in edges and (key,ks) not in edges):
                    edges.append((ks,key))
                '''    
                if(key>ks):
                    if((ks,key) not in edges):
                        edges.append((ks,key))
                else:
                    if((key,ks) not in edges):
                        edges.append((key,ks))
                '''
    return edges
    '''
    print "Edges are ",edges
    '''           

def No_Vertix_Between(V1,IV1,StreetName,V):
    edgee = 0
    ytest = 0
    xtest = 0
    line_Check = line(IV1[0],IV1[1],V1[0],V1[1])
    x_max = max([V1[0],IV1[0]])
    x_min = min([V1[0],IV1[0]])
    y_max = max([V1[1],IV1[1]])
    y_min = min([V1[1],IV1[1]])


    if(IV1[0]==V1[0]):
        for key in V:
            xtest = (V[key][0])
            ytest = (V[key][1])
            if(xtest == IV1[0] and ytest>=y_min and ytest<=y_max):
                if(V[key] not in [V1,IV1]):
                    #print "There is a vertix in between the 2 mentioned vertices"
                    return edgee
    else:
        m = line_Check.gradient()
        yc = line_Check.equation()
        for key in V:
            xtest = (V[key][0])
            ytest = (V[key][1])
            if(xtest>=x_min and xtest<=x_max and ytest>=y_min and ytest<=y_max):
                if(V[key] not in [V1,IV1]):
                    y = m*xtest+yc
                    if(y==ytest):
                        #print "There is a vertix in between the 2 mentioned vertices"
                        return edgee

    edgee = 1
    return edgee
                  

def Vertix_Check(v1,v2,custom_line1):
    Vx = v1[0]
    Vy = v1[1]
    IVx = v2[0]
    IVy = v2[1]
    result = 0
    
    x_max = max(custom_line1.x1,custom_line1.x2)
    x_min = min(custom_line1.x1,custom_line1.x2)
    y_max = max(custom_line1.y1,custom_line1.y2)
    y_min = min(custom_line1.y1,custom_line1.y2)

    
    if(custom_line1.x1 == custom_line1.x2):
        if(Vx==custom_line1.x1 and IVx==custom_line1.x1 and Vy>=custom_line1.y1 and Vy<=custom_line1.y2 and IVy>=custom_line1.y1 and IVy<=custom_line1.y2):
            result = 1
            #print "Vertices = ",v1,v2,"Are on same street"
            return result
    elif(Vx>=x_min and Vx<=x_max and Vy>=y_min and Vy<=y_max and IVx>= x_min and IVx<=x_max and IVy>=y_min and IVy<y_max):
        m = custom_line1.gradient()
        yc = custom_line1.equation()
        if(Vy == (m*Vx + yc) and IVy == (m*IVx + yc)):
            #print "Vertices = ",v1,v2,"Are on same street"
            result = 1
            return result
    else:
        return result
        
            
    
def addStreet(cart,TotalStreets,Command,StreetNames):
    Streets=[]
    i = 1
    numSeg = int(len(cart)/2 - 1)
    for k in range(0,numSeg):
        line1 = line(cart[i],cart[i+1],cart[i+2],cart[i+3])
        Streets.append(line1)
        i = i+2
    provided = Command
    flag2 = 0
    streetlist=''
    p = 0
    while (p< len(provided)):
        if(provided[p] != '"' and  flag2 == 0):
            p = p+1
        else:
            flag2 = 1
            y=p
            while(y<len(provided)):
                streetlist += provided[y]
                y = y+1
                if(provided[y] =='"'):
                    streetlist += provided[y]
                    break
        if (flag2== 1):
            break
    streetlist = streetlist.upper()
    print "StreetList is ",streetlist

    if(streetlist in StreetNames):
        print"Error: The street you want to add already exists."
        return TotalStreets,StreetNames
    else:
        StreetNames.append(streetlist)
        TotalStreets.update({streetlist:Streets})
        return TotalStreets,StreetNames



def changeStreet(cart,TotalStreets,Command,StreetNames):
    Streets=[]
    i = 1
    numSeg = int(len(cart)/2 - 1)
    for k in range(0,numSeg):
        line1 = line(cart[i],cart[i+1],cart[i+2],cart[i+3])
        Streets.append(line1)
        i = i+2
    provided = Command
    flag2 = 0
    streetlist=''
    p = 0
    while (p< len(provided)):
        if(provided[p] != '"' and  flag2 == 0):
            p = p+1
        else:
            flag2 = 1
            y=p
            while(y<len(provided)):
                streetlist += provided[y]
                y = y+1
                if(provided[y] =='"'):
                    streetlist += provided[y]
                    break
        if (flag2== 1):
            break
    
    streetlist = streetlist.upper()
    if(streetlist not in StreetNames):
        print"Error: The street you want to change doesn't exist.First add it."
        return TotalStreets,StreetNames
    else:
        print "StreetList is ",streetlist
        TotalStreets.update({streetlist:Streets})
        return TotalStreets,StreetNames










def Vertex(xInt,yInt,custom_line1,custom_line2,V,Intersection_Vertex):
 
    
    print "Type of xIntt before rouding", type(xInt)
    print "xint before rounding", xInt
    xIntt = round(xInt,2)
    print "Type of xIntt after rouding", type(xIntt)
    print "xint after rounding", xIntt
    yIntt = round(yInt,2)
    x_1_1 = round(custom_line1.x1,2)
    x_2_1 = round(custom_line1.x2,2)
    x_1_2 = round(custom_line2.x1,2)
    x_2_2 = round(custom_line2.x2,2)
    y_1_1=  round(custom_line1.y1,2)
    y_2_1=  round(custom_line1.y2,2)
    y_1_2 = round(custom_line2.y1,2)
    y_2_2 = round(custom_line2.y2,2)

    
   
        
    if((xIntt,yIntt) not in Intersection_Vertex.values()):
        Intersection_Vertex[len(Intersection_Vertex)] = xIntt,yIntt

    
    if((xIntt,yIntt) not in V.values()):
        V[len(V)+1] = xIntt,yIntt
        
    if((x_1_2,y_1_2) not in V.values()):
        V[len(V)+1] = x_1_2,y_1_2
        
    if((x_2_2, y_2_2) not in V.values()):
        V[len(V)+1] = x_2_2, y_2_2
        
    if((x_2_1, y_2_1) not in V.values()):
        V[len(V)+1] = x_2_1, y_2_1
        
    if((x_1_1,y_1_1) not in V.values()):
        V[len(V)+1] = x_1_1,y_1_1

    return V,Intersection_Vertex
    
def keyupdate(V,Intersection_Vertex):
    keyy = 0
    intersection_with_actual_keys = {}
    for i in range(len(Intersection_Vertex)):
        keyy= [key  for (key, value) in V.items() if value == Intersection_Vertex[i]]
        keyyy = keyy[0]
        intersection_with_actual_keys.update({keyyy: Intersection_Vertex[i]})
        #print"Key is and value is ",keyyy,Intersection_Vertex[i]
    #print "intersection_with_actual_keys is ",intersection_with_actual_keys
    return intersection_with_actual_keys
        
        
    
def exCord(Command):
    provided = []
    provided = Command
    i = 0
    flag = 0

    Cord = []

    while (i< len(provided)):
        while(provided[i]!= '(' and flag == 0):
            i = i+1
        flag = 1
        Cord.append(provided[i])
        i = i+1
    h = len(Cord)
    itr = 0
    cart = {}
    u = 0
    much = 0
    listt = []
    while itr<h:
        if(Cord[itr] not in ["(",")",","," "]):
            much = much+1
            while True:
                if(Cord[itr] == ")" or Cord[itr] == ","):
                    itr = itr+1
                    break
                elif(Cord[itr] not in ["(",")",","]):
                    listt.append(Cord[itr])
                    itr = itr+1
            s = [str(i) for i in listt]
            res = int("".join(s))
            cart[much] = res
            listt = []
        else:
            itr = itr + 1
   
            
    return cart

def ErrorCheck(Command):
    output = 0
    k = 0
    g = 0
    flag_Input = 0
    flag_count=0
    flag_brac_check = 0
    br = 0
    error = 0
    ind = 0
    check = 0
    checkbrac = 0
    onlyletters = ""
    
    if(len(Command)==0 ):
        print"Error:Not valid input given"
        output = 1
        return output
    if(Command[0] == ' '):
        print"Error:Not valid input given as there is extra space at start"
        output = 1
        return output
    if(Command[0]=='g' and len(Command)>1):
        print"Error: Nothing should be given as input along with 'g'"
        output = 1
        return output
    if(Command[0]!='g' and len(Command)<2):
        print"Error: Invalid Input as no streetname and coordinates are given"
        output = 1
        return output
    if(Command[0]!='g'):
        if(Command[0] not in ['a','c','r','g']):
            print "Error: Invalid input command at Start "
            output = 1
            return output
        if(Command[1] != ' '):
            print "Error: No space before Street Name "
            output = 1
            return output
            
        for i in range(len(Command)):
            if(Command[i]=='"'):
               if(Command[i]=='"' and flag_Input==1):
                   flag_count = 2
                   k = i
                   g = i+1
                   if(Command[0]!='r'):

                       ''' 
                       while(g<len(Command)):
                           if(Command[g] not in ['(',',',' ',')'] and Command[g] not in range(0,100)):
                               print "Error: InValid Input (You may have used Invalid Brackets) "
                               print "Command[g]", Command[g]
                               error = 1
                               output = 1
                               return output
                           else:
                                g = g +1
                        '''
                       
                       if(i==len(Command)-1 ):
                           print "Error: No coordinates given"
                           error = 1
                           output = 1
                           return output
                           break      
                       
                       if(Command[len(Command)-1] not in  [')',' ']):
                           print "Error: Valid Brackets Missing for Coordinates so Invalid Input"
                           error = 1
                           output = 1
                           return output
                           break
                          
                       
                       if(i==len(Command)-1 ):
                           print "Error: No coordinates given"
                           error = 1
                           output = 1
                           return output
                           break
                       if(Command[i+1]!=' '):
                           error = 1
                           print "Error: No Space after Street Name"
                           output = 1
                           return output
                           break
                       while(k<len(Command) ):
                             if(Command[k+1] ==' '):
                                 k = k+1
                             elif(Command[k+1]=='('):
                                 flag_brac_check = 1
                                 k = k+1
                                 break
                             else:
                                 print"Error: Invalid Bracket/Input "
                                 br = 1
                                 output = 1
                                 return output
                                 break
               flag_Input = 1
        if(flag_count)==0:
            print "Error: Invalid street name or no street name given "
            output = 1
            return output
        if(br == 1):
            print "Error:Invalid Brackets"
            output = 1
            return output

        if(flag_Input == 0):
            print "Error: Invalid 123 Input"
            output = 1
            return output
            
        flag_CheckLetters = 0

        for i in range(1,len(Command)):
            if(Command[i] not in ['"',' ']):
                print "Error: Invalid input before Street Name"
                output = 1
                return output  
            elif(Command[i] == '"'):
                break
                
        
        for i in range(len(Command)):    
            if(Command[i]=='"' and flag_CheckLetters==0):
                i = i+1
                while (Command[i]!='"'):
                    onlyletters += Command[i]
                    i = i+1
                flag_CheckLetters = 1
                break
        '''   
        print "Only letter string is " , onlyletters
        '''
        validin = 0
            
        if all(x.isalpha() or x.isspace() for x in onlyletters):
            #Valid Street Name
            validin = 1
            
        else:
            print("Error: Street name should only have alphabets ")
            error = 1
            output = 1
            return output
            
            
    for i in range(len(Command)):
        if(Command[i] in ['(',')']):
            if(Command[i] == ')' and flag_brac_check== 0):
                print "Error: Invalid Bracket Start"
                check = 1
                output = 1
                return output
                continue
            elif(Command[i]=='(' and checkbrac == 0):
                 checkbrac = 1
            elif(Command[i]==')' and checkbrac == 1):
                 checkbrac = 0
            else:
                print "Error: Bracket/Brackets Missing "
                output = 1
                check = 1
                return output
               
    if(check==1 or checkbrac==1):
        #print "Error: Invalid Brackets"
        output = 1
        return output
    if(error == 1):
        #print "Error: Invalid Input"
        output = 1
        return output
    
    return output
   

def keyupdate_For_V(V,V_Previous):
    keyy = 0
    new_V = {}
    flag_0 = 0
    kee = 0
    new_V_2 = {}
    keylist = V_Previous.keys()
    if(len(V_Previous)>0):
        key_max = max(keylist)
        L = key_max
    else:
        L = 0
    
    print"len(V_Previous) = ",L
    for key in V:
        kee = key
        for key in V_Previous:
            if(V_Previous[key]==V[kee]):
                new_V.update({key: V_Previous[key]})
    '''
    for a in sorted(new_V.keys()):
        print a
        new_V_2[a] = new_V[a]

    new_V = new_V_2
    print "New_V_2 = ",new_V_2
    '''
    for key in V:
        kys = key
        for key in new_V:
            if(V[kys]==new_V[key]):
                flag_0 = 1
        if(flag_0 == 0):
            L=L+1
            new_V.update({L:V[kys]})
            
        flag_0 = 0
   
    return new_V

def removeStreet(TotalStreets,Command,StreetNames):
    provided = Command
    flag2 = 0
    streetlist=''
    p = 0
    while (p< len(provided)):
        if(provided[p] != '"' and  flag2 == 0):
            p = p+1
        else:
            flag2 = 1
            y=p
            while(y<len(provided)):
                streetlist += provided[y]
                y = y+1
                if(provided[y] =='"'):
                    streetlist += provided[y]
                    break
        if (flag2== 1):
            break

    streetlist = streetlist.upper()
    if(streetlist not in StreetNames):
        print"Error: The street you want to remove doesn't exist on our database."
        return TotalStreets,StreetNames
    else:
        print "StreetList is ",streetlist
        StreetNames.remove(streetlist)
        del TotalStreets[streetlist]
        #TotalStreets.update({streetlist:Streets})
        return TotalStreets,StreetNames
def showEdge(EdgeList):
    if(len(EdgeList)<1):
        print "E = { }"
    else:
        print "E = { "
        for i in range(len(EdgeList)):
            print "<" ,EdgeList[i][0],",",EdgeList[i][1], ">"
        print"}"

def showDic(new_V):
    '''
    if(len(new_V)<1):
        print "V = { }"
    else:
        print "V = { "
        for key,value in new_V.iteritems():
            print key, ":",value
        print"}"
       '''
    if(len(new_V)<1):
        print "V = { }"
    else:
        print "V = { "
        for key in sorted(new_V):
            print key, ":",new_V[key]
        print"}"

 
  
# Function checks if the string 
# contains any special character 
def run(string): 
  
    # Make own character set and pass  
    # this as argument in compile method 
    regex = re.compile('[@_!#$%^&*<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
    if(regex.search(string) == None): 
        return 0
          
    else: 
        print("Error:Input not accepted as it contains invlaid characters or brackets.") 
        return 1
    

while True:
    V={}
    Intersection_Vertex = {}
    Streets = []
    TotalStreets = {}
    StreetList = []
    I_V={}
    Error_Result = 0
    V_Previous ={}
    Intersection_Vertex_Previous = {}
    new_Flag = 0
    gPress = 0
    Edges_List = []
    inputResult = 0
    while True:
   
        Command = raw_input("Enter Input ")
        inputResult = run(Command)
        if(inputResult == 1):
            continue
        Error_Result = ErrorCheck(Command)
        #print "Error Result is ", Error_Result
        if(Error_Result ==1):
            continue
        elif(Error_Result ==0):
            if(Command[0] == 'a'):
                cart1= exCord(Command)
                TotalStreets,StreetList = addStreet(cart1,TotalStreets,Command,StreetList)
                gPress = 0

            elif(Command[0] == 'c'):
                cart1= exCord(Command)
                TotalStreets,StreetList = changeStreet(cart1,TotalStreets,Command,StreetList)
                gPress = 0
                


            elif(Command[0] == 'r'):
                TotalStreets,StreetList = removeStreet(TotalStreets,Command,StreetList)
                gPress = 0
                
                 
                     
            elif(Command[0]=='g'):
                
                if(gPress == 0):
                    gPress = 1

                    V={}
                    Intersection_Vertex = {}
    
                    for i in range(len(StreetList)):
                        tr = i
                        while (tr<len(StreetList)-1):
                            for k in range(len(TotalStreets[StreetList[i]])):
                                for l in range(len(TotalStreets[StreetList[tr+1]])):
                                    V,Intersection_Vertex = intersection(TotalStreets[StreetList[i]][k],TotalStreets[StreetList[tr+1]][l],V,Intersection_Vertex)
                            tr = tr + 1

                    if(new_Flag == 0):
                        new_V = V
                        #print "V is ", V
                        #print "Intersection Vertix with wrong keys is ",Intersection_Vertex
                        I_V= keyupdate(V,Intersection_Vertex)
                        #print"I_V",I_V
                        showDic(new_V)
                        Edges_List = same_street(V,I_V,TotalStreets,StreetList)
                        showEdge(Edges_List)
                        
                    elif(new_Flag==1):
                        #print"NewFlag",new_Flag
                        new_V = keyupdate_For_V(V,V_Previous)
                        #print "V is ", V
                        #print "Intersection_Vertex is ",Intersection_Vertex
                        #print "new_V is ", new_V
                        
                        I_V= keyupdate(new_V,Intersection_Vertex)
                        #print "New_V ",new_V
                        showDic(new_V)
                        Edges_List = same_street(new_V,I_V,TotalStreets,StreetList)
                        showEdge(Edges_List)
                        
                    new_Flag = 1

                elif(gPress == 1):
                    #print "V =",new_V,
                    showDic(new_V)
                    showEdge(Edges_List)
                    gPress = 1
                    

                    
                    
                print"V_Previous is ", V_Previous
                V_Previous = new_V

            #print"Total Streets", TotalStreets
            #print "StreetList Length is ",len(StreetList)

        




        '''

        for l in range(len(TotalStreets[StreetList[i+1]])):
            intersection(TotalStreets[StreetList[i]][k],TotalStreets[StreetList[i+1]][l],V)
            
        for i in range(len(TotalStreets)):
            for k in range(len(Street_2)):
                intersection(Street_1[i],Street_2[k],V)
        for i in range(len(Street_1)):
            for k in range(len(Street_3)):
                intersection(Street_1[i],Street_3[k],V)
        for i in range(len(Street_2)):
            for k in range(len(Street_3)):
                intersection(Street_2[i],Street_3[k],V)
        updVertex(V)

        '''
        '''
        if __name__ == '__main__':
            main()
        '''
