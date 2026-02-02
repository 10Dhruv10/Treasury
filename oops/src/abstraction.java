import java.util.*;
abstract class Transaction{
    int salary;
    void withdraw(int amount){};
    void getter(){};

}

class UPI extends Transaction{
    int amount;
    UPI(int salary){
        this.salary = salary;
    }
    void withdraw(int amount){
        salary -= amount;

    }
    void getter(){
        System.out.println(salary);
    }
}

public class abstraction{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        Transaction obj = new UPI(x);
        obj.withdraw(500);
        obj.getter();

    }
}