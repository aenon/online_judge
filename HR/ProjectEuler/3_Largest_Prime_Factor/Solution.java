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
						List factors = new ArrayList();
						long largest_prime_factor = 1;
						for(long i = 2; i <= n; i++){
							//System.out.println("Checking " + i);
						// Check for all numbers from 2 up to n
							if (n % i == 0) {
							// If the number i is a factor
							  //System.out.println(i + " is a factor.");
								//if (factors.size() > 0) {
								// If there are factors smaller than i
								  boolean is_prime = true;
									for (int i0 = 0; i0 < factors.size(); i0++) {
									// Check if i is a prime number
									  if (i % (Long)factors.get(i0) == 0) {
											is_prime = false;
										}
									}
									if (is_prime == true) {
										//System.out.println(i + " is a prime factor");
										largest_prime_factor = i;
									}
									factors.add(i);
									//System.out.println("List of factors for " + n + ": " + factors);
								//}
							}
						}
						System.out.println(largest_prime_factor);
				}
		}
}

