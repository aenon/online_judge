/* 167 Two Sum II 
 * O(n) runtime, O(1) space - Two pointers
 */

public class Solution {
  public int[] twoSum(int[] numbers, int target) {
    int i = 0, j = numbers.length - 1;
    while (i < j) {
      if (numbers[i] + numbers[j] == target) {
        return new int[] {i + 1, j + 1};
      }
      else if (numbers[i] + numbers[j] > target) {
        j--;
      }
      else {
        i++;
      }
    }
    throw new IllegalArgumentException("No two sum solution");
  }
}