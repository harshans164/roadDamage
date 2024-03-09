# Program to convert an xml
# file to json file

# import json module and xmltodict
# module provided by python
import json
import xmltodict


# open the input xml file and read
# data in form of python dictionary 
# using xmltodict module

#file opening error

fileNum=148
while fileNum<149:
    file_Name=r"c:\Users\Harshan\Downloads\road datasets\Czech\train\annotations\Czech_"
    final_file=file_Name+"000"+ str(fileNum)+".xml"

    with open(final_file) as xml_file:
	    data_dict = xmltodict.parse(xml_file.read())
	    json_data = json.dumps(data_dict)

    with open(r"c:\Users\Harshan\Downloads\road datasets\Czech\train\annotations json\Czech_000148.xml", "w") as json_file:
        json_file.write(json_data)
		
		
    f = open(r"c:\Users\Harshan\Downloads\road datasets\Czech\train\annotations json\Czech_000148.xml")
    data = json.load(f)
    fileNum+=1
    def label(s):
        if s=="D00":
            return 0
        elif s=="D10":
            return 1
        elif s=="D20":
            return 2
        elif s=="D40":
            return 3

    # Iterating through the json
    # list
    d=data['annotation']
    #print(d['object'])
    #keyerror exception
    try:
        if isinstance(d, list):
            print("list")

        elif isinstance(d, dict):
            print("dict")
            x=d['object']
            l=label(x['name'])
            coord=x['bndbox']
            
            stri=str(l)+" "+coord['xmin']+" "+coord['ymin']+" "+coord['xmax']+" "+coord['ymax']
            
        # Closing file
        f.close()
        
    except KeyError:
        continue
    
       
   
    