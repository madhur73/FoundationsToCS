import java.util.*;
import java.util.ArrayList;

public class ThreeSum {
    List<List<Integer>> solution =new ArrayList<>();

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> solution = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2 ; i++) {

            twoSum(nums,-1 *nums[i], i+1);

        }

        return this.solution;

    }
    public List<List<String>> groupAnagrams(String[] strs) {
        char [] charArray = new char[26];
        int val = 'a';
        Map<String,String> myMap = new HashMap<String,String>();

        for(String s:strs){
            char [] temp =s.toCharArray();
            int [] key = new int[26];
            for (int i=0;i<26;i++){
                key[i] = 0;
            }
            for (char c : temp){

                int asciiVal = (c) - val;
                key[asciiVal] +=1;
            }
            String myKey = key.toString();
            myMap.put(myKey,s);
        }


    }

    public void twoSum(int [] nums,int targetSum,int left){


        int right = nums.length -1;
        int tempSum =0;
        List<Integer> result = new ArrayList<Integer>();


        while(left < right){
            while(left< right && nums[left] == nums[left+1])
                left++;
            while(left < right && nums[right] == nums[right -1])
                right --;
            if(left < right) {
                tempSum = nums[left] + nums[right];
                if (tempSum < targetSum) {
                    left++;
                } else if (tempSum > targetSum) {
                    right--;
                } else {
                    result.add(nums[left]);
                    result.add(nums[right]);
                    result.add(-1* targetSum);
                    if (!result.isEmpty())
                        this.solution.add(result);
                        result.clear();
                    left++;
                    right--;

                }
            }
            else{
                return;
            }
        }


    }
}
