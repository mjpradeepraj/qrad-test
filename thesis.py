import sys,os
os.system('cls')
print ('')


def main():
    
    eps = int(input('Enter Average Logs per second: '))
    os.system('cls')
    if eps >= 80000:
        print("\nLarger Size SOC\n")
        print("Enter the below value:")
        core = int(input("Processor Core (Nos): "))
        ram = int(input("RAM Memory (GB): "))
        disk = int(input("Disk Throughput (MB/s): "))
        storage = int(input("Disk Storage (TB): "))
        network = int(input("Network - Gigabit Ethernet Usage (Yes-1, No-0):"))
        db = int(input("DataBase (External-1,Embedded-0): "))
        log_collector = int(input("Log Collector (Nos): "))
        log_processor = int(input("Log Processor (Nos): "))
        log_src_count = int(input("Log Source Min Count (Nos): "))
        ticketing = int(input("Use of Ticketing Tool (Yes-1, No-0): "))
        taxii = int(input("TAXII feed Configured (Yes-1, No-0): "))
        analyst_count = int(input("Skilled Analyst Count (Nos): "))
        avg_time_offence = int(input("Average Time Taken to Complete One Offence (Mins): "))
        emp_train = int(input("Is Employee Training in place (Yes-1, No-0): "))
        cert_soc = int(input("Certified Analyst Availability (Yes-1, No-0): "))
        large(core,ram,disk,storage,network,db,log_collector,log_processor,log_src_count,ticketing,taxii,analyst_count,avg_time_offence,emp_train,cert_soc);
    elif eps >= 40000:
        print("\nMedium Size SOC\n")
        print("Enter the below value:")
        core = int(input("Processor Core (Nos): "))
        ram = int(input("RAM Memory (GB): "))
        disk = int(input("Disk Throughput (MB/s): "))
        storage = int(input("Disk Storage (TB): "))
        network = int(input("Network - Gigabit Ethernet Usage (Yes-1, No-0):"))
        db = int(input("DataBase (External-1,Embedded-0): "))
        log_collector = int(input("Log Collector (Nos): "))
        log_processor = int(input("Log Processor (Nos): "))
        log_src_count = int(input("Log Source Min Count (Nos): "))
        ticketing = int(input("Use of Ticketing Tool (Yes-1, No-0): "))
        taxii = int(input("TAXII feed Configured (Yes-1, No-0): "))
        analyst_count = int(input("Skilled Analyst Count (Nos): "))
        avg_time_offence = int(input("Average Time Taken to Complete One Offence (Mins): "))
        emp_train = int(input("Is Employee Training in place (Yes-1, No-0): "))
        cert_soc = int(input("Certified Analyst Availability (Yes-1, No-0): "))
        medium(core,ram,disk,storage,network,db,log_collector,log_processor,log_src_count,ticketing,taxii,analyst_count,avg_time_offence,emp_train,cert_soc);
    else:
        print("\nSmaller Size SOC\n")
        print("Enter the below value:")
        core = int(input("Processor Core (Nos): "))
        ram = int(input("RAM Memory (GB): "))
        disk = int(input("Disk Throughput (MB/s): "))
        storage = int(input("Disk Storage (TB): "))
        network = int(input("Network - Gigabit Ethernet Usage (Yes-1, No-0):"))
        db = int(input("DataBase (External-1,Embedded-0): "))
        log_collector = int(input("Log Collector (Nos): "))
        log_processor = int(input("Log Processor (Nos): "))
        log_src_count = int(input("Log Source Min Count (Nos): "))
        ticketing = int(input("Use of Ticketing Tool (Yes-1, No-0): "))
        taxii = int(input("TAXII feed Configured (Yes-1, No-0): "))
        analyst_count = int(input("Skilled Analyst Count (Nos): "))
        avg_time_offence = int(input("Average Time Taken to Complete One Offence (Mins): "))
        emp_train = int(input("Is Employee Training in place (Yes-1, No-0): "))
        cert_soc = int(input("Certified Analyst Availability (Yes-1, No-0): "))
        small(core,ram,disk,storage,network,db,log_collector,log_processor,log_src_count,ticketing,taxii,analyst_count,avg_time_offence,emp_train,cert_soc);


    

