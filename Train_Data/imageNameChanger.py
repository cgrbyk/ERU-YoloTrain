import os 
  
# Function to rename multiple files 
def main(): 
    i = 409
      
    for filename in os.listdir("Videoimages"): 
        dst ="images\\" +'{:06}.png'.format(i)
        src ="Videoimages\\"+filename  
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 