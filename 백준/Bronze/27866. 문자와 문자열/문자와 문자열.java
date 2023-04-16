import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String args[]) throws Exception {
        String s = br.readLine();
        int n = Integer.valueOf(br.readLine());
        
        System.out.println(s.charAt(n-1));
    }
}