public class URLify {
    private int count_spaces(char [] arr,int trueLen){
        int space_count = 0;
        for (int i = 0; i < trueLen; i++) {
            if(arr[i] == ' '){
                space_count++;
            }
        }

        return space_count;
    }

   public String urlConverter(String input, int trueLen){
        char tokens [] = {'%','2','0'};
        char [] inputChars = input.toCharArray();
        int left, right;

        left = trueLen - 1;
        int offset = count_spaces(inputChars,trueLen);
        offset = offset*tokens.length;
        right = left + offset;

        while(left >= 0){
            while(inputChars[left] != ' ' && left >= 0){
                inputChars[right] = inputChars[left];
                inputChars[left] = ' ';
                left --;
                right--;

            }
            //change to for loop
            if(inputChars[left] == ' '  && inputChars[left]!= '#'){
                inputChars[right--] = tokens[2];
                inputChars[right--] = tokens[1];
                inputChars[right--] = tokens[0];
            }



        }

        return inputChars.toString();



   }
}
