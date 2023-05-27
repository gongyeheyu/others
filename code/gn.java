import java.util.Scanner;
class gn {
    public static void main(String args[]) {
        try(Scanner sc = new Scanner(System.in)) {
            System.out.println("it start");
            int inp=sc.nextInt();
            System.out.println("input is "+inp);
            if(inp<10) System.out.println("input < 10");
            if(inp>=10) System.out.println("input >= 10");
            int x;
            for(x=inp; x<1000; x++)
                System.out.println("x is "+x);
        }
    }
}