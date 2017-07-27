/* 159. Longest Substring At Most Two 
 * O(n) time, O(1)
 */

public class Solution {
  public int lengthOfLongestSubstringTwoDistinct(String s) {
    int i = 0, j = -1, maxLen = 0;
    // i: start of the substring with at most two distinct characters
    // k: next char index
    // j: k - 1
    for (int k = 1; k < s.length(); k++) {
      if (s.charAt(k) == s.charAt(k - 1)) continue; // k is not new char
      if (j >= 0 && s.charAt(j) != s.charAt(k)) { // k is new char
        maxLen = Math.max(k - i, maxLen);
        i = j + 1;
      }
      j = k - 1;
    }
    return Math.max(s.length() - i, maxLen);
  }
}