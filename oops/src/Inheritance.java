class Parent{
    String name;

    Parent(String name){
        this.name = name;
    }
}

class Child extends Parent{
    int age;

    Child(String name, int age){
        super(name);
        this.age = age;

    }

}

public class Inheritance{
    public static void main(String[] args) {
        Child obj = new Child("dhruv", 1);
        System.out.println(obj.name + " " + obj.age);
    }
}