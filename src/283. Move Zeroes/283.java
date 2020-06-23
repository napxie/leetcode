class Solution {
    public void moveZeroes(int[] nums) {
		if(nums==null) {
			return;
		}
        int i = 0, j = 0;
        for (i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                j ++;
            }
        }
    }
    private static void printArr(int[] arr){
        for(int i = 0 ; i < arr.length ; i ++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]){

        int[] arr = {0, 1, 0, 3, 12};
        (new Solution()).moveZeroes(arr);
        printArr(arr);
    }
}