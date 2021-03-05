public class Kata {
    public static int findShort(String s) {
        int wordLength = s.split(" ")[0].length();
        for (String word : s.split(" "))
            if (word.length() < wordLength) wordLength = word.length();
        return wordLength;
	//most awesome solution seen:
	//return Arrays.stream(s.split(" ")).mapToInt(String::length).min().getAsInt();
    }
}
