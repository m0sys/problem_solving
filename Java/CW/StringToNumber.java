public class StringToNumber {
	public static int stringToNumber(String str) {
		//TODO: Convert str into a number
		int number = Integer.parseInt(str);
		return number;
	}

	public static void main(String[] arguments) {
		System.out.println("My String: 1234 => " + stringToNumber("1234"));
	}
}
