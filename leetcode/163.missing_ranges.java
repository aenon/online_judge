/* 163. Missing Ranges
 * O(n) time, O(1)
 */

public class Solution {
  public List<String> findMissingRanges(int[] vals, int start, int end) {
    List<String> ranges = new ArrayList<>();
    // prev : previous number;
    // curr: current number
    int prev = start - 1; 
    for (int i = 0; i <= vals.length; i++) {
      int curr = (i == vals.length) ? end + 1 : vals[i];
      if (curr - prev >= 2) { // if gap exist
        ranges.add(getRange(prev + 1, curr - 1));
      }
      prev = curr;
    }
    return ranges;
  }

  private String getRange (int from, int to) {
    return (from == to) ? String.valueOf(from) : from + "->" + to;
  }
}