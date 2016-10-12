package iterators;
import java.util.*;
import java.io.*;

public class IteratorExample {


	public static void main(String[] pArgs) {

		Set vNames= new TreeSet(); //
		vNames.add("Hello");
		vNames.add("Goodbye");
		vNames.add("Bonjour");
		vNames.add("Adieu");
		vNames.add("Dag");

		System.out.println("Treeset iteration:"+ "\n");
		Iterator<String> vIter= vNames.iterator();
		while(vIter.hasNext()) {
			String vCurrent= vIter.next();
			System.out.println(vCurrent);
		}
		
		Set vNames1= new HashSet(); //
		vNames1.add("Hello");
		vNames1.add("Goodbye");
		vNames1.add("Bonjour");
		vNames1.add("Adieu");
		vNames1.add("Dag");

		System.out.println("Hashset iteration:"+ "\n"); 
		Iterator<String> vIter1= vNames1.iterator();
		while(vIter1.hasNext()) {
			String vCurrent1= vIter1.next();
			System.out.println(vCurrent1);
		}
		

		Set vNames2= new LinkedHashSet(); //
		vNames2.add("Hello");
		vNames2.add("Goodbye");
		vNames2.add("Bonjour");
		vNames2.add("Adieu");
		vNames2.add("Dag");

		System.out.println("LinkedHashset iteration:"+ "\n"); 
		Iterator<String> vIter2= vNames2.iterator();
		while(vIter2.hasNext()) {
			String vCurrent2= vIter2.next();
			System.out.println(vCurrent2);
		}		
	}
}
	