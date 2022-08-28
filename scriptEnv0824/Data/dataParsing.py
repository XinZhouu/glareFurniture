

#Header
def headerControl(newTxt):
    #delete the first garbage data
    line0 = newTxt[0][2::]
    return [line0]

#Glare Source
def glareSourceOutput(newTxt):
    #glare source info
    glareSourceTxt = copy.copy(newTxt)
    #remove header
    glareSourceTxt.pop(0)
    lenTxt = len(glareSourceTxt)
    glareSourceTxt.pop(lenTxt-1)
    glareSourceTxt.pop(lenTxt-2)
    # add the updated header
    lst = headerControl(newTxt)
    lst += glareSourceTxt
    
    newLst = []
    for line in lst:
        line = line.split(' ')
        newLst.append(line)
    return newLst

def extractGlareSources(twoDList):
    dic = dict()
    # the num should remove the header
    numDataSources = len(twoDList)-1 
    # find (x,y,z) in the header
    header = twoDList[0]
    indexX = header.index('xdir')
    indexY = header.index('ydir')
    indexZ = header.index('zdir')
    lum = header.index('Max_Lum')
    # extract specific data
    # ignore the header
    for row in range(1, len(twoDList)):
        glareName = twoDList[row][0]
        x = twoDList[row][indexX]
        y = twoDList[row][indexY]
        z = twoDList[row][indexZ]
        lumVal = twoDList[row][lum]
        lst = [(x,y,z), lumVal]

        if glareName not in dic:
            dic[glareName] = lst
    return dic

# Final Glare Value(DGP, DGI...)
# return a 2D list
def glareValueOutput(newTxt):
    lst = []
    #glare final output info
    glareOutput = copy.copy(newTxt)
    lenGlare = len(glareOutput)
    glareOutputString = glareOutput[lenGlare-2:][0]
    glareOutputLst = glareOutputString.split(":")
    glareOutputValue = glareOutputLst[1][1:]
    lst.append(glareOutputLst[0].split(','))
    lst.append(glareOutputValue.split(" "))
    return lst

def selectUseFulGlareMetrics(twoDList):
    dic = dict()
    header = twoDList[0]
    index = header.index('dgp')
    value = twoDList[1][index]
    dic['dgp'] = value
    return dic

def dicToTwoDList(dic1, dic2):
    # combine them into a single dic
    for key in dic2:
        if key not in dic1:
            dic1[key] = dic2[key]
    return dic1
    
def extractGlarePositions(dic):
    lst = []
    for key in dic:
        if key.isdigit():
            pt = dic[key][0]
            lst.append(pt)
    return lst
    
def constructPtsFromStr(ptLst):
    lst = []
    for tp in ptLst:
        pt = gh.ConstructPoint(tp[0], tp[1], tp[2])
        lst.append((pt))
    return lst
            
            
def glareDirection(glareSource):
    lst = []
    for pt in glareSource:
        vector = rs.VectorCreate(pt, (0,0,0))
        lst.append(vector)
    return lst
        

# for debugging purposes
#def visualize2DMatrix(twoDlst):
#    dic = dict()
#    for row in lst:

