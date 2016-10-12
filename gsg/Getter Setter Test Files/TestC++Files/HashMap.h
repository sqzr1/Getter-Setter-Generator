/*
  
     My own Hash Map implementation:
     The example situation is a Hash Map of words & their frequency occurance

     Header file
     
*/


#include <string>

using namespace std;



struct MapElement
{
             
      MapElement( string key, int data );  // Constructor
      void AddNewElement( string key );
      string wordKey;   // Element key
      int value;        // Element data
      
};


class HashMap
{
      
    public:
           
         HashMap();
         ~HashMap();
         void AddMapElement( string newKey );
         void EraseMapElement( string searchKey );
         int GetIndex( string searchKey );
           
    private:
         
        MapElement table[20];   // Linked list of Map Elements
        MapElement *listPtr;
        unsigned int tableSize;
        
};