def large(core,ram,disk,storage,network,db,log_collector,log_processor,log_src_count,ticketing,taxii,analyst_count,avg_time_offence,emp_train,cert_soc):
    ## processor Core
    if core >= 48:
        core = 5
    elif core >= 24:
        core = 3
    elif core >= 16:
        core = 1
    elif core >= 4:
        core = 0
    else:
        core1 = 0 
        
    ## RAM
    if ram >= 128:
        ram = 5
    elif ram >= 64:
        ram = 2
    elif ram >= 32:
        ram = 1
    elif ram >= 16:
        ram = 0
    else:
        ram = 0
        
    ## Disk Throughput
    if disk >= 2000:
        disk = 5
    elif disk >= 1000:
        disk = 2
    elif disk >= 500:
        disk = 0
    else:
        disk = 0
        
    ## storage
    if storage >= 40:
        storage = 5
    elif storage >= 12:
        storage = 2
    elif storage >= 6:
        storage = 0
    else: 
        storage = 0
        
    ## Network
    if network == 1:
        network = 5
    elif network == 0:
        network =0
        
    ## db
    if db == 1:
        db = 5
    elif db == 0:
        db = 0
     
    ## log_collector
    if log_collector >= 8:
        log_collector = 5
    elif log_collector >= 6:
        log_collector = 2
    elif log_collector >= 2:
        log_collector = 0
    else: 
        log_collector = 0
        
    ## log_processor
    if log_processor >= 8:
        log_processor = 5
    elif log_processor >= 6:
        log_processor = 2
    elif log_processor >= 2:
        log_processor = 0
    else: 
        log_processor = 0
        
    ## log_src_count
    if log_src_count >= 8:
        log_src_count = 5
    elif log_src_count >= 6:
        log_src_count = 2
    elif log_src_count >= 4:
        log_src_count = 1
    else:
        log_src_count = 0
        
    ## ticketing
    if ticketing == 1:
        ticketing = 5
    elif ticketing == 0:
        ticketing = 0
        
    ## taxii
    if taxii == 1:
        taxii = 5
    elif taxii == 0:
        taxii = 0
    
    ## analyst_count
    if analyst_count >= 8:
        analyst_count = 5
    elif analyst_count >= 6:
        analyst_count = 2
    elif analyst_count >= 3:
        analyst_count = 0
    else:
        analyst_count = 0
        
    ## avg_time_offence
    if avg_time_offence > 25:
        avg_time_offence = 0
    elif avg_time_offence == 25:
        avg_time_offence = 1
    elif avg_time_offence >= 20:
        avg_time_offence = 2
    elif avg_time_offence <= 15:
        avg_time_offence = 5
        
    ## emp_train
    if emp_train == 1:
        emp_train = 5
    elif emp_train == 0:
        emp_train = 0
        
    ## cert_soc
    if cert_soc == 1:
        cert_soc = 5
    elif cert_soc == 0:
        cert_soc = 0
        
    print('\n')
    soc_list = [core,ram,disk,storage,network,db,log_collector,log_processor,log_src_count,ticketing,taxii,analyst_count,avg_time_offence,emp_train,cert_soc]
    avg = sum(soc_list)/len(soc_list)
    percentage= ((avg/5)*100)
    print("The SOC Performance is:", str(round(percentage))+'%')
    
    
        
        
def medium(core,ram,disk,storage,network,db,log_collector,log_processor,log_src_count,ticketing,taxii,analyst_count,avg_time_offence,emp_train,cert_soc):
    ## processor Core
    if core >= 48:
        core = 5
    elif core >= 24:
        core = 5
    elif core >= 16:
        core = 3
    elif core >= 4:
        core = 2
    else:
        core = 1 
        
    ## RAM
    if ram >= 128:
        ram = 5
    elif ram >= 64:
        ram = 5
    elif ram >= 32:
        ram = 3
    elif ram >= 16:
        ram = 1
    else:
        ram = 0
        
    ## Disk Throughput
    if disk >= 2000:
        disk = 5
    elif disk >= 1000:
        disk = 4
    elif disk >= 500:
        disk = 1
    else:
        disk = 0
        
    ## storage
    if storage >= 40:
        storage = 5
    elif storage >= 12:
        storage = 4
    elif storage >= 6:
        storage = 2
    else: 
        storage = 1
        
    ## Network
    if network == 1:
        network = 5
    elif network == 0:
        network =1
        
    ## db
    if db == 1:
        db = 5
    elif db == 0:
        db = 1
     
    ## log_collector
    if log_collector >= 8:
        log_collector = 5
    elif log_collector >= 6:
        log_collector = 3
    elif log_collector >= 2:
        log_collector = 1
    else: 
        log_collector = 0
        
    ## log_processor
    if log_processor >= 8:
        log_processor = 5
    elif log_processor >= 6:
        log_processor = 3
    elif log_processor >= 2:
        log_processor = 1
    else: 
        log_processor = 0
        
    ## log_src_count
    if log_src_count >= 8:
        log_src_count = 5
    elif log_src_count >= 6:
        log_src_count = 3
    elif log_src_count >= 4:
        log_src_count = 1
    else:
        log_src_count = 0
        
    ## ticketing
    if ticketing == 1:
        ticketing = 5
    elif ticketing == 0:
        ticketing = 1
        
    ## taxii
    if taxii == 1:
        taxii = 5
    elif taxii == 0:
        taxii = 1
    
    ## analyst_count
    if analyst_count >= 8:
        analyst_count = 5
    elif analyst_count >= 6:
        analyst_count = 3
    elif analyst_count >= 3:
        analyst_count = 2
    else:
        analyst_count = 1
        
    ## avg_time_offence
    if avg_time_offence > 25:
        avg_time_offence = 1
    elif avg_time_offence == 25:
        avg_time_offence = 2
    elif avg_time_offence >= 20:
        avg_time_offence = 3
    elif avg_time_offence <= 15:
        avg_time_offence = 5
        
    ## emp_train
    if emp_train == 1:
        emp_train = 5
    elif emp_train == 0:
        emp_train = 2
        
    ## cert_soc
    if cert_soc == 1:
        cert_soc = 5
    elif cert_soc == 0:
        cert_soc = 1
        
    print('\n')
    soc_list = [core,ram,disk,storage,network,db,log_collector,log_processor,log_src_count,ticketing,taxii,analyst_count,avg_time_offence,emp_train,cert_soc]
    avg = sum(soc_list)/len(soc_list)
    percentage= ((avg/5)*100)
    print("The SOC Performance is:", str(round(percentage))+'%')
    
