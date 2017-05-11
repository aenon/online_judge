import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
				List pals = new ArrayList();
				for (int pal = 101101; pal < 1000000; pal++){

					String strpal = Integer.toString(pal);
					boolean isPal = true;
					for (int a2 = 0; a2 < 3; a2++) {
						if (strpal.charAt(a2) != strpal.charAt(5 - a2)) {
							isPal = false;
						}
					}
					if (!isPal) {continue;}
					//System.out.println(pal);

					for (int i = 100; i < Math.sqrt(pal) + 1; i++){
						if (pal / i > 999) {continue;}
						if (pal % i == 0){
							pals.add(pal);
							//System.out.println(pal);
							//System.out.println(i);
							break;
						}
					}
				}

        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
						int largest_pal = 101101;
						for (int a1 = 0; a1 < pals.size(); a1++) {
							if ((int)pals.get(a1) < n) {
								largest_pal = (int)pals.get(a1);
							}
						}
						System.out.println(largest_pal);
        }
    }
}

