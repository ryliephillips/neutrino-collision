import math

results = {}

def distances(xpoint, ypoint, zpoint):
    xlist = [-12]*32 #all x coordinates
        
    ylist = [55.249,55.249,27.431,-0.303,-28.576,-56.615,-56.203,54.646,54.693,-0.829,-0.706,-56.261,-57.022,55.771,55.822,-0.875,-0.549,-56.323,-56.205,55.800,55.625,-0.051,-0.502,-56.408,-56.284,55.822,55.313,27.607,-0.722,-28.625,-56.309,-56.514] #all y coordinates

    zlist = [108.693,149.287,72.034,194.676,71.407,108.802,149.112,308.909,349.145,262.947,394.771,308.572,349.273,521.066,561.862,474.028,606.217,521.153,561.549,732.006,772.816,685.136,817.141,732.207,772.838,931.998,972.794,1010.644,886.531,1011.288,932.872,972.797] #all z coordinates
            
            
    for x in range(0,32):
                name = 'PMT' + str(x + 1)
                xdistance = xpoint - xlist[x]
                ydistance = ypoint - ylist[x]
                zdistance = zpoint - zlist[x]
                distance = math.sqrt(xdistance**2 + ydistance**2 + zdistance**2)
                results[name] = distance
                    
    return results

f=open('distFile.csv','w')

for xPos in range(0,258):
    for yPos in range(-117,117):
        for zPos in range(0,1038):

            myStuff=distances(xPos, yPos, zPos)
            myStr="%i,%i,%i"%(xPos,yPos,zPos)
            for i in range(1,33):
                out=myStuff["PMT%i"%i]
                myStr=myStr+",%f"%(out)
            myStr=myStr + '\n'
            f.write(myStr)
f.close()



