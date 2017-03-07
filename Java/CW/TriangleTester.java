class TriangleTester {
	public static boolean isTriangle(int a, int b, int c) {
		// Possible pairs
		int ab = a + b;
		int ac = a + c;
		int bc = b + c;

		// Sum of two lengths > length #3
		if ((ab > c) && (ac > b) && (bc > a))  {
			return true;
		}
		return false;
		}

	public static void main(String[] arugments) {
		System.out.println("a = 1, b = 2, c = 2: " + isTriangle(1, 2, 2));
		System.out.println("a = 7, b = 2, c = 2: " + isTriangle(7, 2, 2));

		System.out.println("");
		System.out.println("Changing Sides");
		System.out.println("a = 1, b = 2, c = 3: " + isTriangle(1, 2, 3));
		System.out.println("a = 1, b = 3, c = 2: " + isTriangle(1, 3, 2));
		System.out.println("a = 3, b = 1, c = 2: " + isTriangle(3, 1, 2));
		System.out.println("a = 1, b = 2, c = 5: " + isTriangle(1, 2, 5));
		System.out.println("a = 1, b = 5, c = 2: " + isTriangle(1, 5, 2));
		System.out.println("a = 5, b = 1, c = 2: " + isTriangle(5, 1, 2));

		System.out.println("");
		System.out.println("Zero values");
		System.out.println("a = 0, b = 2, c = 2: " + isTriangle(0, 2, 2));
		System.out.println("a = 1, b = 0, c = 2: " + isTriangle(1, 0, 2));
		System.out.println("a = 1, b = 2, c = 0: " + isTriangle(1, 2, 0));
	}
}
