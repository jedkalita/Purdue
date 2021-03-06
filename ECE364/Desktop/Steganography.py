#! /usr/bin/env python3.4
#
# $Author$:
# $Date$:
# $HeadURL$:

import os
import math
import sys
import re
#sys.path.append('/home/ecegrid/a/ee364c10/Lab11/BitVector-3.3.2')
import BitVector
from BitVector import *
from PIL import Image
import base64
'''
bv = BitVector(intVal = 123)
print(bv)
im = Image.open("/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/sunflower.png")
px = im.load()
print(px[21,23])
'''
class Message: #Message class
    def __init__(self, **kwargs): #define the constructor
        #print(kwargs)
        #print(sorted(kwargs))
        self.type = [] #a list to store whether it is a filePath or a String
        self.values = [] #the values(MessageType, filepath string, xml string)
        self.xml = '' #if an xml string is passed, then yes, otherwise no
        self.msgText = '' #the original message if it is a text
        self.msgType = '' #the type of message is stored here, if applicable
        self.msgSize = '' #the size of the original message
        self.msgPath = '' #the path of the message is stored here, if applicable
        self.xmlForm = '' #the xml encoded form of the original message
        self.encodedString = '' #the string to store the encoded version of the original message
        self.grayList = []#list to store the values of the gray scale
        self.redList = []#list to store values for red channel of colored 
        self.greenList = []#list to store values for green channel of colored 
        self.blueList = []#list to store values for blue channel of colored 
        self.redEncoded = ''#to store red encoded string
        self.greenEncoded = ''#to store green encoded string
        self.blueEncoded = ''#to store blue encoded string
        for keys in sorted(kwargs): #filePath = 'path for file', messageType = 'Type' or xmlString = 'string that is encoded'
            self.type.append(keys) #get the keys first to state if you have a filepath or an xml string
            self.values.append(kwargs[keys]) #get either the path of the file and the message type, or the actual XML string
        #print(self.type)
        
        #NEW VALUEERROR FOR EMPTY FILEPATH
        if (len(self.values[0]) == 0):
            raise ValueError('The filepath cannot be empty.!!!')

        if (len(self.type) == 1): #basically if just one argument, then it is an XML string
            if (self.type[0] != 'XmlString'): #the type is not XML string or the corresponding value is not a , that means it has to raise an excption
                #print(self.type[0])
                #print(type(self.values[0]))
                raise ValueError('Wrong argument!!')
            else:
                pass
        elif (len(self.type) == 2): #basically if two keys, then check if they are filePath and messageType
            if (self.type[0] != 'filePath') or (self.type[1] != 'messageType') or (self.values[1] != 'Text' and self.values[1] != 'GrayImage' and self.values[1] != 'ColorImage'): #if not filePath or the type of message is not one of the ones required
                '''
                print(self.type[0])
                print(self.type[1])
                print(self.values[0])
                print(self.values[1])
                if (self.type[0] != 'filePath'):
                    print('FilePath err')
                if (self.type[1] != 'messageType'):
                    print('MessageType err')
                if (self.values[1] != 'Text' and self.values[1] != 'GrayImage' and self.values[1] != 'ColorImage'):
                    print('Type of message err')
                '''
                raise ValueError('Wrong argument!!')
            else:
                pass
        else: #there can only be two or one keys, that means it is an error
            raise ValueError('There can be at most two arguments.')
        #now, there will be no more errors, so we can populate the member data of the class - the message type, message path, xml string if applicable
        if (len(self.type) == 1):#xml string is the only argument
            self.xmlForm = self.values[0] #the encoded XML string
            self.xml = 'y' #the message type is XML
            #now, get the size and type of the XML string
            t = self.xmlForm#temporary string
            tot = t.split('=') #split according to =
            tpe = tot[3]#always constant
            sze = tot[4]#always constant
            tpe = tpe.split(' ')[0]
            sze = sze.split(' ')[0]
            tpe = tpe.replace('\"', '')
            sze = sze.replace('\"', '')
            self.msgSize = sze #set size of message
            self.msgType = tpe #set type of message
            #print(self.msgType)
            #print(self.msgSize)
        else: #if not 1, then 2
            self.xml = 'n' #the message type is not XML
            self.msgPath = self.values[0] #(filePath = '.../.../')
            self.msgType = self.values[1] #messageType = 'Text/ColorImage/GrayImage'
            if (self.msgType == 'GrayImage') or (self.msgType == 'ColorImage'):#set the message size for an image message type
                im = Image.open(self.msgPath)
                width,height = im.size
                self.msgSize = str(width) + ',' + str(height)
            else: #for the case that it is a text, we don't have to set it yet
                pass #it will be set based on the length of the ncoded string
    '''
    def showVals(self):
        print('XML Form: ' + self.xmlForm)
        print('Message Type: ' + self.msgType)
        print('Message Path: ' + self.msgPath)
        print('Encoded String: ' + self.encodedString)
    '''    
    def getMessageSize(self):#function to get the number of bytes in XML form
        #tmp = open('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/color_mona_enc.xml')
        if len(self.xmlForm) == 0:#the size of the xml string is 0,then exception
        #if len(self.xmlForm) == 0:#the size of the xml string is 0,then exception
            raise Exception
        return(len(self.xmlForm)) #the length of the xml form string
        '''
        for lines in tmp:
            #print(lines)
            m = re.search(r"(size=)(?P<sizeTot>.*)( encrypted)", str(lines)) #the regex to extract the size
            if m:
                #print('yes')
                totSize = int(m.group("sizeTot").replace('\"','').replace(',',''))#to replace a few things from the string
                #print(totSize)
                return totSize
        '''
   
    def getOriginalText(self): #get the original text from the text or image 
        if (self.xml == 'y'): #if its an XML, then don't do anything
            pass
        else: #if its an image or text
            if (self.msgType == 'Text'): #if it is a text
                f = open(self.msgPath, 'r') #open the text file for reading
                string = '' #temporary string
                for lines in f:
                    #pass
                    #lines.replace('\n', '')
                    string = string + lines      
                self.msgText = string #simply get the text lines
                #print(self.msgText)
                f.close() #close the file handler
            else: #for image files
                if (self.msgType == 'GrayImage'):#populate the grayList list
                    im = Image.open(self.msgPath) #open the image 
                    self.grayList = list(im.getdata())
                else:#for a colored image Red,Green, Blue channels independently
                    im = Image.open(self.msgPath)#open the image
                    lst = list(im.getdata()) #to get the tuple
                    for i in range(0, len(lst)):#iterate throught entire list
                        self.redList.append(lst[i][0])#1st element of tuple=Red
                        self.greenList.append(lst[i][1])#2nd element of tuple=Green
                        self.blueList.append(lst[i][2])#3rd element of tuple=Blue
                    
    def encodeOriginalText(self): #function to encode the original message
        if (self.xml == 'y'):#already in encoded form if XMLString
            #extract the encoded message part
            #tmp = self.xml #a temporary string to hold the xml
            #tmp = open('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/color_mona_enc.xml')
            f_tmp = open('tmp_file.xml','w')
            f_tmp.write(self.xmlForm)
            f_tmp.close()
            f_tmp = open('tmp_file.xml','r')
            #tmp = self.xmlForm #the xml string that is given to us
            for lines in f_tmp:
                if lines[0] != '<': #since every lines begins with a '<' except for the one we need
                    self.encodedString = lines #get the encoded string
                else:
                    pass
        else: #else if it is an image or a text
            #first of all, get the original message
            self.getOriginalText()
            if (self.msgType == 'Text'): #if it is a text message
                self.encodedString = str(base64.b64encode(bytearray(self.msgText.encode('UTF-8')))) #encode the string
                self.encodedString = self.encodedString[2:len(self.encodedString) - 1] #remove the non-required portions
                self.msgSize = str(len(self.msgText))
            elif (self.msgType == 'GrayImage'): #for gray image
                self.encodedString = str(base64.b64encode(bytes(self.grayList)), "UTF-8") #encode the string
                # self.encodedString = self.encodedString[2:len(self.encodedString) - 1] #remove the non-required portions
            else: #for color image
                colorList = bytes(self.redList + self.greenList + self.blueList)
                self.encodedString = str(base64.b64encode(colorList), "UTF-8")

                # self.redEncoded = str(base64.b64encode(bytes(self.redList))) #encode the red string
                # self.redEncoded = self.redEncoded[2:len(self.redEncoded) - 1] #remove the non-required portions
                # self.greenEncoded = str(base64.b64encode(bytes(self.greenList))) #encode the green string
                # self.greenEncoded = self.greenEncoded[2:len(self.greenEncoded) - 1] #remove the non-required portions
                # self.blueEncoded = str(base64.b64encode(bytes(self.blueList))) #encode the blue string
                # self.blueEncoded = self.blueEncoded[2:len(self.blueEncoded) - 1] #remove the non-required portions
                # self.encodedString = self.redEncoded + self.greenEncoded + self.blueEncoded #add the three channel encoded strings to form the overall string
            
    def getXmlString(self):#the function to populate the message attributes
        if(self.xml == 'y'):#if already an XML string
            return
        self.encodeOriginalText() #encode the message by calling function
        if len(self.encodedString) == 0:#raise an exception
            raise Exception
        #now make the xml string representation
        self.xmlForm = self.xmlForm + '<?xml version=\"1.0\" encoding=\"UTF-8\"?>' + '\n'
        self.xmlForm = self.xmlForm + '<message type=\"' + self.msgType + '\" size=\"' + self.msgSize + '\" encrypted=\"False\">' + '\n'
        self.xmlForm = self.xmlForm  + self.encodedString
        self.xmlForm = self.xmlForm + '\n</message>'

        return self.xmlForm


    def saveToTarget(self, targetPath): #the function to save either to an image or to a text file
        if (self.msgType == 'Text'):#if the message if of type Text
            self.saveToTextFile(targetPath)
        elif (self.msgType == 'GrayImage') or (self.msgType == 'ColorImage'):#if color or gray image
            self.saveToImage(targetPath)
        else:#for XML string type of message
            pass

    def saveToTextFile(self, targetTextFilePath):#the function to save to a text file
        #first get the XML string that in turn fills up all the corresponding fields
        if(self.xml == 'y'):#if already an XML, get the encoded version
            #print('Coming here!!!')
            self.encodeOriginalText()
        else:
            self.getXmlString()
        if (self.msgType != 'Text'):#if not text then raise TypeError
            raise TypeError('Not a text file!!!')
        if (len(self.encodedString) == 0):#encoded string has nothing
            raise Exception        
        #now, we have the encoded string which we have to decode
        #decoded = str(base64.b64decode(self.encodedString).decode('string-escape'))
        #print(self.encodedString)
        decoded = str(base64.b64decode(self.encodedString))
        decoded = decoded[2:len(decoded) - 1] #remove the non-required things
        #print(decoded) 
        tot_slash_n = 0
        for i in range(0, len(decoded)-2):
            if (decoded[i+1] =='\\' and decoded[i+2]=='n'):
                tot_slash_n = tot_slash_n + 1
        fin = ''       
        if tot_slash_n != 0:
            ind = []
            ind.append(0)
            for i in range(0, len(decoded)-2):
                if (decoded[i+1] =='\\' and decoded[i+2]=='n'):
                    ind.append(i+1)
            for i in range(0,len(ind)-1):
                if(ind[i]==0):
                    fin = fin + decoded[ind[i]:ind[i+1]]
                else:
                    fin = fin + decoded[ind[i]+2:ind[i+1]]
                fin = fin + '\n'
        else:
            fin = decoded
        #print(fin)
        #print(decoded[len(decoded)-2])
        f = open(targetTextFilePath, 'w') #use a file handler to write to target
        f.write(fin) #write the decoded text to the file

    def saveToImage(self, targetImagePath):
        if(self.xml == 'y'):#if already an XML, get the encoded version
            self.encodeOriginalText() 
            if (self.msgType != 'GrayImage') and (self.msgType != 'ColorImage') :#if not image then raise TypeError
                raise TypeError('Not an image file!!!')
            if (len(self.encodedString) == 0):#encoded string has nothing
                raise Exception
            
            if (self.msgType == 'ColorImage'): #only if its a color image
                decoded = list(bytes(base64.b64decode(self.encodedString)))
                # print(len(decoded))
                # print(self.msgSize)
                red_data = []
                green_data = []
                blue_data = []
                #print(len(decoded))
                red_end = int(len(decoded)/3)
                green_end = int(red_end*2)
                #print(red_end)
                #print(green_end)
                blue_end = red_end*3
                #print(blue_end)
                for i in range(0, red_end):
                    red_data.append(decoded[i])
                for i in range(red_end, green_end):
                    green_data.append(decoded[i])
                for i in range(green_end, blue_end):
                    blue_data.append(decoded[i])
                total_data = [] #the total data

                for i in range(0, len(red_data)): #since lengths are the same
                    total_data.append((red_data[i], green_data[i], blue_data[i])) #make the tuple
                #print(total_data)
                '''
                #print(len(total_data))
                #print(len(red_data))
                #print(len(green_data))
                #print(len(blue_data))
                '''
                # tup = tuple
                w = self.msgSize.split(',')[0]
                h = self.msgSize.split(',')[1]
                tup = (int(w), int(h)) #get the dimensions 
                #print(tup)
                im_new = Image.new('RGB', tup)
                im_new.putdata(total_data)
                im_new.save(targetImagePath) #save to the correct output file name
            

            else: #else if gray image 
                decoded = base64.b64decode(self.encodedString) #decode
                tup = tuple
                w = self.msgSize.split(',')[0]
                h = self.msgSize.split(',')[1]
                tup = (int(w), int(h)) #get the dimensions        
                im_new = Image.frombytes('L', tup, decoded)           
                im_new.save(targetImagePath) #save to the correct output file name
            
        else: #not an xml string, ie just a gray image ir color image
            self.getXmlString()
            if (self.msgType != 'GrayImage') and (self.msgType != 'ColorImage') :#if not image then raise TypeError
                raise TypeError('Not an image file!!!')
            if (len(self.encodedString) == 0):#encoded string has nothing
                raise Exception
            if (self.msgType == 'GrayImage'): #if its a gray image
                decoded = base64.b64decode(self.encodedString) #decode
                #print(decoded)
                tup = tuple
                w = self.msgSize.split(',')[0]
                h = self.msgSize.split(',')[1]
                tup = (int(w), int(h)) #get the dimensions        
                im_new = Image.frombytes('L', tup, decoded)           
                im_new.save(targetImagePath) #save to the correct output file name
            else:#if its a color image
                red_data = list(bytes(base64.b64decode(self.redEncoded))) 
                green_data = list(bytes(base64.b64decode(self.greenEncoded)))
                blue_data = list(bytes(base64.b64decode(self.blueEncoded)))
                total_data = [] #the total data
                for i in range(0, len(red_data)): #since lengths are the same
                    total_data.append((red_data[i], green_data[i], blue_data[i])) #make the tuple
                #print(total_data)
                tup = tuple
                w = self.msgSize.split(',')[0]
                h = self.msgSize.split(',')[1]
                tup = (int(w), int(h)) #get the dimensions 
                #print(tup)
                im_new = Image.new('RGB', tup)
                im_new.putdata(total_data)
                im_new.save(targetImagePath) #save to the correct output file name
       
