from tabulate import tabulate
import datetime



# Dictionary Variables.............


swimmers = {'MGMG': {'Name': ['MGMG'], 'Age': ['18'], 'Gender': ['male'] ,'Status' : ['active'],'Event':[],'Time':[],"Meet":[]},'APPLE': {'Name': ['APPLE'], 'Age': ['18'], 'Gender': ['male'] ,'Status' : ['active'],'Event':[],'Time':[],"Meet":[]}}

# total_record_swimmers_real={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[],'Post_Status': []}


record_swimmers_temp ={}

record_swimmers_real ={}

# record_swimmers_real_table= {'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[]}


#register_status
reg_status_true = "active"
reg_status_false = "inactive"

#post status
post_status_true ="posted"
post_status_false ="unposted"

# function
#input_validation_function
def check_name(check_reg_name):
    
    if check_reg_name.isalpha():
        return True
    else:
        return False

#check date function
def check_date(check_reg_date):

    year,month,day = check_reg_date.split('/')
    #check input_validation_for age
    
    try:
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        return False

#check gender

def check_gender(check_reg_gender):
    
    if check_reg_gender == '1':
        return ['Male']
    elif check_reg_gender == '2':
        return ['Female']
    elif check_reg_gender == '3':
        return ['Others']
    else:
        return False


# check register swimmers
def registered_swimmers():
    register_swimmers_table={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[]}
    for x in swimmers.values():
        
        for a in x['Name']:
            register_swimmers_table['Name'].append(a)

        for a in x['Age']:
            register_swimmers_table['Age'].append(a)

        for a in x['Gender']:
            register_swimmers_table['Gender'].append(a)

        for a in x['Status']:
            register_swimmers_table['Status'].append(a)

        for a in x['Event']:
            register_swimmers_table['Event'].append(a)
                    
        for a in x['Time']:
            register_swimmers_table['Time'].append(a)
                    
        for a in x['Meet']:
            register_swimmers_table['Meet'].append(a)
                
    print("\n\n\n"+ tabulate(register_swimmers_table, headers='keys'))            
    main_program = True   

# check recorded swimmers
def recorded_swimmers():
    record_swimmers_temp_table ={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[],'Post_Status':[]}
    for temp_swimmer in record_swimmers_temp.values():

        for b in temp_swimmer['Name']:
            record_swimmers_temp_table['Name'].append(b)

        for b in temp_swimmer['Age']:
            record_swimmers_temp_table['Age'].append(b)

        for b in temp_swimmer['Gender']:
            record_swimmers_temp_table['Gender'].append(b)

        for b in temp_swimmer['Status']:
            record_swimmers_temp_table['Status'].append(b)

        for b in temp_swimmer['Event']:
            record_swimmers_temp_table['Event'].append(b)
                    
        for b in temp_swimmer['Time']:
            record_swimmers_temp_table['Time'].append(b)
                    
        for b in temp_swimmer['Meet']:
            record_swimmers_temp_table['Meet'].append(b)
                        
        for b in temp_swimmer['Post_Status']:
            record_swimmers_temp_table['Post_Status'].append(b)
                

    print("\n\n\n"+ tabulate(record_swimmers_temp_table, headers='keys'))            
        


# check real swimmers
def real_swimmers():
    real_swimmer_table ={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[],'Post_Status':[]}
    for real_swimmer in record_swimmers_real.values():

        for b in real_swimmer['Name']:
            real_swimmer_table['Name'].append(b)

        for b in real_swimmer['Age']:
            real_swimmer_table['Age'].append(b)

        for b in real_swimmer['Gender']:
            real_swimmer_table['Gender'].append(b)

        for b in real_swimmer['Status']:
            real_swimmer_table['Status'].append(b)

        for b in real_swimmer['Event']:
            real_swimmer_table['Event'].append(b)
                    
        for b in real_swimmer['Time']:
            real_swimmer_table['Time'].append(b)
                    
        for b in real_swimmer['Meet']:
            real_swimmer_table['Meet'].append(b)
                        
        for b in real_swimmer['Post_Status']:
            real_swimmer_table['Post_Status'].append(b)
                

    print("\n\n\n"+ tabulate(real_swimmer_table, headers='keys'))            
        
    main_program = True

