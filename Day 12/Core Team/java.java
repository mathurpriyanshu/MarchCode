import java.util.Scanner;

public class DayTwelve {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter lower range: ");
		int lowerRange = sc.nextInt();
		System.out.println("Enter uper range: ");
		int upperRange = sc.nextInt();
		
		int flag = 0;
		
		for(int i = lowerRange; i<= upperRange; i++) {
			if(i == 1 || i == 0 ) {
				continue;
			}
			flag = 1;
			
			for(int j = 2; j <= i/2; j++) {
				if(i%j == 0) {
					flag = 0;
					break;
				}
			}
			
			if(flag == 1) {
				System.out.println(i);
			}
		}	
		sc.close();
	}
}