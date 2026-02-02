//import java.util.*;
//
//class temp {
//    static int timesAccessed = 0;
//
//    String name;
//
//    temp(){
//        timesAccessed ++ ;    // cant do it without this constructor
//    }
//
//}
//
//public class Public_Static{
//    public static void main(String[] args){
//        Scanner sc = new Scanner(System.in);
//
//        temp obj1 = new temp();
//        String x = sc.next();
//        obj1.name = x;
//
//        temp obj2 = new temp();
//        String y = sc.next();
//        obj2.name = y;
//
//        System.out.println(obj1.name);
//        System.out.println(temp.timesAccessed);  // increases for each time we call 'temp' class
//
//
//    }}
//
//// public are accessed using objects
//// static can be accessed using classname
//
//// public of a class can be accessed in other packages(files)
//// static of a class only exists within that class
//
////public static means it belongs to the class and can be accessed from anywhere
////void means JVM expects nothing to be returned after 'main' ends
////main is starting point of program, JVM looks for this
////when we run program the CLI gives some strings that are passed to an array named 'args'