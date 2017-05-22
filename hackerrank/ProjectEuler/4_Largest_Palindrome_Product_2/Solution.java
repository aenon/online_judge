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
						int prod = 0, largest_pal = 0;
						for (int i = 100; i < 1000; i++){
							for (int j = 100; j < 1000; j++){
								prod = i * j;
								if (prod > n){break;}
								int num = prod;
								int mun = 0;
								while (num != 0) {
									mun *= 10;
									mun += num % 10;
									num /= 10;
								}
								if (prod == mun && prod > largest_pal) {
									largest_pal = prod;
								}
							}
						}

						System.out.println(largest_pal);
    }
  }
}

