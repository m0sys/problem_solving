class Solution {
	static int stray(int[] numbers) {
		// Variables
		int index = 1;

		// Iterating through each element and comparing it to the next element
		for (int element : numbers) {
			if (numbers[index] != element) {
				return element;
			}
		}
		return 0; // none
	}

	public static void main(String[] arguments) {
		System.out.println("Hello world!");
		int[] numbers = {1, 1, 2};
		int[] numbers2 = {1, 1, 1};
		int[] numbers3 = {1, 2, 3};
		System.out.println("Array = [1, 1, 2]: " + stray(numbers));
		System.out.println("Array = [1, 1, 1]: " + stray(numbers2));
		System.out.println("Array = [1, 2, 3]: " + stray(numbers3));
	}
}
