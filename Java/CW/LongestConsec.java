class LongestConsec {
    
    public static String longestConsec(String[] strarr, int k) {
        // Variables 
        int longestLength = 0;
        String longestString = "";
        int index = 0;

        for (String str : strarr) {
        	String tempLongString = ""; // reset
        	
        	if (index + k <= strarr.length) {
        		for (int i = 0; i < k; i++) {

        			// Continue from index
        			int tempI = i + index;
        			tempLongString += strarr[tempI];
        		}
        	}

        	// Check for longest string
        	if (tempLongString.length() > longestLength) {
        		longestLength = tempLongString.length();
        		longestString = tempLongString;
        	}

        	// Check inside array for longest string
        	if (tempLongString.length() < str.length() && longestString.length() < str.length()) {
        		if (k > 0 && strarr.length > k) {
        			longestString = str;
        		}

        	}

        	index ++;
        }

        return longestString;
    }

    public static void main(String[] arguments) {
    	// Test 1
    	// String[] test1 = {"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"};
    	// System.out.println("Longest consecutive string: " + longestConsec(test1, 2));
    	// System.out.println("\n");
    	// Passed!

    	// Test 2
    	// String[] test2 = {"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"};
    	// System.out.println("Longest consecutive string: " + longestConsec(test2, 1));
    	// System.out.println("\n");
    	// System.out.println("HELLO WORLD!!!");
    	// System.exit(0);
    	// assert(false);
    	// Passed!

    	// Test 3 
    	// String[] test3 = {}; 
    	// System.out.println("Longest consecutive string: " + longestConsec(test3, 3));
    	// System.out.println("\n");
    	// System.exit(0);
    	// Passed

    	// Test 4
    	// String[] test4 = {"itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"}; 
    	// System.out.println("Longest consecutive string: " + longestConsec(test4, 2));
    	// System.out.println("\n");
    	// System.exit(0);
    	// Passed

    	// Test 5
    	// String[] test5 = {"wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"};  
    	// System.out.println("Longest consecutive string: " + longestConsec(test5, 2));
    	// System.out.println("\n");
    	// System.exit(0);
    	// Passed

    	// Test 6
    	// String[] test6 = {"zone", "abigail", "theta", "form", "libe", "zas"};   
    	// System.out.println("Longest consecutive string: " + longestConsec(test6, -2));
    	// System.out.println("\n");
    	// System.exit(0);
    	// Passed

    	// Test 7
    	// String[] test7 = {"it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"};
    	// System.out.println("Longest consecutive string: " + longestConsec(test7, 3));
    	// System.out.println("\n");
    	// System.exit(0);
    	// Passed

    	// Test 8
    	// String[] test8 = {"it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"};
    	// System.out.println("Longest consecutive string: " + longestConsec(test8, 15));
    	// System.out.println("\n");
    	// System.exit(0);
    	// Passed

    	// Test 9
    	// String[] test9 = {"it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"};
    	// System.out.println("Longest consecutive string: " + longestConsec(test9, 0));
    	// System.out.println("\n");
    	// System.exit(0);
    	// Passed
    }
}
