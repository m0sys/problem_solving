import java.util.Arrays;
public class LargestDifference {
    public static int largestDifference(int[] data) {
    	// Variables
    	int index1 = -1 ;
    	int index2 = 0;
    	int tempIndexDifference;
    	int indexDifference = 0;
    	int[] data2 = Arrays.copyOfRange(data, 1, data.length);

    	// Going through pair ints
        for (int num1 : data) {
        	index1 ++;
        	for (int num2 : data2) {
        		index2 ++;
        		if (num1 <= num2) {
        			tempIndexDifference = index2 - index1;

        			if (tempIndexDifference > indexDifference) {
        				indexDifference = tempIndexDifference;
        			}

        		}

        	}
        	// Reset
        	index2 = 0;
        }
        return indexDifference;
    }

    public static void main(String[] arguments) {
    	System.out.println("Hello");
    	int[] test1 = {1, 2, 3};
    	System.out.println("Test 1: " + largestDifference(test1));
    	System.out.println("\n\n");

    	System.out.println("Starting test #2");
    	int[] test2 = {9,4,1,10,3,4,0,-1,-2};
    	System.out.println("Test 2: " + largestDifference(test2));
    	System.out.println("\n\n");

    	System.out.println("Starting test #3");
    	int[] test3 = {3,2,1};
    	System.out.println("Test 3: " + largestDifference(test3));
    }
}
