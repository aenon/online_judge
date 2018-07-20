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
					long sum = (n * n * (n + 1) * (n + 1) / 4)  - n * (n + 1) * (2 * n + 1) / 6;
					if (sum < 0) sum = -sum;
					System.out.println(sum);
				}
		}
}

