#-----------------------------------------------------------------------
# Name: Nagelli Srikanth Goud 
# Platform: phython
#----------------------------------------------------------------------
# * A Code to Implement Column associative cache * 
#----------------------------------------------------------------------
k=open("trace.txt","r")
input=k.readlines()
print(len(input))
minput=[]
for i in range(len(input)):
    minput.append(bin(int(input[i][2:],16))[2:]) #hex to binary by removing labels 
    minput[i]=minput[i].zfill(32) # appending zero to make it 32 bit size 
print len(minput)  
cache={}  # cache block dictionary  
rehashbit={}# rehash bit 
for i in range(512):
    c=(bin(i))[2:].zfill(9) # converting index values in binary ; P -key 
    rehashbit[c]=1 # reash bit is initialized to 1 for all cache blocks
    cache[c]=0   
hit=0
miss=0
for i in range(len(minput)):
    I=minput[i][19:28] #  getting index bits 
    T=minput[i][0:19] # Tgetting Tag  bits  
    MT=T+I[0]  #Msb bit of Index is appended to tag 
    #-------- * Accessing the Upper Half of the coluumn associate cache (0-255) *------
    if cache[I]==MT:
        hit=hit+1
        rehashbit[I]=0
    else:
        if rehashbit[I]==1:
            miss=miss+1
            cache[I]=MT
            rehashbit[I]=0
        else:
            if I[0]==0:
                I2="1"+I[1:] # Fliping the MSB bits if its zero 
            else: 
                #-------- * Accessing the lower Half of the coluumn associate cache (256- 511) *------
                I2="0"+I[1:] # Fliping the MSB bit if its one 
            if cache[I2]==MT: 
                hit=hit+1
                a=cache[I2]
                cache[I2]=cache[I]  
                cache[I]=a
                rehashbit[I]=1
            else:
                miss=miss+1
                cache[I2]=MT
                b=cache[I2]
                cache[I2]=cache[I]
                cache[I]=b
                rehashbit[I]=1
print miss
print hit
print "Miss rate For column associative cache:"
print (miss/float(miss+hit))


        

