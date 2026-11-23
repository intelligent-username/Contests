// https://leetcode.com/problems/merge-sorted-array/submissions/1347216368/?envType=study-plan-v2&envId=top-interview-150
// Merge Sorted Array
// Complete

public class _1Merge_Sorted {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // m for [filled] in nums1
        // n for nums2
        
        int p1 = m - 1;
        int p2 = n - 1;
        int p3 = m + n - 1;

        while (p2 >= 0) {
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[p3] = nums1[p1];
                p1--;
            } else {
                nums1[p3] = nums2[p2];
                p2--;
            }
            p3--;
        }
    }
}
