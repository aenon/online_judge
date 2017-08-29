/* 65. Valid Number
 */

public class Solution {
  public boolean isNumber (String s) {
    boolean is_number = false;
    int i = 0, n = s.length();
    while (i < n && Character.isWhitespace(s.charAt(i))) i++;
    // filter leading whitespaces
    if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) i++;
    // filter sign
    while (i < n && Character.isDigit(s.charAt(i))) {
      i++;
      is_number = true;
    }
    if (i < n && s.charAt(i) == '.') {
      // the decimal point
      i++;
      while (i < n && Character.isDigit(s.charAt(i))) { 
        // every digit following the decimal point
        i++;
        is_number = true;
      }
    }
    if (is_number && i < n && s.charAt(i) == 'e') {
      // the exponential 
      i++;
      is_number = false;
      if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) i++;
      while (i < n && Character.isDigit(s.charAt(i))) {
        i++;
        is_number = true;
      }
    }
    while (i < n && Character.isWhitespace(s.charAt(i))) i++;
    return is_number && i == n;
  }
}