# check individual swimmers
def search_swimmers(search_results):
    
    print("\n\n\n"+ tabulate(search_results, headers='keys'))            
        
    main_program = True




#Main Program.........

#For Registering.....................

main_program = True
while main_program == True:
    user_choice = input("\n\n\nFor register press 1\nFor record swimmer time press 2\nTo search individual press 3\nTo search individual by event press 4\nTo remove player press 5\nTo execute program press 6\nEnter Your option:")
    if user_choice == '6':
        main_program = False
    if user_choice == 'apple':        
       registered_swimmers()
    if user_choice == 'banana':        
       recorded_swimmers()       
    if user_choice == '1':

        input_loop = True
    
        while input_loop == True:

            reg_name  = input("Enter name:").upper()

            #check input_validation_for name  
            check_name(reg_name)                                 
            while check_name(reg_name) == False:
                print("Only allow alphabets for name")
                reg_name  = input("Enter name:")
                check_name(reg_name)



            if reg_name in swimmers and [reg_status_false] == swimmers[reg_name]['Status']:
                swimmers[reg_name]['Status'] = [reg_status_true]


                #inactive to active status in real table
                if  reg_name in record_swimmers_real:
                    b=[]
                    for counter in range(len(record_swimmers_real[reg_name]['Status'])):
                        b.append(reg_status_true)
                        # print (counter, "Counter")
                    record_swimmers_real[reg_name]['Status']=b
                
                print("This username is now active")
                input_loop = False
                main_program = True
                

            elif reg_name in swimmers and [reg_status_true] == swimmers[reg_name]['Status']:
                print("This user is already active")
                input_loop = False
                main_program = True
                
            else:
                input_loop = False
                swimmers[reg_name]={}
                swimmers[reg_name]['Name']=[reg_name]

                reg_dob= input("Enter data of birth in format yy/mm/dd:")

                #check input_validation_for dateTime  
                check_date(reg_dob)
                while check_date(reg_dob) == False:
                    print("Input date is not valid..")
                    reg_dob= input("Enter data of birth in format yy/mm/dd:")
                    check_date(reg_dob)
                swimmers[reg_name]['Age']=[reg_dob] 


                reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
                check_gender(reg_gen)
                while check_gender(reg_gen) == False:
                    reg_gen= input("Enter 1 for Male\nEnter 2 for Female\nEnter 3 for Others\nEnter your gender number:")
                    check_gender(reg_gen)
                    
                swimmers[reg_name]['Gender']=check_gender(reg_gen)

            
                swimmers[reg_name]['Status']=[reg_status_true]
                swimmers[reg_name]['Event']=[None]
                swimmers[reg_name]['Time']=[None]
                swimmers[reg_name]['Meet']=[None]


                print("Register Successful and now active")

               
        registered_swimmers() #table for register

