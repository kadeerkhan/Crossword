def display(p):
    for i in p:
        print (i)

def v_length(p,x,y,w):
    a=0
    for k in range(x,len(p)):
        if(p[k][y]=='*'):
            a=a+1
        else:
            if(w!=None):
                if(a<len(w)):
                    if(p[k][y]==w[a]):
                        a=a+1
                    else:
                        return -1
                else:
                    break
            else:
                break
    return a

def h_length(p,x,y,w):
    a=0
    for k in range(y,len(p[x])):
        if(p[x][k]=='*'):
            a=a+1
        else:
            if(w!=None):
                if(a<len(w)):
                    if(p[x][k]==w[a]):
                        a=a+1
                    else:
                        return -1
                else:
                    break
            else:
                #print(p[x],x,y)
                #return -1
                break

    return a

def h_fit(w,p,x,y):
    for i in range(0,len(w)):
        s=p[x]
        s=s[:y+i]+w[i]+s[y+i+1:]
        p[x]=s

def v_fit(w,p,x,y):
    for i in range(0,len(w)):
        s=p[x+i]
        s=s[:y]+w[i]+s[y+1:]
        p[x+i]=s

hd=[]
vd=[]
def fil_d(p):
    for i in range(0,len(p)):
        v1=[]
        h1=[]
        for j in range(0,len(p[i])):
            v=v_length(p,i,j,None)
            h=h_length(p,i,j,None)
            v1.append(v)
            h1.append(h)
        hd.append(h1)
        vd.append(v1)

def asdf(p,w):
    for i in range(0,len(p)):
        for j in range(0,len(p[i])):
            v=vd[i][j]
            h=hd[i][j]
            if(v>1):
                for word in w:
                    if(v==len(word)):
                        if(v==v_length(p,i,j,word)):
                            v_fit(word,p,i,j)
                            w.remove(word)
                        #break
                    else:
                        None
            if(h>1):
                for word in w:
                    #print(word,len(word),"\t",h)
                    if(h==len(word)):
                        print(h," ",i,j)
                        if(h==h_length(p,i,j,word)):
                            h_fit(word,p,i,j)
                            w.remove(word)
                        break
                    else:
                        None
    display(p)

def rec(p,w,it):
    print(it," ",len(w))
    for i in range(0,len(p)):
        for j in range(0,len(p[i])):
            if(len(w)==0):
                return True
            v=vd[i][j]
            h=hd[i][j]
            if(v>1 and len(w)>0):
                for wi in range(0,len(w)):
                    if(len(w)==0):
                        return True
                    word=w[wi]
                    if(v==len(word)):
                        if(v==v_length(p,i,j,word)):
                            cp=p.copy()
                            v_fit(word,p,i,j)
                            w.remove(word)
                            if(len(w)>0):
                                if(not rec(p,w,it+1)):
                                    w.insert(wi,word)
                                    p=cp
                                else:
                                    return True
                            else:
                                return True
                    else:
                        None
            if(h>1 and (len(w)>0)):
                for wi in range(0,len(w)):
                    if(len(w)==0):
                        return True
                    word=w[wi]
                    if(h==len(word)):
                        if(h==h_length(p,i,j,word)):
                            cp=p.copy()
                            h_fit(word,p,i,j)
                            w.remove(word)
                            if(len(w)>0):
                                #None
                                if(not rec(p,w,it+1)):
                                    w.insert(wi,word)
                                    p=cp.copy()
                                else:
                                    return True
                            else: 
                                return True
                    else:
                        None
    if(len(w)==0):
        return True
    else: 
        return False                   

def rb(p,w):
    word=w[0]
    for i in range(0,len(p)):
        for j in range(0,len(p[0])):
            #if(len(w)==0):
                #return True
            v=vd[i][j]
            h=hd[i][j]
            if(v==len(word)and len(w)>0):
                if(v==v_length(p,i,j,word)):
                    cp=p.copy()
                    v_fit(word,p,i,j)
                    w.remove(word)
                    if(len(w)==0):
                        print("Solution exists")
                        display(p)
                        exit(0)
                        #return True
                    else:
                        if(rb(p,w)):
                            return True
                        else:
                            p=cp
                            w.insert(0,word)
                        
            if(h==len(word) and len(w)>0):
                if(h==h_length(p,i,j,word)):
                    cp=p.copy()
                    h_fit(word,p,i,j)
                    w.remove(word)
                    if(len(w)==0):
                        print("Solution exists")
                        display(p)
                        exit(0)
                        #return True
                    else:
                        if(rb(p,w)):
                            None
                            #return True
                        else:
                            p=cp
                            w.insert(0,word)
    if(len(w)==0):
        return True
    else:
        return False


def main():
    file1 = open("puzzle5.txt","r+")
    p=file1.readlines()
    words0=[]
    puz=[]
    for i in range(0,len(p)):
        if(p[i].__contains__('.')|p[i].__contains__('*')):
            line=(p[i].replace('\n',''))
            for j in range(0,len(p[i])):
                line=(p[i].replace('\n',''))
            puz.append(line)
        else:
            words0.append(p[i])
    words=[]
    for i in words0:
        
        i=i.replace('\n','')
        words.append(i)
    for i in range(0,len(words)):
        for j in range(i,len(words)):
            if(len(words[i])<len(words[j])):
                temp=words[i]
                words[i]=words[j]
                words[j]=temp
    print(words)
    fil_d(puz)
    #rb(puz,words)
    if(rb(puz,words)):
        print("Solution exists")
        display(puz)

    else:
        print("Solution doesn't exists")
    #asdf(puz,words)
    #print(vertical_fit(puz,0,11))
    #print(horizontal_length(puz,0,11))
main()