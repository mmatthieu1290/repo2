class Math:
    
    def square_root(self,x):
        
        
        try:
         if x<0:
             raise ValueError("The input must be a nonnegative number")
        except:
            print("The input must be a nonnegative number")
        else: 
         return x**(1/2)
     
    def mean(self,x):
        
        for element in x:
            if (isinstance(element,float) or isinstance(element,int))==False:
                x.remove(element)
        S=sum(x)
        l=len(x)
        return S/l
    
    def is_even(self,x):
        
       if x == int(x):
        if x%2==0:
            print('The integer {} is even'.format(x))
        else:
            print('The integer {} is odd'.format(x))
       else:
           print('The input must be an integer')
     
    def sum(self,l):
        
        S = 0
        
        for x in l:
            S += x
            
        return S 
    
    
class Inputer():


    def average(self,l):
        
        l_numbers = [elt for elt in l if isinstance(elt,float) or isinstance(elt,int)]
        le = len(l_numbers)
        avg = sum(l_numbers)/le
                
        return [elt if isinstance(elt,float) or isinstance(elt,int) else avg for elt in l] 
    
# Here is a list : [None, 2, 3, 12, 5, 6, None]
# Here is the list with the empty values replaced by the median : [5, 2, 3, 12, 5, 6, 5]    

    def median(self,l):
        
        l_numbers = [elt for elt in l if isinstance(elt,float) or isinstance(elt,int)]
        le = len(l_numbers)
        l_numbers.sort()

        if le%2 ==1:
            me = l_numbers[(le-1)//2]
        else:
            me = (l_numbers[le//2]+l_numbers[le//2-1])/2
               
        return [elt if (isinstance(elt,float) or isinstance(elt,int)) else me for elt in l]

        
def max_list(l):
    
    l_numbers = [elt  for elt in l if isistance(elt,float) or isinstance(elt,int)]

    return max(l_numbers)

def min_list(l):

    l_numbers = [elt for elt in l if isistance(elt,float) or isinstance(elt,int)]

    return min(l_numbers)
            
            
            
        
        
    