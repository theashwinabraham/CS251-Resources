package Q2;
import java.util.Scanner;

public class Main {

    /*
     * NOTE: Create helper functions here if required
     */
    private static int rec_func(int arr[], int n)
    {
        if(n < 0) return 0;
        if(n == 0)
        {
            return arr[0]*arr[0];
        }
        return arr[n]*arr[n] + rec_func(arr, n-1);
    }

    private static void get_arr(int[] the_arr, int i, int n, Scanner s)
    {
        if(n <= 0) return;
        the_arr[i] = s.nextInt();
        if(i+1 < n) get_arr(the_arr, i+1, n, s);
    }

    private static void run_test_cases(int t, Scanner s)
    {
        if(t <= 0) return;
        int n = s.nextInt();
        if(n < 0) return;
        int [] the_arr = new int[n];
        get_arr(the_arr, 0, n, s);
        System.out.println(rec_func(the_arr, n-1));
        run_test_cases(t - 1, s);
    }
    
    public static void main(String args[]) {
        /*
         * TODO: Complete this method
         * NOTE: Take input from STDIN and print the output to STDOUT
         */
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        run_test_cases(t, s);
        s.close();
    }
}
