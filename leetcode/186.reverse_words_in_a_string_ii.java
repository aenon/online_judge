/* 186 Reverse Words in a String II
 * O (n) time, O (1) space
 */

public class Solution {
  public void reverseWords(char[] s) {
    if (s.length > 1) {
      reverse(s, 0, s.length); // reverse the whole string
      for (int i = 0, j = 0; j <= s.length; j++) {
        if (j == s.length || s[j] == ' ') {
          reverse(s, i, j); // reverse the first word 
          i = j + 1;
        }
      }
    }
  }

  private void reverse(char[] s, int begin, int end) {
    for (int i = 0; i < (end - begin) / 2; i++) {
      char temp = s[begin + i];
      s[begin + i] = s[end - i - 1];
      s[end - i - 1] = temp;
    }
  }
}
