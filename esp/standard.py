"""The standard namespace where most numerical routines and models should accessible from"""

import copy

class Vector:
    """A simple, generic vector class that should work with any type that has addition, subtraction and multiplication
    defined."""
    def __init__( self, values, length=None ):
        """Constructor function. Builds up the vector from the list given in values. If length is not None, then values
        will be treated as a single element and the vector will consist of values repeated length number of times"""

        self.elements = [] #the elements are stored in a list, even if it is just one element.
        self.row = True #vectors are assumed to be row vectors unless otherwised set

        if length is None: #this is the default behavior
            self.elements = list( values ) #Ensuring the elements are a list in case a tuple or similar is passed.

        else: #if length is not None, then create a vector of 'length' identical elements, each set to 'value'
            for elem in range(length):
                self.elements.append( values ) #we simply repeatedly append 'values` to our elements list.
    
        self.length = len(self.elements) #save the length of the vector so we can compare to safely add and multiply

    def __len__(self):
        """Returns the length of the vector that we stored at creation. Overloads the len() function in Python"""
        return( self.length )

    def __getitem__( self, key ):
        """Defines the element indexing in the vector allowing the elements to be accessed with value = self[key]"""
        return( self.elements[key] )

    def __setitem__( self, key, value ):
        """Defines the element indexing in the vector allowing the elements to be set with self[key] = value"""
        self.elements[key] = value


    def __add__(self, other):
        """Overloading the '+' operator so that we can add two vectors together. We can only add two vectors of same
        length. We will add a row vector to a column vector (and output a row vector)."""

        if ( len(self) != len(other) ): #check to ensure the two vectors are the same length
            raise ArithmeticError( "Vector lengths do not match") 

        sumVector = Vector(0, len(self) ) #create the sum vector

        for index in range( len(self) ):
           sumVector[index] = self[index]+other[index]

        return( sumVector )

    def __add__(self, other):
        """Overloading the '-' operator so that we can subtract vectors. We can only subtract two vectors of same
        length. We will add a row vector to a column vector (and output a row vector)."""

        if ( len(self) != len(other) ): #check to ensure the two vectors are the same length
            raise ArithmeticError( "Vector lengths do not match") 

        diffVector = Vector(0, len(self) ) #create the sum vector

        for index in range( len(self) ):
           diffVector[index] = self[index]-other[index]

        return( diffVector )

    def __mult__(self, other ):
        """Overloading the '*' operator so we can multiply two vectors together piecewise. If other is a scalar, 
          we will scale self by it."""

        productVector = Vector(0, len(self) ) #create the sum vector

        try: #attempt to test other's length
            other_length = len(other) #if other has no len() method, it is a scalar and we will attempt to scale by it
        except TypeError: #execute the following if there is a type error
            for index in range( len(self) ): #for each element in the vector 'self' scale it by 'other'
                productVector[index] = self[index]*other
            return( productVector ) #return the result from here so we do not compare lengths (other doesn'thave a length)       

        if ( len(self) != len(other) ): #check to ensure the two vectors are the same length
            raise ArithmeticError( "Vector lengths do not match") 

        #if the two vectors are the same length, piecewise multiply them
        for index in range( len(self) ):
           productVector[index] = self[index]*other[index]

        #return the result
        return( productVector )

    def __radd__( self, other ): #the reflection of __add__(). (other+self rather than self+other)
        return( Vector.add(other, self ) ) #we call add as a function rather than a method and switch the inputs

    def __rmult__( self, other ):
        return( Vector.mult(other, self ) )

    def __rsub__( self, other ):
        return( Vector.sub( other, self ) )

    def norm( self, p=2 ):
        """Returns the p-norm of the vector. Defaults to the Euler norm if no p is given. Not implemented yet."""
        return( NotImplemented )

    def __repr__( self ):
        """Represents a vector class as a string"""
        elem_string = "Vector( ["+str(self[0])
        for index in range(1,self.length):
            elem_string=elem_string+","+str( self[index] )

        elem_string=elem_string + "] )"
        return( elem_string )
