import java.util.*;
class Transaction{
    private int balance;

    Transaction(int balance){
        this.balance = balance;
    }

    void withdraw(int amount){
        balance -= amount;
    }

    void getter(){
        System.out.println(balance);
    }
}

public class encapsulation{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        Transaction obj = new Transaction(x);


        obj.withdraw(500);
        obj.getter();

    }
}