import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();
    for(int a0 = 0; a0 < t; a0++){
      int n = in.nextInt();
						BigInteger sum = BigInteger.valueOf(0);
						for (int i = 1; i < n; i++){
							sum = sum.add(BigInteger.valueOf(i * (n + i + 1) * (n - i)));
						}
						System.out.println(sum);
    }
  }
}

