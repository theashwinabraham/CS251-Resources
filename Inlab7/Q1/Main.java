package Q1 ;

import Q1.Matrix;

public class Main {
    public static void main(String args[]) {
        Matrix m1 = new Matrix(4, 5, 4) ;
        m1.printmatrix() ;
        System.out.println("-----------------------------");

        m1.scalarmul(3) ;
        m1.printmatrix() ;
        System.out.println("-----------------------------");

        Matrix m2 = new Matrix(4, 5, 2) ;
        m2.printmatrix() ;
        System.out.println("-----------------------------");

        m2.setelem(1, 1, 10);
        m2.printmatrix() ;
        System.out.println("-----------------------------");

        Matrix m3 = Matrix.add(m1, m2) ;
        m3.printmatrix() ; 
        System.out.println("-----------------------------");

        Matrix m4 = new Matrix(5, 1, 2) ;
        m4.printmatrix() ;
        System.out.println("-----------------------------");
        
        Matrix m5 = Matrix.matmul(m3, m4) ;
        m5.printmatrix() ;
        System.out.println("-----------------------------");
    }
}

// Expected Output:
// 4 4 4 4 4
// 4 4 4 4 4
// 4 4 4 4 4
// 4 4 4 4 4
// -----------------------------
// 12 12 12 12 12
// 12 12 12 12 12
// 12 12 12 12 12
// 12 12 12 12 12
// -----------------------------
// 2 2 2 2 2
// 2 2 2 2 2
// 2 2 2 2 2
// 2 2 2 2 2
// -----------------------------
// 2 2 2 2 2
// 2 10 2 2 2
// 2 2 2 2 2
// 2 2 2 2 2
// -----------------------------
// 14 14 14 14 14
// 14 22 14 14 14
// 14 14 14 14 14
// 14 14 14 14 14
// -----------------------------
// 2
// 2
// 2
// 2
// 2
// -----------------------------
// 140
// 156
// 140
// 140
// -----------------------------