#...........................Record Swimmers..........................
    elif user_choice == '2':
        record_name = input('Enter player name to record(must be registered):').upper()

        if record_name in swimmers:
            
            record_event_type =input("Choose the event type\nPress 1 for Freestyle\nPress 2 for Backstroke\nPress 3 for Breaststroke\nPress 4 for Butterfly\nPress 5 for individual Medley\nEnter your type:")

            

            if record_event_type == '1':
                record_event_meter_range=('50','100','200','400','800','1500')
                record_event_input_status = True
                while record_event_input_status == True:
                    record_event_meter= input('Choose between meter 50,100,200,400,800,1500:')
                    if record_event_meter in record_event_meter_range:
                        record_event_type_detail="Freestyle: "+record_event_meter+"m"
                        record_event_input_status = False
                    else:
                        print('invalid input range')
                        record_event_input_status = True

            elif record_event_type == '2':
                record_event_meter_range=('50','100','200')
                record_event_input_status = True
                while record_event_input_status == True:
                
                    record_event_meter= input('Choose between meter 50,100,200:')
                    if record_event_meter in record_event_meter_range:
                            record_event_type_detail ="Backstroke: "+record_event_meter+"m"
                            record_event_input_status = False
                    else:
                        print('invalid input range')
                        record_event_input_status = True

            elif record_event_type == '3':
                record_event_meter_range=('50','100','200')
                record_event_input_status = True
                while record_event_input_status == True:
                
                    record_event_meter= input('Choose between meter 50,100,200:')
                    if record_event_meter in record_event_meter_range:
                            record_event_type_detail = "Breastroke: "+record_event_meter+"m"
                            record_event_input_status = False
                    else:
                        print('invalid input range')
                        record_event_input_status = True


            elif record_event_type == '4':
                record_event_meter_range=('50','100','200')
                record_event_input_status = True
                while record_event_input_status == True:
                
                    record_event_meter= input('Choose between meter 50,100,200:')
                    if record_event_meter in record_event_meter_range:
                            record_event_type_detail = "Butterfly: "+record_event_meter+"m"
                            record_event_input_status = False
                    else:
                        print('invalid input range')
                        record_event_input_status = True
            
            elif record_event_type == '5':
                record_event_meter_range=('50','100','200')
                record_event_input_status = True
                while record_event_input_status == True:
                
                    record_event_meter= input('Choose between meter 100,200,400:')
                    if record_event_meter in record_event_meter_range:
                            record_event_type_detail = "Individual Medley: "+record_event_meter+"m"
                            record_event_input_status = False
                    else:
                        print('invalid input range')
                        record_event_input_status = True


            else:
                print("invaild input")
                main_program = True

            record_time=input("Enter time to record(eg.01:11:00):")
            record_meet=input("Enter the name of competition:").upper()

