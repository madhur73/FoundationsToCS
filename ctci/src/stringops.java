public class stringops {
    public static void main(String[] args){
        /*
        String s [] = {"Buck", "funck","futhehck","fucieurieur","Bontauck"};
        for(String word : s){
            if( word.endsWith("ck")){
                System.out.println(word);
            }
        }
        */

        String s=" nuckymadhurBuckmadhur";
        System.out.println(s.replace("mad","MADH"));
        String w = "          Mad   ";
        String a = "hur Biyani";

        System.out.println(w.concat(a));
        System.out.println(w.trim());




    }
}
