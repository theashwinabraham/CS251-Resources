package Q1;
/* 
 * IMPLEMENTED BY: ASHWIN ABRAHAM
 */
public class Matrix {
    private int n,m ;
    private int mat[][] ;

    Matrix(int n, int m, int v) {
        /* 
         * TODO: Complete this constructor
         * Initialize a matrix of size n x m with all elements equal to v
         */
        this.n = n;
        this.m = m;
        mat = new int [n][m];
        for(int i = 0; i<n; i++){
            for(int j = 0; j<m; j++){
                mat[i][j] = v;
            }
        }

    }

    Matrix(int n, int m) {
        /* 
         * TODO: Complete this constructor 
         * Initialize a matrix of size n x m with all elements equal to 0
         */
        this.n = n;
        this.m = m;
        mat = new int [n][m];
        for(int i = 0; i<n; i++){
            for(int j = 0; j<m; j++){
                mat[i][j] = 0;
            }
        }
    }

    public static Matrix add(Matrix A, Matrix B) {
        /*
         * TODO: Complete this method
         * Add two matrices and return the result
         * and return a zero matrix of size 1 x 1
         */
        if(A.n == B.n && A.m == B.m) {
            Matrix m = new Matrix(A.n, A.m);
            for(int i = 0; i<A.n; i++) {
                for(int j = 0; j<A.m; j++) {
                    m.mat[i][j] = A.mat[i][j] + B.mat[i][j];
                }
            }
            return m;
        }
        else {
            return new Matrix(1, 1);
        }
    
    }

    public static Matrix matmul(Matrix A, Matrix B) {
        /*
         * TODO: Complete this method
         * Multiply two matrices and return the result
         * and return a zero matrix of size 1 x 1
         */
        if(A.m == B.n)
        {
            Matrix m = new Matrix(A.n, B.m);
            for(int i = 0; i<A.n; i++)
            {
                for(int j = 0; j<B.m; j++)
                {
                    m.mat[i][j] = 0;
                    for(int k = 0; k<A.m; k++)
                    {
                        m.mat[i][j] += A.mat[i][k]*B.mat[k][j];
                    }
                }
            }
            return m;
        }
        else {
            return new Matrix(1, 1);
        }
    }

    public void scalarmul(int k) {
        /*
         * TODO: Complete this method
         * Multiply all elements of the matrix by k
         */
        for(int i = 0; i<this.n; i++)
        {
            for(int j = 0; j<this.m; j++)
            {
                this.mat[i][j] = this.mat[i][j]*k;
            }
        }
    }

    int getrows() {
        /*
         * TODO: Complete this method
         * Return the number of rows in the matrix
         */
        return this.n;
    }

    int getcols() {
        /*
         * TODO: Complete this method
         * Return the number of columns in the matrix
         */
        return this.m;
    }

    int getelem(int i,int j) {
        /*
         * TODO: Complete this method
         * Return the element at row i and column j
         * If i or j is out of bounds, return -1
         */
        if(i >= 0 && i<this.n && j >=0 && j<this.m) return this.mat[i][j];
        return -1;
    }

    void setelem(int i,int j, int v) {
        /*
         * TODO: Complete this method
         * Set the element at row i and column j to v
         * If i or j is out of bounds, don't change anything
         */
        if(i >= 0 && i<this.n && j >=0 && j<this.m) this.mat[i][j] = v;
    }

    void printmatrix() {
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(j!=0) System.out.print(" ");
                System.out.print(mat[i][j]);
            }
            System.out.print("\n") ;
        }
    }
}

