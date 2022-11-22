import sys
import NetworkAttacker
import vars
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def menu():
        ''' Main menu to choose an item '''

        chosen_element = 0
        print("#############################################################################")
        print("########                                                             ########")
        print("########                                                             ########")
        print("########             Python project developed by: Roni               ########")
        print("######## ----------------------------------------------------------- ########")
        print(f"#######            Target is  {vars.target}                         ########")
        print("######## ----------------------------------------------------------- ########")
        print("########                                                             ########")
        print("########                    Choose an option:                        ########")
        print("########                                                             ########")
        print("########      1) Scan Netmask   |  2) View Open Ports                ########")
        print("########      3) Get MacAddress |  4) Exit                           ########")
        print("########                                                             ########")
        print("########                                                             ########")
        print("#############################################################################")
        while True:
            chosen_element = input("Enter a number from 1 to 5: ")
            if int(chosen_element) == 1:
                NetworkAttacker.netmaskscan(vars.target)
            elif int(chosen_element) == 2:
                NetworkAttacker.scanallports()
                if not vars.Open_Ports:
                    print("No open ports.")
                else:
                    print(vars.Open_Ports)
                if 22 in vars.Open_Ports:
                    ans = input("Would you like to ssh brute_force ? - y/n ")
                    if ans == 'y':
                        NetworkAttacker.ssh_brute_force(vars.target)
            elif int(chosen_element) == 3:
                NetworkAttacker.netmaskscan(vars.target)
            elif int(chosen_element) == 4:
                sys.exit()
        else:
            print('Sorry, the value entered must be a number from 1 to 4, then try again!')


if __name__ == '__main__' or '__NetworkAttacker__':
    ''' Python script main function '''

menu()
