import java.util.Arrays;
public class Kata3 {
	public static String createPhoneNumber(int[] numbers) {
		// Variables
		String phoneNumber;
		StringBuilder strBuilder = new StringBuilder();
		String tempNumbers;

		// Building string of elements from 'numbers'
		for (int i = 0; i < numbers.length; i++) {
			strBuilder.append(numbers[i]);
		}
		tempNumbers = strBuilder.toString();

		// Creating phone number
		phoneNumber = "(" + tempNumbers.substring(0, 3) + ") "; // city code
		phoneNumber += tempNumbers.substring(3, 6) + "-"; // first part 
		phoneNumber += tempNumbers.substring(6, 10); // second part

		return phoneNumber;
  }

  public static void main(String[] arguments) {
  	int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}; 
  	System.out.println(createPhoneNumber(numbers));

  } 
}
