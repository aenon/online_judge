/* 28 implement strstr
 * O(nm) time, O(1) space - Brute force
 */

public class Solution {
  public int strStr(String haystack, String needle) {
    for (int i = 0; ; i++ ) {
      for (int j = 0; ; j++ ) {
        if (j == needle.length()) return i;
        if (i + j == haystack.length()) return -1;
        if (needle.charAt(j) != haystack.charAt(i + j)) break;
      }
    }
  }
}