def small(core,ram,disk,storage,network,db,log_collector,log_processor,log_src_count,ticketing,taxii,analyst_count,avg_time_offence,emp_train,cert_soc):
    ## processor Core
    if core >= 48:
        core = 5
    elif core >= 24:
        core = 5
    elif core >= 16:
        core = 5
    elif core >= 4:
        core = 3
    else:
        core = 2 
        
    ## RAM
    if ram >= 128:
        ram = 5
    elif ram >= 64:
        ram = 5
    elif ram >= 32:
        ram = 5
    elif ram >= 16:
        ram = 3
    else:
        ram = 1
        
    ## Disk Throughput
    if disk >= 2000:
        disk = 5
    elif disk >= 1000:
        disk = 5
    elif disk >= 500:
        disk = 3
    else:
        disk = 1
        
    ## storage
    if storage >= 40:
        storage = 5
    elif storage >= 12:
        storage = 5
    elif storage >= 6:
        storage = 3
    else: 
        storage = 2
        
    ## Network
    if network == 1:
        network = 5
    elif network == 0:
        network =2
        
    ## db
    if db == 1:
        db = 5
    elif db == 0:
        db = 3
     
    ## log_collector
    if log_collector >= 8:
        log_collector = 5
    elif log_collector >= 6:
        log_collector = 5
    elif log_collector >= 2:
        log_collector = 2
    else: 
        log_collector = 1
        
    ## log_processor
    if log_processor >= 8:
        log_processor = 5
    elif log_processor >= 6:
        log_processor = 5
    elif log_processor >= 2:
        log_processor = 2
    else: 
        log_processor = 1
        
    ## log_src_count
    if log_src_count >= 8:
        log_src_count = 5
    elif log_src_count >= 6:
        log_src_count = 5
    elif log_src_count >= 4:
        log_src_count = 2
    else:
        log_src_count = 1
        
    ## ticketing
    if ticketing == 1:
        ticketing = 5
    elif ticketing == 0:
        ticketing = 2
        
    ## taxii
    if taxii == 1:
        taxii = 5
    elif taxii == 0:
        taxii = 2
    
    ## analyst_count
    if analyst_count >= 8:
        analyst_count = 5
    elif analyst_count >= 6:
        analyst_count = 5
    elif analyst_count >= 3:
        analyst_count = 5
    else:
        analyst_count = 2
        
    ## avg_time_offence
    if avg_time_offence > 25:
        avg_time_offence = 1
    elif avg_time_offence == 25:
        avg_time_offence = 3
    elif avg_time_offence >= 20:
        avg_time_offence = 5
    elif avg_time_offence <= 15:
        avg_time_offence = 5
        
    ## emp_train
    if emp_train == 1:
        emp_train = 5
    elif emp_train == 0:
        emp_train = 3
        
    ## cert_soc
    if cert_soc == 1:
        cert_soc = 5
    elif cert_soc == 0:
        cert_soc = 2
        
    print('\n')
    soc_list = [core,ram,disk,storage,network,db,log_collector,log_processor,log_src_count,ticketing,taxii,analyst_count,avg_time_offence,emp_train,cert_soc]
    avg = sum(soc_list)/len(soc_list)
    percentage= ((avg/5)*100)
    print("The SOC Performance is:", str(round(percentage))+'%')
    
main();