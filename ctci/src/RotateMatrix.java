public class RotateMatrix {
    //int [][] transpose(int [][])
    // int [] []SwapColumns(int[][])

    public int[][] startRotation(int [][] matrix){
        int n = matrix.length;
        if(n > 1) {
            matrix = transpose(matrix);
            //printMat(matrix);
            matrix = swapColumns(matrix);

            return matrix;
        }
        else{
            return matrix;
        }
    }

    public int[][] transpose(int[][] matrix){
        int n = matrix.length;
        int temp = 0,end =0;
        for (int i = 0; i < n ; i++) {
            for (int j = 0; j <= end; j++) {
                matrix = swap(i,j,matrix);

            }
            end++;

        }
        return matrix;

    }

    public int[][] swapColumns(int [][] matrix){
        int n = matrix.length;
        int start,end,temp;
        start =0;
        end = n-1;
        while(start < end) {
            for (int i = 0; i < n; i++) {
                temp = matrix[i][start];
                matrix[i][start] = matrix[i][end];
                matrix[i][end] = temp;
            }
            start++;
            end--;

        }

        return matrix;
    }

    public int[][] swap(int row,int col,int[][] matrix){
        int temp = 0;
        temp = matrix[row][col];
        matrix[row][col] = matrix[col][row];
        matrix[col][row] = temp;

        return matrix;
    }

    public void printMat(int[][] matrix){
        int n = matrix.length;
        System.out.println("[[");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(Integer.toString(matrix[i][j]) +"\t");
            }
            System.out.println("\n");

        }
        System.out.println("]]");
    }

}
