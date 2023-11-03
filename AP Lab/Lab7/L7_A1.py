def reverseLines(filename):
    try: 
        with open(filename,'r',encoding='utf-8') as f:
            flines = f.readlines()
            for line in reversed(flines):
                print(line.strip())
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occured: {str(e)}"  
    
filename = input("Enter the name of the file: ")
reverseLines(filename)
