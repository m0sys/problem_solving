import java.util.Arrays;
public class Kata2 {

	public static long[] NumbersWithDigitInside(long x, long d) {
		// Variables
		int count = 0;
		long product = 1;
		int sum = 0;
		long[] myArray = new long[3];
		boolean isNum = false;

		for (int i = 1; i <= x; i++) {
			if (Integer.toString(i).contains(Long.toString(d)) == true) {
				isNum = true;
				count += 1;
				sum += i;
				product *= i;
			}
		}

		if (isNum) {
			myArray[0] = count;
			myArray[1] = sum;
			myArray[2] = product;
			return myArray;

		}else {
			return myArray;
		}		

	}

	public static void main(String[] arguments) {
		System.out.println("Hello");
		System.out.println("x = 11, d = 1 => " + Arrays.toString(NumbersWithDigitInside(11L, 1L)));
		System.out.println("x = 20, d = 0 => " + Arrays.toString(NumbersWithDigitInside(20L, 0L)));
		System.out.println("x = 44, d = 4 => " + Arrays.toString(NumbersWithDigitInside(44L, 4L)));

	}
}