# ........................................avoid duplicate record......................................
            # if (record_event_type_detail in record_swimmers_real[record_name]['Event'] and record_time in record_swimmers_real[record_name]['Time'] and record_meet in record_swimmers_real[record_name]['Meet']) or (record_event_type_detail in record_swimmers_temp[record_name]['Event'] and record_time in record_swimmers_temp[record_name]['Time'] and record_meet in record_swimmers_temp[record_name]['Meet']):
            #     print("You can not add same record twice")
            #     main_program = True

            if 1==1: #temporary pause above program for some error :(

    #......................................Check Already Record and Register swimmer............................            
                if record_name in list(swimmers.keys()) and ((record_name in list(record_swimmers_temp.keys()) or record_name in list(record_swimmers_real.keys()) or record_name in list(record_swimmers_real.keys()) and record_name in list(record_swimmers_temp.keys()))):
                    print('1')
                    if record_name in list(record_swimmers_temp.keys()) and record_name not in list(record_swimmers_real.keys()):
                        print('1.1')
                        record_swimmers_temp[record_name]['Name'].append(swimmers[record_name]['Name'][0])
                        record_swimmers_temp[record_name]['Age'].append(swimmers[record_name]['Age'][0])
                        record_swimmers_temp[record_name]['Gender'].append(swimmers[record_name]['Gender'][0])
                        record_swimmers_temp[record_name]['Status'].append(swimmers[record_name]['Status'][0])
                        record_swimmers_temp[record_name]['Event'].append(record_event_type_detail)
                        record_swimmers_temp[record_name]['Time'].append(record_time)
                        record_swimmers_temp[record_name]['Meet'].append(record_meet)
                        record_swimmers_temp[record_name]['Post_Status'].append(post_status_false)

                    elif record_name in list(record_swimmers_real.keys()) and record_name not in list(record_swimmers_temp.keys()): 
                        print('1.2')
                        if record_swimmers_temp == {} or (record_swimmers_temp != {} and record_name not in record_swimmers_temp):
                            print('1.2.1')  
                            # print(list(record_swimmers_real.keys()))
                            record_swimmers_temp[record_name]={}
                            record_swimmers_temp[record_name]['Name']=[record_name]
                            record_swimmers_temp[record_name]['Age']=[swimmers[record_name]['Age'][0]]
                            record_swimmers_temp[record_name]['Gender']=[swimmers[record_name]['Gender'][0]]
                            record_swimmers_temp[record_name]['Status']=[swimmers[record_name]['Status'][0]]
                            record_swimmers_temp[record_name]['Event']=[record_event_type_detail]
                            record_swimmers_temp[record_name]['Time']=[record_time]
                            record_swimmers_temp[record_name]['Meet']=[record_meet]
                            record_swimmers_temp[record_name]['Post_Status']=[post_status_false]

                        else:
                            print('1.2.2')
                            record_swimmers_temp[record_name]['Name'].append(swimmers[record_name]['Name'][0])
                            record_swimmers_temp[record_name]['Age'].append(swimmers[record_name]['Age'][0])
                            record_swimmers_temp[record_name]['Gender'].append(swimmers[record_name]['Gender'][0])
                            record_swimmers_temp[record_name]['Status'].append(swimmers[record_name]['Status'][0])
                            record_swimmers_temp[record_name]['Event'].append(record_event_type_detail)
                            record_swimmers_temp[record_name]['Time'].append(record_time)
                            record_swimmers_temp[record_name]['Meet'].append(record_meet)
                            record_swimmers_temp[record_name]['Post_Status'].append(post_status_false)


                    elif record_name in list(record_swimmers_real.keys()) and record_name in list(record_swimmers_temp.keys()):
                            print('1.3')
                            record_swimmers_temp[record_name]['Name'].append(swimmers[record_name]['Name'][0])
                            record_swimmers_temp[record_name]['Age'].append(swimmers[record_name]['Age'][0])
                            record_swimmers_temp[record_name]['Gender'].append(swimmers[record_name]['Gender'][0])
                            record_swimmers_temp[record_name]['Status'].append(swimmers[record_name]['Status'][0])
                            record_swimmers_temp[record_name]['Event'].append(record_event_type_detail)
                            record_swimmers_temp[record_name]['Time'].append(record_time)
                            record_swimmers_temp[record_name]['Meet'].append(record_meet)
                            record_swimmers_temp[record_name]['Post_Status'].append(post_status_false) 



            #......................................Check Register swimmer but not Record............................  
                elif record_name in list(swimmers.keys()) and record_name not in list(record_swimmers_temp.keys()):
                    print('2')
                    record_swimmers_temp[record_name]={}
                    record_swimmers_temp[record_name]['Name']=[record_name]
                    record_swimmers_temp[record_name]['Age']=[swimmers[record_name]['Age'][0]]
                    record_swimmers_temp[record_name]['Gender']=[swimmers[record_name]['Gender'][0]]
                    record_swimmers_temp[record_name]['Status']=[swimmers[record_name]['Status'][0]]
                    record_swimmers_temp[record_name]['Event']=[record_event_type_detail]
                    record_swimmers_temp[record_name]['Time']=[record_time]
                    record_swimmers_temp[record_name]['Meet']=[record_meet]
                    record_swimmers_temp[record_name]['Post_Status']=[post_status_false]


                recorded_swimmers()
                print(record_swimmers_temp)
                # ....................................posted_unposted..........................................

                check_post_status_input = input("Do you want to post all the unposted data(y/n):")
                if check_post_status_input == 'y':
                    print('banana')

                    for record_key,record_value in record_swimmers_temp.items():
                        print(record_key, "Key")
                        print(record_value, "Value")

                        if record_key not in record_swimmers_real:
                            print(record_key, "Loop record key")
                            # record_swimmers_real = {}
                            record_swimmers_real[record_key]=record_value 
                            for counter in range(len(record_value['Post_Status'])):
                                if counter == 0:
                                    record_swimmers_real[record_key]['Post_Status']=[post_status_true]

                                if counter != 0:
                                    
                                    record_swimmers_real[record_key]['Post_Status'].append(post_status_true)

                            # record_swimmers_real[record_key]['Name'] = record_value['Name']
                        else:
                            for counter in range(len(record_value['Name'])):
                                # print (counter, "Counter")
                                record_swimmers_real[record_key]['Name'].append(record_value['Name'][counter])
                            for counter in range(len(record_value['Age'])):
                                # print (counter, "Counter")
                                record_swimmers_real[record_key]['Age'].append(record_value['Age'][counter])
                            for counter in range(len(record_value['Gender'])):
                                # print (counter, "Counter")
                                record_swimmers_real[record_key]['Gender'].append(record_value['Gender'][counter])
                            for counter in range(len(record_value['Status'])):
                                # print (counter, "Counter")
                                record_swimmers_real[record_key]['Status'].append(swimmers[record_key]['Status'][0])
                            for counter in range(len(record_value['Event'])):
                                # print (counter, "Counter")
                                record_swimmers_real[record_key]['Event'].append(record_value['Event'][counter])

                            for counter in range(len(record_value['Time'])):
                                # print (counter, "Counter")
                                record_swimmers_real[record_key]['Time'].append(record_value['Time'][counter])

                            for counter in range(len(record_value['Meet'])):
                                # print (counter, "Counter")
                                record_swimmers_real[record_key]['Meet'].append(record_value['Meet'][counter])

                            for counter in range(len(record_value['Post_Status'])):
                                # print (counter, "Counter")
                                record_swimmers_real[record_key]['Post_Status'].append(post_status_true)


                    record_swimmers_temp.clear()
                    print(record_swimmers_real,"REAL SWIMMERS")

                    real_swimmers()
                
                
                else:
                    main_program = True



                

        else:
            print("no user found")
            main_program = True

