import java.util.*;

public class linkedList {
    public static void  main(String argsp[]){
        String  p[ ] = {"Harry","Potter","Goblet","of","fire"};
        List<String> list1 = new LinkedList<>();

        LinkedList<String> ll = new LinkedList<String>(Arrays.asList(p));
        ll.addFirst("Hello");
        ll.addFirst("Madhur");

        p = ll.toArray(new String[ll.size()]);

        for (String x :
                p) {
            list1.add(x);

        }

        String s [] = {"is", "the", "Best"};
        List<String> list2 = new LinkedList<>();

        for (String x :
                s) {
            list2.add(x);

        }

        list1.addAll(list2);
        list2 = null;

        printMe(list1);
        removeSubList(list1,2, 5);
        printMe(list1);
        reverseMe(list1);
        printMe(list1);

    }
    private static void printMe(Collection<String> l){
        Iterator<String> it = l.iterator();

        while(it.hasNext()){
            System.out.print(it.next()+" ");
        }
        System.out.println();

    }

    private static void removeSubList(List<String> l, int from, int to){

        l.subList(from, to).clear();
    }

    private static  void reverseMe(List<String> l){
        ListIterator<String> it = l.listIterator(l.size());
        while (it.hasPrevious()){
            System.out.print(it.previous()+" ");
        }


    }
}
