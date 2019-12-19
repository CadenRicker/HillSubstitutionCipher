key2=[[3,10,20],\
        [20,9,17],\
        [9,4,17]]
key3=[[11,22,14],\
        [7,9,21],\
        [17,0,3]]
key5=[[4,9,15],\
        [15,17,6],\
        [24,0,17]]
key5I=[[17,17,5],\
       [21,18,21],\
       [2,2,19]]
key6=[[11,20,20],\
      [2,1,24],\
      [9,3,3]]
key6I=[[9,0,18],\
      [2,9,10],\
      [23,17,23]]
keys = [key2,key3,key5,key5I,key6,key6I]
diction ={'a': 0,'b': 1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,
    'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
rediction ={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',
    13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

while(True):
        text= input("Enter Text: ")
        cols =int(len(text)/3)
        array =[]
        for l in text:
                array.append(diction[l])
        print(array)
        cols =len(array)
        print("0: key2\n1: key3\n2: key5\n3: key5Inverse\n4: key6\n5: key6Inveres")
        keyNum = int(input("Enter Number for key: "))
        key = keys[keyNum]
        row1=""
        row2=""
        row3=""
        Result1=""
        Result2=""
        Result3=""
        outputArray=[]
        for i in range(0,cols,3):
                print(i)
                v1=array[i]
                v2=array[i+1]	
                v3=array[i+2]
                row1=row1+str(key[0][0]*v1%26)+"+"+str(key[0][1]*v2%26)+"+"+str(key[0][2]*v3%26)+" # "
                row2=row2+str(key[1][0]*v1%26)+"+"+str(key[1][1]*v2%26)+"+"+str(key[1][2]*v3%26)+" # "
                row3=row3+str(key[2][0]*v1%26)+"+"+str(key[2][1]*v2%26)+"+"+str(key[2][2]*v3%26)+" # "
                Result1=Result1+str((key[0][0]*v1+key[0][1]*v2+key[0][2]*v3)%26)+"\t # "
                Result2=Result2+str((key[1][0]*v1+key[1][1]*v2+key[1][2]*v3)%26)+"\t# "
                Result3=Result3+str((key[2][0]*v1+key[2][1]*v2+key[2][2]*v3)%26)+"\t# "
                outputArray.append((key[0][0]*v1+key[0][1]*v2+key[0][2]*v3)%26)
                outputArray.append((key[1][0]*v1+key[1][1]*v2+key[1][2]*v3)%26)
                outputArray.append((key[2][0]*v1+key[2][1]*v2+key[2][2]*v3)%26)
        print("Row1: "+row1)
        print("Row2: "+row2)
        print("Row3: "+row3)
        print("Result1: "+Result1)
        print("Result2: "+Result2)
        print("Result3: "+Result3)
        output=""
        for i in outputArray:
                output=output+rediction[i]
        print(output)
