import java.util.Scanner;
class gn2 {
    public static void main(String args[]) {
        String copyright = "Copyright 2023 GONGYE Heyu";
        System.out.println(copyright);
        try(Scanner sc = new Scanner(System.in)) {
            System.out.println("it start");
            int inp=sc.nextInt();
            System.out.println("input is "+inp);
            long x;
            long y = inp;
            long z;
            for(x=0; x <= inp; x++) {
                System.out.println("x is "+x);
                y = y-1;
                System.out.println("y is "+y);
                z = x*y;
                System.out.println("z is "+z);
            }
            if(inp<10) System.out.println("input < 10");
            if(inp>=10) System.out.println("input >= 10");
        }
    }
}