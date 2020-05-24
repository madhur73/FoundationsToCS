import com.sun.org.apache.bcel.internal.classfile.Constant;

public class isUnique {

    boolean checkUnique(String s){
        boolean [] charArray = new boolean[26];
        int initialAscii = (int)'a';
        int index= 0;
        String lowerCase = s.toLowerCase();
        char [] myCharArray = lowerCase.toCharArray();

        for (char c:myCharArray
             ) {
            index= getAscii(c,initialAscii);
            if(charArray[index])
                return false;
            charArray[index] = true;
        }

        return true;
    }
    int getAscii(char c,int value){
        return (int)c - value;
    }




}
