/* 186 Reverse Words in a String II
 * O (n) time, O (1) space
 */

public class Solution {

  public void reverseWords(char[] s) {
    int j = s.length();
    for (int i = s.length() - 1; i >= 0; i--) {
      if (s.charAt(i) == ' ') {
        j = i;
      }
      else if (i == 0 || s.charAt(i - 1) == ' ') {
        if (reversed.length() > 0) {
          reversed.append(' ');
        }
        reversed.append(s.substring(i, j));
      }
    }
  }
}
