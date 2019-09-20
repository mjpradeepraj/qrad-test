import requests, json, sys, os, datetime
from dateutil.parser import parse
import configparser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

##### IP/API Selection #####
config = configparser.ConfigParser()
config.read('config.ini')

IP= config['MSSP1']['IP']
api_key = config['MSSP1']['api_key']


##### For Auto run script #####

#count_days = int('1')
#check_code =str('ERROR') 

##### For Manual User Input ########
print('\n\t######## State ########\n\t\t1.ALL\n\t\t2.SUCCESS\n\t\t3.ERROR\n\t#######################\n')
usr_check = input('Select the Log source state: ')
if usr_check == "1":
    check_code =str('ALL')
elif usr_check == "2":
    check_code = str('SUCCESS')
elif usr_check == "3":
    check_code = str('ERROR')
else:
    print('\nErr.Invalid Input..!')
    os.system('pause')
    exit()

try:
    count_days=int(input('\nEnter Number of days: '))
except ValueError:
    print('\nErr.Invalid Integer Input..!')
    os.system('pause')
    exit()
    
###### Main Block ######
now = datetime.datetime.now()
output_file = IP+'_'+now.strftime("%d%M%Y_%I_%M_%p_")+check_code+'.csv'
if(os.access(output_file, os.F_OK)):
    print("\nCleaning Previous Run..!\n")
    os.remove(output_file)
    file_object = open(output_file, 'w')
    file_object.write('"ID","Name","Description","Log Source","Status","Last Event","Not Connected for"\n')
    file_object.close()
else:
    file_object = open(output_file, 'w')
    file_object.write('"ID","Name","Description","Log Source","Status","Last Event","Not Connected for"\n')
    file_object.close()

url = "https://" + IP + "/api/config/event_sources/log_source_management/log_sources"

headers = {
    'SEC': api_key,
    'Range': 'items=0-500',
    'Version': '9.1'
}

json_data = requests.get(url, headers=headers, verify=False).json()
for log in json_data:
    file_object = open(output_file, 'a')
    id1=log['id']
    name1=log['name']
    desc= log['description']
    log_src='log source'#log['protocol_parameters']
    
    #print(log_src[1]['value'])
    
    ###Log source Status Read####
    stat=log['status']
    if  ("SUCCESS") in str(stat):
        stat = "SUCCESS"
    elif ("ERROR")in str(stat):
        stat = ("ERROR")
    elif("NA") in str(stat):
        stat = ("NA")
    elif("DISABLED") in str(stat):
        stat = ("DISABLED")
    else:
        stat = ("WARN")
   
    if (stat == check_code) or (check_code == "ALL"):
        #####Date read#####
        last_event= log['last_event_time']
        if str(last_event) == "0":
            print('"',id1,'","',name1,'","',desc,'","',log_src,'","',stat,'","',str(last_event),'","','NIL','"',file=file_object)
            continue
        else:
            base_datetime = datetime.datetime( 1970, 1, 1 )
            delta = datetime.timedelta( 0, 0, 0, last_event)
            target_date = (base_datetime + delta)
            last_date=target_date.strftime("%m/%d/%Y %I:%M %p")
            not_con=(datetime.datetime.now() - (parse(last_date)))
            answer= not_con > datetime.timedelta(days = count_days)
            if answer == True:
                if log['enabled'] == True:
                    print('"',id1,'","',name1,'","',desc,'","',log_src,'","',stat,'","',last_date,'","',not_con,'"',file=file_object)
    else:
        continue
    
file_object.close()
print('\nProcessed Successfully..!\n')
os.system('pause')
exit()