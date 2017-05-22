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
      long n = in.nextLong();
						long a = 1;
						long b = 2;
						long sum = 0;
						while (b <= n) {
							if (b % 2 == 0){
								sum += b;
							}
							long b0 = b;
							b += a;
							a = b0;
						}
						System.out.println(sum);

    }
  }
}

