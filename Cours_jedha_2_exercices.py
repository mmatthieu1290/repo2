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
        

        S = 0
        le = 0
        for element in l:
            if isinstance(element,float) or isinstance(element,int):
                S += float(element)
                le += 1
        avg = S/le
        
        for i in range(len(l)):
            if (isinstance(l[i],float) or isinstance(l[i],int))==False:
                l[i] = avg
                
        return l  
    
# Here is a list : [None, 2, 3, 12, 5, 6, None]
# Here is the list with the empty values replaced by the median : [5, 2, 3, 12, 5, 6, 5]    

    def maximum(self,l):
        
        l_numbers = []
        for element in l:
            if isinstance(element,float) or isinstance(element,int):
               l_numbers.append(element)
        m = min(l_numbers)       
        M = max(l_numbers)     
        k = 0  
        for i in range(len(l)):
            if (isinstance(l[i],float) or isinstance(l[i],int))==False:
                if k%2==0:
                 l[i] = M
                else:
                 l[i] = m
                k += 1 
                
        return l 

        
def max_list(l):
    
    for elt in l:
        try:
            if (isinstance(elt,int) or isinstance(elt,float))and(elt>M):
                M = elt 
        except:
            M = elt
    return M        
            
            
            
        
        
    