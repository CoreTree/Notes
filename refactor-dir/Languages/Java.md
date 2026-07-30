# Java
## The Basics
Casting, Conversions, and prints
```java
public class Main {
    public static void main(String[] args) {
        int capA = 65;
        int toH = (int)('H') - (int)('A'); //7
        char h = (char)(capA + toH);
        String hello = h + "ello World";
        System.out.println(hello + "!");
    }
}
```

## Arrays
```java
import java.util.Random;

public class ArrayTest {
    public static void main(String[] args) {
        int[] intArr = new int[6];
        IntStream is = Random.ints(0, 30);
        for(int i = 0; i < intArr.length; i++) {
            intArr[i] = is.nextInt();
            System.out.println(i + ": " + intArr[i]);
        }
    }
}
```
