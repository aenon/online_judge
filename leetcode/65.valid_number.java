/* 65. Valid Number
 */

public class Solution {
  public boolean isNumber (String s) {
    boolean has_digit = false;
    boolean has_dot = false;
    boolean is_exponential = false;
    s = s.trim();
    if (s.length() == 0) return false;
    int i = 0, n = s.length();
    if (s.charAt(i) == '+' || s.charAt(i) == '-') {
      i++;
    }
    while (i < n) {
      if (Character.isDigit(s.charAt(i))) {
        has_digit = true;
      }
      else if (s.charAt(i) == '.' && has_dot == false) {
        has_dot = true;
      }
      else if (s.charAt(i) == 'e' && is_exponential == false) {
        is_exponential = true;
        i++;
        if (i < n &&)
      }
      else {
        return false;
      }
      i++;
    }
    if (has_digit == false) return false;
    return true;
  }
}