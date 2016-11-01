public class Kata
{
	public static int dontGiveMeFive(int start, int end)
	{
		// Variables
		int count = 0;

		for (int i = start; i < (end + 1); i++) {
			if (Integer.toString(i).contains("5") == false) {
				count += 1;
			}
		}
		return count;
	}

	public static void main(String[] arguments) {
		System.out.println("Start: 1, End: 9 = " + dontGiveMeFive(1, 9));
		System.out.println("Start: 4, End: 17 = " + dontGiveMeFive(4, 17));
		System.out.println("Start: 20, End: 25 = " + dontGiveMeFive(20, 25));
	}
}
