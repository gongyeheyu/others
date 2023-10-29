package test;
public class test{
    public static void main(String[] args) {
        // 获取操作系统和版本信息
         
        System.out.println(System.getProperty("os.name"));
        System.out.println(System.getProperty("os.version"));
        System.out.println(System.getProperty("os.arch"));
        System.out.println(System.getProperty("user.name"));
        System.out.println(System.getProperty("user.home"));
        System.out.println(System.getProperty("user.dir"));
        System.out.println(System.getProperty("java.version"));
        System.out.println(System.getProperty("java.vendor"));
        System.out.println(System.getProperty("java.home"));
        System.out.println(System.getProperty("java.class.path"));
        System.out.println(System.getProperty("java.library.path"));
        System.out.println(System.getProperty("java.io.tmpdir"));
        
    }
}