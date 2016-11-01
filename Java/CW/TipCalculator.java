import java.util.HashMap;

public class TipCalculator {

   static HashMap<String, Integer> ratings = new HashMap<>();

   public static Integer calculateTip(double amount, String rating) {
      // Creating a hashmap for ratings
      ratings.put("terrible", 0);
      ratings.put("poor", 5);
      ratings.put("good", 10);
      ratings.put("great", 15);
      ratings.put("excellent", 20);

      rating = rating.toLowerCase();

      // Checking for valid rating
      if (ratings.containsKey(rating)) {
      	int tip = (int) Math.ceil((ratings.get(rating) * amount) / 100);
      	// int tip = Math.round((ratings.get(rating) * amount) / 100);
      	return tip;
      } else {
      	return null;
      }
     
   }

   public static void main(String[] arguments) {
   	  System.out.println("Hello World.");
   	  System.out.println("Amount: 15$, Rate: Good = " + calculateTip(15.0, "Good"));
   	  System.out.println("Amount: 20$, Rate: Terrible = " + calculateTip(20.0, "TERRIBLE"));
   	  System.out.println("Amount: 100$, Rate: Excellent = " + calculateTip(100.0, "Excellent"));
   	  System.out.println("Amount: 107.65$, Rate: GReat = " + calculateTip(107.65, "GReat"));
   }
}
