import pandas as pd
import pprint

#data = pd.read_csv(r'/Users/mktgit/Desktop/Code/PamelasCode/187Calls.csv')
#data = pd.read_csv(r'/Users/mktgit/Desktop/Code/PamelasCode/auglm.csv')
data = pd.read_csv(r'/Users/mktgit/Desktop/Code/Mine/time.csv')
df = pd.DataFrame(data, columns=['From','To','Disposition'])

clients = pd.read_csv(r'/Users/mktgit/Desktop/Code/MessageEf/Clients.csv')
clientsFrame = pd.DataFrame(clients, columns=['First Name','Last Name','Contact Type','Contact Group','Cell Phone','City','State','Zip Code'])


count = 0
the_list = [] #List of phone numbers all of em'
answered = [] #numbers who contacted meneses
called = ['+18328314242(+18328314242)'] #people who meneses sucessfully called
dictionary3 = {}
dictionary = {}
dictionary2 ={}
#Getting the MISSED CALLED phone numbers into an array list
count = 0

for v in df['Disposition']:
    count= count +1
    if (v == 0):
        #print(df.loc[count,"From"]) #note1
        temp = df.loc[count-1,"From"]
        #print(temp[11:])
        temp = temp[-14:]
        temp2 =temp[3:13]
        #the_list.append(temp) # overall missed call
        if temp not in the_list:
            the_list.append(temp) # overall missed call
        if temp in the_list:
            if temp not in dictionary2:
                dictionary2[temp]=1
            if temp in dictionary2:
                #print("doubles")
                dictionary2[temp]=dictionary2[temp]+1



    if ( v != 0):
        if(df.loc[count-1,"From"] == '+18328314242(+18328314242)'):
            called.append(df.loc[count-1,"To"])
            temp = temp[-14:]
        else:
            temp = df.loc[count-1,"From"]
            temp = temp[-14:]
            temp2 =temp[3:13]
            answered.append(temp)

    #     answered.append(df.loc[count-1,"From"]) # we picked up
    #     #count= count+1
    # if ( v != 0):
    #     called.append(df.loc[count-1,"To"]) #called
#print("=============checkpoint=============")
cc = 0
clients =0
clients_list =[]
for v in clientsFrame['Contact Type']:
    cc= cc +1
    if (v == 'Client'):
        clients += 1
        #print(df.loc[count,"From"]) #note1
        temp = str(clientsFrame.loc[cc-1,"Cell Phone"])
        #temp = temp[-14:]
        #temp = temp[3:13]
        #print(temp)
        temp1=temp[1:4]
        temp2=temp[6:9]
        temp3=temp[10:14]
        temp = temp1+temp2+temp3
        #print(temp)
        if temp not in clients_list:
            clients_list.append(temp)





print("////////// \n")
print("The amount of calls  is : ")
print(count)
print("//////////\n")

clean_list = [] #this is the weeded out list, who we called, who did press 1 after
#and even who called afterards and got in contact is out
count2 = 0
for i in the_list:
    if i not in clean_list:
        if i not in answered:
            if i not in called:
                clean_list.append(i)
                count2 += 1


for i in clean_list:
    if i in dictionary2:
        temp = i
        i = i[-14:]
        i = i[3:13]
        dictionary[i] = dictionary2[temp]



print("the count of missed calls is  ")
print(count2)
print(" ")
# print("*****************************************************")
# for i in clean_list:
#     print (i)
##original dictionary pprint
# print("The list of poeple who call multiple times ")
#
# #pprint.pprint(dictionary)
#
#hidden
# print("People who have called overall")
# sorted_dict = sorted(dictionary, key=dictionary.get, reverse=True)
# for r in sorted_dict:
#     print(r,dictionary[r])
#hidden****************************************************************************
#########Right ########## TOP

#######FIX BOTTOM ########
client_dict ={}
client_count= 0
customer_dict = {}
customer_count = 0

#print(clients_list)
#print(dictionary)
for i in dictionary:
    if i in clients_list:
        if i in client_dict:
            client_dict[i] = client_dict[i] + 1

        if i not in client_dict:
            client_dict[i] = dictionary[i]
            #print("client")
            client_count += 1

        #client_count +=1
    if i not in clients_list:
        if i in customer_dict:
            customer_dict[i] = customer_dict[i] + 1

        if i not in customer_dict:
            customer_dict[i] = dictionary[i]
            #print("missed cstomer")
            customer_count += 1

#The top is wrong because its not adding the correct phone numbers on the correct list
        #
        # if temp in the_list:
        #     if temp not in dictionary:
        #         dictionary[temp]=2
        #     if temp in dictionary:
        #         #print("doubles")
        #         dictionary[temp]=dictionary[temp]+1
        #


## something is wrong ont the bottom
print("--------------    Missed calls  -------------")

print("")
print("")
print("customers")

sorted_dict2 = sorted(customer_dict, key=dictionary.get, reverse=True)
for r in sorted_dict2:
    print(r,customer_dict[r])

print(" ")
print(" ")
print("---")
print("clients")
#print(client_dict)

sorted_dict3 = sorted(client_dict, key=dictionary.get, reverse=True)
for r in sorted_dict3:
    print(r,client_dict[r])





#        print("This one is a missed customer")
    #print(r,dictionary[r])
print("")
print("==========================")
print("NEW customer")
print(customer_count)
print("CLIENT")
print(client_count)
print("amount of dif people")
print(len(dictionary))



print("")
print("")
# print("give these to VAS ==========")
# for i in customer_dict:
#     print(i)
#
# print(the_list)
# print(answered)
# print(clients_list)

total_client_call_count = 0
total_new_customer_call_count = 0
for i in the_list:
    i = i[-14:]
    i = i[3:13]
    if i in clients_list:
        total_client_call_count +=1
    if i not in clients_list:
        total_new_customer_call_count +=1


print("-----------------------------")
print("TOTALS ")
print(" new customers ")
print(total_new_customer_call_count)
print(" Client")
print(total_client_call_count)
