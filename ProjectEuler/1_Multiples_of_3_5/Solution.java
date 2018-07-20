import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {
  Scanner in = new Scanner(System.in);
  long t = in.nextInt();
  for(long a0 = 0; a0 < t; a0++){
    long n = in.nextInt();
    n -= 1;
    long n3 = (3 + n - n % 3) * (n / 3) / 2;
    long n5 = (5 + n - n % 5) * (n / 5) / 2;
    long n15 = (15 + n - n % 15) * (n / 15) / 2;
    System.out.println(n3 + n5 - n15);
  }
  }
}

