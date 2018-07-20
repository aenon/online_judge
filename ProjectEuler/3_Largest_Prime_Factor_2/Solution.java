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
						while (n % 2 == 0) {
							n = n / 2;
						}
						long i = 3;
						while (i <= Math.sqrt(n)) {
							while (n % i == 0) {
								n = n / i;
							}
							i += 2;
						}
						long largest_prime_factor = (n > 2) ? n : i - 2;
						System.out.println(largest_prime_factor);
				}
		}
}

