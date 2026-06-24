# PATTERN
def print_python_stars():
    patterns = {
        'P': ["*****","*   *","*   *","*****","*    ","*    ","*    "],
        'Y': ["*   *","*   *"," * * ","  *  ","  *  ","  *  ","  *  "],
        'T': ["*****","  *  ","  *  ","  *  ","  *  ","  *  ","  *  "],
        'H': ["*   *","*   *","*   *","*****","*   *","*   *","*   *"],
        'O': [" *** ","*   *","*   *","*   *","*   *","*   *"," *** "],
        'N': ["*   *","**  *","* * *","*  **","*   *","*   *","*   *"]
    }
    
    word = "PYTHON"
    
   
    for row in range(7):
        line = ""
    
        for letter in word:
            
            line += patterns[letter][row] + "  "
        print(line)

# Run the function
print_python_stars()

def select_level():
    print("\nAvailable level:")
    print("1.EASY")
    print("2. MEDIUM")
    print("3. HARD")
choice = input("\nSelect level (1-3):")
print(choice)
if choice== '1':


    with open("C:\\Users\\Jayanthsenthil\\OneDrive\\Desktop\\1.EASY.txt","r") as a:
        print(a.read())
    a.close()
        
elif choice == '2':
    print("INTERMEDIATE")
    with open("C:\\Users\\Jayanthsenthil\\OneDrive\\Desktop\\2.INTERMEDIATE.txt","r") as b:
        print(b.read())
        b.close()
        
elif choice == '3':
    print("HARD")
    with open("C:\\Users\\Jayanthsenthil\\OneDrive\\Desktop\\3.HARD.txt","r") as c:
        print(c.read())
        c.close()
else:
    print("invalid choice")
    

def summary():
    print("\summary:")
    print("1.EASY")
    print("2. MEDIUM")
    print("3. HARD")
choice = input("\nSelect summary (1-3):")
print(choice)



if choice== '1':
    with open("C:\\Users\\Jayanthsenthil\\OneDrive\\Desktop\\1.EASY(SUMMARY).txt","r") as d:
        print(d.read())
        close()

        
elif choice == '2':
        with open("C:\\Users\\Jayanthsenthil\\OneDrive\\Desktop\\2.INTERMEDIATE(SUMMARY).txt","r")as e: 
            print(e.read())
            close()


            
elif choice == '3':
            with open("C:\\Users\\Jayanthsenthil\\OneDrive\\Desktop\\3.HARD(SUMMARY).txt","r")as f:
                print(f.read())
                close()
            
            
            


            












            

        
        

    
    



    


 

 































    





























