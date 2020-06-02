import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {


//       isUnique myObj = new isUnique();
//       if(myObj.checkUnique("ABCDEFf")){
//           System.out.println("Unique charcters");
//       }
//
//       else{
//           System.out.println("NOT Unique charcters");
//       }

//       URLify urlObj = new URLify();
//       String s = "Mr John Smith        ";
//       s = urlObj.urlConverter(s,13);
//       System.out.println(s);

        ThreeSum obj = new ThreeSum();
        int [] input = { -1, 0, 1, 2, -1, -4};
        List<List<Integer>> result = obj.threeSum(input);

        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));

        }

    }


}
