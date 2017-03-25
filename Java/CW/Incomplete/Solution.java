import java.lang.Math;
public class Solution {
  public static int zeros(int n) {
      // your beatiful code here
  	String fact = Integer.toString(factorial(n));
  	String[] numbers = fact.split(""); 
  	int numZeros = 0;

  	for (int i = numbers.length - 1; i > 0; i--) {
  		if (Integer.parseInt(numbers[i]) == 0) {
  			numZeros++;
  		} else {
  			break;
  		}
  	}

  	return numZeros;
  }

  public static int factorial(int n) {
  	if (n == 1) { // base case
  		return 1;
  	}
  	return n * factorial(n -1); 
  }

  public static double factorial2(int n) {
  	if (n == 1) {
  		return Math.pow(5, n);
  	}
  	return (n / 5.0) * (factorial(n - 1) / 5.0);
  }

  public static void main(String[] args) {
  	// Testing factorial
  	int fact1 = factorial(12);
  	System.out.println("Factorial of 12: " + fact1);

  	// Test 2
  	int fact2 = factorial(13);
  	System.out.println("Factorial of 13: " + fact2);

  	// Test 3
  	int fact3 = factorial(17);
  	System.out.println("Factorial of 17: " + fact3);

  	// Testing factorial2
  	double fact4 = factorial2(12);
  	System.out.println("Factorial of 12: " + fact4);

  	// Testing zeros
  	int numberOfZeros = zeros(12);
  	System.out.println("Number of trailing zeros in factorial of 12: " + numberOfZeros);

  	// Test 2
  	numberOfZeros = zeros(13);
  	System.out.println("Number of trailing zeros in factorial of 13: " + numberOfZeros);

  	// Test 3
  	numberOfZeros = zeros(17);
  	System.out.println("Number of trailing zeros in factorial of 13: " + numberOfZeros);

  }
}