class Steganography: #Steganography class
    def __init__(self, imagePath, direction='horizontal'): #the constructor

        if (direction != 'horizontal' and direction != 'vertical'): #raise ValueError since direction does not hold the correct value(s)
            raise ValueError('direction should be horizontal or vertical!!!')

        self.im = Image.open(imagePath) #the medium image, open the imagepath provided

        if (self.im.mode != 'L'):#i.e, it is not a gray scale image
            raise TypeError('Image medium must be gray scale!!!!!')#raise the TypeError message
        self.dir = direction
        self.width = self.im.size[0] #get the width of medium image
        self.height = self.im.size[1] #get the height of medium image
        self.maxSize = int((self.width * self.height) / 8) #corresponding to this particular image medium in gray scale, since each bit of the message corresponds to one byte of the image medium thats why divide by 8. This is the max. no of bytes that could be in the message to be embedded
        
    def embedMessageInMedium(self, message, targetImagePath): #the function to embed the message inside of the medium image, then save the overall image to the targetImagePath image file

        message.getXmlString()
        if (message.getMessageSize() > self.maxSize):#basically the embedding medium cannot embed everything in the original message
            raise ValueError('The Embedding Medium is of lesser size than required to embed message!!!') #the TypeError message

        mess = message.xmlForm #get the XML string of the message
        #now the first task is to check if the direction is horizontal or vertical

        if (self.dir == 'horizontal'):#if horizontal direction
            tup = tuple #make the tuple to store the width and height of medium
            tup = (int(self.width), int(self.height)) 
            all_pixels = list(self.im.getdata()) #get all the pixels in int form

            #since it is horizontal rasterisation, we can just scan through all_pixels while we try to compare the LSB for embedding the message
            text = '' #the bit value storing string for the message XML

            for i in range(0, len(mess)): #get the bit level representation (each 8 bit long per character) by iterating throught the entire message XML
                bit = bin(ord(mess[i]))[2:].rjust(8, '0') #get the 8-bit long representation of each character
                text = text + bit #append to the text to get 8-bit long representation for all the characters of the message XML

            fin_pix = [] #the final pixel list that will store the changed bits (LSB) for each pixel

            for i in range(0, len(text)): #iterate through the entire bits
                bv = BitVector(intVal = all_pixels[i], size = 8) #byte representation of each pixel

                #if LSB not equal to corresponding bit, then change
                if (bv[7] == 1 and text[i] != '1'): 
                    bv[7] = 0
                elif (bv[7] == 0 and text[i] != '0'):
                    bv[7] = 1
                else:
                    pass

                newnum = int(bv) #the changed/unchanged number

                fin_pix.append(newnum) #append the new number to final pixel array
            #now just copy the remaining pixel values from the original pixels to the final pixel list
            for i in range(len(fin_pix), len(all_pixels)):
                fin_pix.append(all_pixels[i])
            #store the new pixels with the embedded data in a new image
            '''
            c=0
            for i in range(0,len(fin_pix)):
                if(fin_pix[i]!=all_pixels[i]):
                    c=c+1
            print('Number different: ', c)
            '''
            im = Image.new('L', tup)
            im.putdata(fin_pix)
            im.save(targetImagePath)
            #finished for horizontal rasterisation
        else: #for vertical rasterisation
            tup = tuple #make the tuple to store the width and height of medium
            tup = (int(self.width), int(self.height)) 
            #a=list(self.im.getdata())
            all_pixels = self.im.load() #to get all the pixels in 2D format
            mat = [[0] * self.width for i in range(self.height)] #a 2-D list with width x height dimensions, initialized to 0
            text = '' #the bit value storing string for the message XML
            for i in range(0, len(mess)): #get the bit level representation (each 8 bit long per character) by iterating throught the entire message XML
                bit = bin(ord(mess[i]))[2:].rjust(8, '0') #get the 8-bit long representation of each character
                text = text + bit #append to the text to get 8-bit long representation for all the characters of the message XML
            #now, put the vertically scanned pixels into the 2D list of lists mat
            for i in range(0, self.width):
                for j in range(0, self.height):
                    mat[j][i] = all_pixels[i,j]
            #now, it's time to emdeb into the mat[][] list the LSB values by comparing with the embed message
            count = 0#to store the current element relative to text bit string
            for i in range(0, self.width):
                for j in range(0, self.height):
                    if count == len(text): #if count becomes equal, then come out
                        break
                    else: #perform the comparison and change the pixels accordingly
                        bv = BitVector(intVal = mat[j][i], size = 8)#byte representation of each pixel
                        #if LSB not equal to corresponding bit, then change
                        if (bv[7] == 1 and text[count] != '1'): 
                            bv[7] = 0
                        elif (bv[7] == 0 and text[count] != '0'):
                            bv[7] = 1
                        else:
                            pass
                        newnum = int(bv) #the changed/unchanged number
                        mat[j][i] = newnum #assign the new pixel value in mat
                        count = count + 1 #increment the value of count
            #now, make the final pixel list out of the mat[][] list of lists
            fin_pix = []
            for i in range(0, self.height):
                for j in range(0, self.width):
                    #print('i: ' + str(i))
                    #print('j: ' + str(j))
                    fin_pix.append(mat[i][j])
            #store the new pixels with the embedded data in a new image
            '''
            c=0
            for i in range(0,len(fin_pix)):
                if(fin_pix[i]!=a[i]):
                    c=c+1
            print('Number different: ', c)
            '''
            im = Image.new('L', tup)
            im.putdata(fin_pix)
            im.save(targetImagePath)
    
    def extractMessageFromMedium(self): #the function to extract message from medium
        xmlString = '' #the final XML string from hopefully the extracted message(XML if valid, else random
        if (self.dir == 'horizontal'):#if horizontal rasterisation
            pix = list(self.im.getdata())#get the list of pixel data from object image
            strc = '00111100001011110110110101100101011100110111001101100001011001110110010100111110' #the bit level 80-bit representation for '</message>'
            #now we iterate through pixel list using their LSB values until we find </message>, and at that point we break, and use th value of the stopping byte
            found = 0#to check if we find the XML string or not
            for i in range(0, len(pix) - 80):
                string = ''
                for j in range(i, i + 80):#since 10 characters long is </message>
                    s = bin(pix[j])[2:].rjust(8, '0')[7] #get the LSB of 8bit level representation of each pixel value
                    string = string + s
                if (string == strc):#we've found it
                    found = 1#to indicte that have indeed found an XML string
                    break
            if (found == 1):#only if it is an XML string
                r = j % 8 #find out the remainder that j is not a multiple of 8 by, since otherwise characters only work for 8-bit multiples
                l = j - r 
                m = l + 8 #to get the next byte from j if any remainder
                tot = '' #the total string to get th XML form out of
                for i in range(0, m):
                    b = bin(pix[i])[2:].rjust(8, '0')[7]
                    tot = tot + b
                xmlString = BitVector(bitstring = tot).get_text_from_bitvector()#the final xml string, if it is an XML string
            else: #if not xml string, then make the returned xml string to be empty
                pass

        else: #i.e, the rasterisation direction is vertical
            #now make a list that gets all the pixels in Top-Bottom, L-R direction
            pixels = self.im.load() #get 2D array of pixels values
            pix = [] #th elist to eventually store the pixel values
            for i in range(self.width): #for all width
                for j in range(self.height): #for all height
                    p = pixels[i,j]
                    #print(p)
                    pix.append(p) #append the pixel values
            #now, its essentially the same process as horizontal
            strc = '00111100001011110110110101100101011100110111001101100001011001110110010100111110' #the bit level 80-bit representation for '</message>'
            #now we iterate through pixel list using their LSB values until we find </message>, and at that point we break, and use th value of the stopping byte
            found = 0#to check if we find the XML string or not
            for i in range(0, len(pix) - 80):
                string = ''
                for j in range(i, i + 80):#since 10 characters long is </message>
                    s = bin(pix[j])[2:].rjust(8, '0')[7] #get the LSB of 8bit level representation of each pixel value
                    string = string + s
                if (string == strc ):#we've found it
                    found = 1#to indicte that have indeed found an XML string
                    break
            if (found == 1):#only if it is an XML string
                r = j % 8 #find out the remainder that j is not a multiple of 8 by, since otherwise characters only work for 8-bit multiples
                l = j - r 
                m = l + 8 #to get the next byte from j if any remainder
                tot = '' #the total string to get th XML form out of
                for i in range(0, m):
                    b = bin(pix[i])[2:].rjust(8, '0')[7]
                    tot = tot + b
                xmlString = BitVector(bitstring = tot).get_text_from_bitvector()#the final xml string, if it is an XML string
            else: #if not xml string, then make the returned xml string to be empty
                pass
        if (xmlString == ''):#i.e, probable xml string is empty, then return None
            return None
        #now that we have the string that could probably be the XML string
        else: #otherwise, return an onject of Message type
            extractedMessage = Message(XmlString = xmlString)
            return extractedMessage
        
