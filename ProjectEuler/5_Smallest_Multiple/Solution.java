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
						System.out.println("The given number is n = " + n);
						int mul = 1;
							for (int i = 1; i <= n; i++) {
								System.out.println("Checking for number i = " + i);
								int j = i;
								for (int k = 1; k < i; k++){
									System.out.println("Check if j = " + j + " is divisible by " + k);
									if (j == 1 || k == 1) {
										System.out.println("Skipping 1.");
										continue;
									}
									if (j % k == 0) {
										j /= k;
										System.out.println("j is now " + j);
									}
								}
								mul *= j;
								System.out.println("mul is now " + mul);
							}
						System.out.println(mul);
    }
  }
}

