import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class sorting {
    public static void main(String args[]){

        Character c [] = {'m','a','d'};
        List<Character> list = Arrays.asList(c);
        System.out.print("original list :");
        output(list);

        Collections.reverse(list);
        System.out.print("reverse list :");
        output(list);

        Character newRay [] = new Character[3];
        List<Character> copyList = Arrays.asList(newRay);
        Collections.copy(copyList, list);
        System.out.print("copy list :");
        output(copyList);


        Collections.fill(list,'X');
        System.out.print("fiil method");
        output(list);
    }

    private static void output(List<Character> l){
        for (Character x : l){
            System.out.print(x+" ");
        }
        System.out.println();
    }
}
