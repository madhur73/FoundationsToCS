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

        RotateMatrix myObj = new RotateMatrix();
        int[][] arr = {
                        {1, 2, 3},
                        {4, 5, 6},
                        {7, 8, 9}
                };
        //myObj.printMat(arr);
        arr = myObj.startRotation(arr);
        myObj.printMat(arr);

                }

}
