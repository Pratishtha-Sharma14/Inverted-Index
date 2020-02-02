#importing posting lists from CSV
def import_lists():
    final_dict= dict()
    with open('Posting Lists.csv', 'r') as csvfile:
        Key_words= list()
        Posting_Lists= list()
        for line in csvfile.readlines():
            comma= line.find(',')
            word= line[0:comma]
            rest= line[comma+1: len(line)-1]
            s_ind= rest.find("[")
            e_ind= rest.find("]")
            rest= rest[s_ind+1: e_ind]
            plist= rest.split(',')
            Key_words.append(word)
            l1= list()
            for x in plist:
                x= x.replace(" ", "")
                l1.append(int(x))
            Posting_Lists.append(l1)
            
        for i in range(0, len(Key_words)):
            final_dict[Key_words[i]]= Posting_Lists[i]
    
    csvfile.close()
    
    return final_dict

def AND(list1, list2):
    result= list()
    for x in list1:
        if x in list2:
            result.append(x)
    result.sort()  
    return result

def OR(list1, list2):
    result= list()
    len1= len(list1)
    len2= len(list2)
    if len1>=len2: 
        result= list1
        for x in list2:
            if x not in result:
                result.append(x)
    else:
        result= list2
        for x in list2:
            if x not in result:
                result.append(x)
                
    result.sort()
    return result

def NOT(list1):
    temp= list()
    result= list()
    for i in range(1, 28):
        temp.append(i)
        
    for x in temp:
        if x not in list1:
            result.append(x)
    
    result.sort()
    return result

final_dict= import_lists()
Query= str(input("Enter Query or enter NULL to quit\n"))
while(Query!="NULL"):
    data= Query.split()
    operators= list()
    operands= list()
    temp= 0
    while temp< len(data):
        operands.append(data[temp])
        temp=temp+2
    temp= 1
    while temp< len(data):
        operators.append(data[temp])
        temp=temp+2
    
    posting_lists= list()
    for x in operands:
        posting_lists.append(final_dict[x])
    
    result= list()
    if len(operators)==1:
        if operators[0]=="and":
            result= AND(posting_lists[0], posting_lists[1])
        
        elif operators[0]=="or":
            result= OR(posting_lists[0], posting_lists[1])
        else:
            result= NOT(final_dict[operators[0]])
        
    else:
        for i in range(0, len(operators)):
            if operators[i]=="and":
                result= AND(posting_lists[0], posting_lists[1])
            elif operators[i]=="or":
                result= OR(posting_lists[0], posting_lists[1])
            else:
                result= AND(posting_lists[0], NOT(posting_lists[1]))
                
            posting_lists.pop(0)
            posting_lists.pop(0)
            posting_lists.insert(0, result)
        
    print(result)
    Query= str(input("Enter Query or enter NULL to quit\n"))
        
if Query== "NULL":
    print("Thank you. Good Bye")