# ....................................Total Swimmer Detail.................................            
    elif user_choice == '3':

        search_name = input("Enter name to search:").upper()
        if  search_name in record_swimmers_real:
            search_swimmers(record_swimmers_real[search_name])
            main_program=True
        else:
            print('Invalid Input')
            main_program=True

    elif user_choice == '4':

        search_name = input("Enter name to search:").upper() 
        search_meet = input("Enter name to search:").upper()

        search_NameAndMeet_table={'Name':[],"Age":[],"Gender":[],"Status":[],"Event":[],"Time":[],"Meet":[],"Post_Status":[]}

        if  search_name in record_swimmers_real and search_meet in record_swimmers_real[search_name]['Meet']:
                
            i=0
            for x in record_swimmers_real[search_name]['Meet']:
                if search_meet == x:
                    
                    
                    search_NameAndMeet_table['Name'].append(record_swimmers_real[search_name]['Name'][i])
                    search_NameAndMeet_table['Age'].append(record_swimmers_real[search_name]['Age'][i])
                    search_NameAndMeet_table['Gender'].append(record_swimmers_real[search_name]['Gender'][i])
                    search_NameAndMeet_table['Status'].append(record_swimmers_real[search_name]['Status'][i])
                    search_NameAndMeet_table['Event'].append(record_swimmers_real[search_name]['Event'][i])
                    search_NameAndMeet_table['Time'].append(record_swimmers_real[search_name]['Time'][i])
                    search_NameAndMeet_table['Meet'].append(record_swimmers_real[search_name]['Meet'][i])
                    search_NameAndMeet_table['Post_Status'].append(record_swimmers_real[search_name]['Post_Status'][i])
                    i+=1
                if search_meet != x:
                    i+=1
            

            search_swimmers(search_NameAndMeet_table)
            main_program=True
        else:
            print('Invalid Input')
            main_program=True


    elif user_choice == '5':
    
        search_name = input("Enter name to search:").upper()
        if  search_name in record_swimmers_real:

            swimmers[search_name]['Status']= [reg_status_false]

            y=[]
            for counter in range(len(record_swimmers_real[search_name]['Status'])):
                y.append(reg_status_false)
                # print (counter, "Counter")
            record_swimmers_real[search_name]['Status']=y



            

            main_program=True
        else:
            print('Invalid Input')
            main_program=True    

            