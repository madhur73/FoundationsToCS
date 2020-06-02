import com.sun.javafx.binding.StringFormatter;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;

public class ArrayList {

    public static  void main(String args[]) {
        String[] things = {"words", "eggs", "laser", "head"};
        List<String> list1 = new java.util.ArrayList<String>();

        for (String x : things) {
            list1.add(x);
        }


        String[] otherthings = { "laser", "head"};
        List<String> list2 = new java.util.ArrayList<String>();

        for (String y : otherthings) {
            list2.add(y);
        }

        for (int i = 0; i < list1.size(); i++) {
            System.out.printf("%s ",list1.get(i));
        }

        removeCommon(list1,list2);
        for (int i = 0; i < list1.size(); i++) {
            System.out.printf("--------%s",list1.get(i));
        }
    }

    public static void removeCommon(Collection<String> l1, Collection<String> l2){
        Iterator<String> it = l1.iterator();
        while (it.hasNext()){
            if(l2.contains(it.next()))
                it.remove();
        }

        }
    }