interface Animal {
    void sound();           // abstract method
    void eat();             // abstract method
}
class Dog implements Animal {
    public void sound() {
        System.out.println("Barks");
    }

    public void eat() {
        System.out.println("Eats bones");
    }
}
public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.sound();  // Output: Barks
        d.eat();    // Output: Eats bones

        // Interface reference
        Animal a = new Dog();
        a.sound();  // Barks
        a.eat();    // Eats bones
    }
}
