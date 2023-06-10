#Use given file and will search for strings regular, root & Linux
#then will print and write them to given file.


def main():
    #read file.log fom user input
    log_file_path = input("Enter log file path: ")
    #python opens the file in read mode
    log_file = open(log_file_path, "r")
    #while using open() method Python will close the file when script ends
    #or we can close the file with log_file.close()
    output_file_path = input("Enter name of result file: ")
    #user provide path for output file with write mode
    with open(output_file_path, "w") as f:
        f.write("")
    output_file = open(output_file_path, "a")
    #for loop with variable named line that will iterate log_file
    #using .readlines() method
    for line in log_file.readlines():
        #print and write to the file only lines that include
        if ('regular' in line or 'root' in line and 'Linux' in line):
            print(line)
            output_file.write(line)

if __name__ == "__main__":
    try:
        main()
        print("file created successfully ")
    except Exception as e:
        print(e)

        
 
'''
example logs:
Time , 04:55 , IP:149.25.2.7 , Protocol:RDP , Permission:admin , OS:Windows
Time , 04:58 , IP:149.68.85.194 , Protocol:SSH , Permission:regular , OS:Linux
Time , 05:05 , IP:172.25.10.5 , Protocol:SMB , Permission:admin , OS:Windows
Time , 05:13 , IP:149.192.2.89 , Protocol:TCP , Permission:admin , OS:Windows
Time , 05:55 , IP:149.39.2.9 , Protocol:RDP , Permission:root , OS:Linux
Time , 05:55 , IP:149.39.2.9 , Protocol:RDP , Permission:admin , OS:Linux
Time , 06:12 , IP:1.25.2.1 , Protocol:RDP , Permission:admin , OS:Windows
Time , 06:31 , IP:58.25.4.8 , Protocol:SSH , Permission:root , OS:Linux
Time , 07:42 , IP:149.24.2.7 , Protocol:RDP , Permission:admin , OS:Windows
Time , 08:02 , IP:149.25.2.6 , Protocol:RDP , Permission:admin , OS:Windows
Time , 08:17 , IP:149.241.76.1 , Protocol:RDP , Permission:admin , OS:Windows
Time , 08:24 , IP:149.25.2.98 , Protocol:UDP , Permission:root , OS:Linux
Time , 09:46 , IP:234.30.56.7 , Protocol:RDP , Permission:regular , OS:Windows
'''
