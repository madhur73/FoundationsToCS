import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Stack;

public class ListPalindrome {
    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public boolean isPalindrome(ListNode head) {

        if(head == null || head.next==null){
            return true;
        }
        ListNode slow,fast;
        slow = fast = head;
        Stack s = new Stack<Integer>();

        while(fast!= null || fast.next!=null){
            s.push(slow.val);
            slow = slow.next;
            fast = fast.next.next;
        }
        if(fast.next == null){
            slow = slow.next;
        }

        while(slow!=null){
            if((Integer)slow.val != s.pop()){
                return false;
            }
            slow =slow.next;
        }
        return true;

    }
}





