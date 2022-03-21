#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# SSyjuco, 2022-Mar-20, Added code to complete the requirements for Assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []  #need to add code somwhere, maybe to the new CD creation one to automatically append the CD 
# to this listofCDOBjects after the creation of each 

class CD:
    """Stores data about a CD:
    
        
    properties: #these are the different object properties we need to raise. CD is the object
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TO done Add Code to the CD class
    def __init__(self, cdid, cdtitle, cdartist):
        """CD Object constructor that creates CD object with attributes cdid, cdtitle, cdartist"""
        self.cdid = cdid
        self.cdtitle = cdtitle
        self.cdartist = cdartist
        
    def __str__(self):
        """ Object instance method to display human friendly version of CD attributes"""
        
        return f"{self.cdid}    {self.cdtitle} {self.cdartist}"        
    
    @staticmethod
    def add_cd():
        """ Function to add CD details to memory
        
        Args: 
            None.
        
        Returns:
            IO.show_invenotry(lstOfCDObjects) # this calls the IO function show_inventory(lstOfCDObjects) to confirm to the user what was added to the table 
        
        
        """
        newlst = []
        newlst = IO.input_cd()
        new_cd = CD(newlst[0], newlst[1], newlst[2])
        lstOfCDObjects.append(new_cd)
        return IO.show_inventory(lstOfCDObjects)

    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TO done Add code to process data from a file
    #TO done how to read a list of objects 
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        objFile = open(file_name, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')   
            lstOfCDObjects.append(lstRow)
        
    # TO done Add code to process data to a file
    # Can we simplify this to write the results of the read info anyway? or whatever the latest lst of CD objects is?
    @staticmethod
    def write_file(file_name, table): 
        """Function to save the CDs currently in memory to the text file CDInventory.txt
        
        Args:
            file_name: name of the file to be written to
            table: the list of CD objects that will be written to the file 
        
        Returns: 
            None. 
        
        """
        objFile = open(strFileName, 'a')
        for row in table:
            strCDs = ''
            strCDs += str(row) + ','
            strCDs = strCDs[:-1] + '\n'
            objFile.write(strCDs)
            objFile.close()
    
# -- PRESENTATION (Input/Output) -- #
class IO:
    # TO done add docstring
    """Handling Input / Output
    
    The following functions take input from the user and displays corresponding output. 
    
    """
    # TO done add code to show menu to user copy this from Assignment06 
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
        
        
    # TO done add code to captures user's choice
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    # TO done add code to display the current data on screen
    
    @staticmethod 
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of CD Objects): a table with a list of CD objects

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
    # TO done add code to get CD data from user
    
    @staticmethod    
    def input_cd():
        """Function to ask the user for CD details to add to memory: CD's ID, CD title, Artist
        
        Args:
            None. 
        
        Returns: 
            strID = input('Enter ID: ').strip() # asks the user for their desired ID to assign to the CD
            strTitle = input('What is the CD\'s title? ').strip() # asks the user to input the CDs title
            stArtist = input('What is the Artist\'s name? ').strip() #asks the user to input the Artist of the CD
            return [strID, strTitle, stArtist] #returns the result of the three inputs as a list. this is important for the add_cd(): function to get a list result to process. 
        
        """
        strInput = ''
        while True:
            strInput = input('Enter CD numerical ID: ').strip()
            try:
                strID = int(strInput)
                strTitle = input('What is the CD\'s title? ').strip()
                stArtist = input('What is the Artist\'s name? ').strip()
                return [strID, strTitle, stArtist] 
            except:
                print('Please input a number to proceed.')
    pass

# -- Main Body of Script -- #
# TO done Add Code to the main body. 

# Load data from file into a list of CD objects on script start
try: 
    FileIO.read_file(strFileName, lstOfCDObjects)

# Start main loop
finally: #using finally clause to push through with the main menu even if there is no file yet to read from. 
    while True:
        # Display Menu to user and get choice
        IO.print_menu()
        strChoice = IO.menu_choice()
        
        if strChoice == 'x':
            break
        # show user current inventory
        elif strChoice == 'i':
            try:
                IO.show_inventory(lstOfCDObjects)
                continue  # start loop back at top.
            except: 
                print('Could not load inventory. specify a table () for the funcion IO.show_inventory.\nCheck your code.')
        # TO done let user add data to the inventory
        elif strChoice == 'a':
            CD.add_cd() #This asks user for CD info then converts input to CD object to be added to the list lstOfCDObjects
            continue  # start loop back at top.
        # TO done let user save inventory to file
        elif strChoice == 's':
            # 3.6.1 Display current inventory and ask user for confirmation to save
            try:
                IO.show_inventory(lstOfCDObjects)
            except: 
                print('Could not load inventory. specify a table () for the funcion IO.show_inventory.\nCheck your code.')
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # 3.6.2 Process choice
            if strYesNo == 'y':
                # 3.6.2.1 save data
                # TO Done move processing code into function
                FileIO.write_file(strFileName, lstOfCDObjects) #Added this new function to process the saving of memory to strFileName
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            continue  # start loop back at top.
        # TO done let user load inventory from file
        elif strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                FileIO.read_file(strFileName, lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
        else:
            print('General Error')
