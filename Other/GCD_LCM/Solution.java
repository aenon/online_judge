import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

	public static void main(String[] args){
		int a, b, x, y, t, gcd, lcm;
		System.out.println("Enter two integers:");
		Scanner in = new Scanner(System.in);
		x = in.nextInt();
		y = in.nextInt();

		a = x;
		b = y;

		while (b != 0) {
			t = b;
	    b = a % b;
			a = t;
		}

	  gcd = a;
	  lcm = (x*y)/gcd;

	  System.out.format("Greatest common divisor of %d and %d = %d\n", x, y, gcd);
	  System.out.format("Least common multiple of %d and %d = %d\n", x, y, lcm);
	}
}