if __name__ == "__main__":
    '''
    #testing code

    fp = '/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/mona.png'
    #fp = '/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/full.txt'
    #mt = 'ColorImage'
    mt = 'GrayImage'
    #mt = 'Text'

    fp = open('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/full.xml','r')
    string = ''
    for lines in fp:
        #print(lines)
        string = string + lines
    #print(lines)
    msgobj = Message(XmlString = string)

    msgobj = Message(filePath = fp, messageType = mt)
    msgobj.getXmlString()
    #msgobj.saveToTarget('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/test_image.png')
    #msgobj.saveToTarget('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/test_gray.png')
    #msgobj.saveToTarget('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/test_text.txt')
    #print(msgobj.xmlForm)
    #f = open('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/test_xml.xml','w')
    #print(msgobj.encodedString)
    #f.write(msgobj.xmlForm)
    #print(msgobj.xmlForm)
    #msgobj = Message(XmlString = 'jjdjdjdjdd')
    #msgobj.encodeOriginalText()
    #msgobj.getXmlString()
    #msgobj.showVals()
    #print(msgobj.getMessageSize())
    #im = Image.open("/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/color_mona.png")
    #px = im.load()
    #print(im.size)
    #print(px[127,127])
    '''

    #fp = '/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/mona.png'
    fp = '/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/sunflower.png'
    #fp = '/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/full.txt'
    mt = 'ColorImage'
    #mt = 'GrayImage'
    #mt = 'Text'
    msgobj = Message(filePath = fp, messageType = mt)
    msgobj.getXmlString()
    f1 = open('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/TEST_MES.xml', 'w')
    f1.write(msgobj.xmlForm)
    f1.close()
    check_image = msgobj.xmlForm
    chckimg = Message(XmlString = check_image)
    chckimg.saveToTarget('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/XTRACT_CHECK_COLOR.png')

    '''
    imagePath = '/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/nature.png'
    #imagePath = '/home/ecegrid/a/ee364c10/Lab11/BitVector-3.3.2/stegimg.png'
    #direction = 'horizontal'
    direction = 'vertical'
    stegobj = Steganography(imagePath, direction)
    #targetImagePath = '/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/steg_horizontal.png'
    targetImagePath = '/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/steg_vertical.png'
    stegobj.embedMessageInMedium(msgobj, targetImagePath)
    #imagePath2 = '/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/steg_horizontal.png'
    imagePath2 = targetImagePath
    stegobj2 = Steganography(imagePath2, direction)
    msg = stegobj2.extractMessageFromMedium()
    f2 = open('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/TEST_STEG.xml', 'w')
    if(msg is None):
        print('No message!')
        f2.close()
    else:
        if (msg.msgType == 'GrayImage' or msg.msgType == 'ColorImage'):
            msg.saveToTarget('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/xtract_message_test.png')
            f2.write(msg.xmlForm)
            f2.close()
            #print(msg.xmlForm)
        else:
            msg.saveToTarget('/home/ecegrid/a/ee364c10/Lab11/Phase_I_Tests(1)/files/xtract_message_test.txt')
            f2.write(msg.xmlForm)
            f2.close()
            #print(msg.xmlForm)
    '''









