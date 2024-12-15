import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int [][]schedule = new int[N][2]; // 회의실의 수에 대한 시작시간과 끝나는 시간
		for(int i=0; i<N; i++){
			schedule[i][0] = sc.nextInt(); // 시작시간
			schedule[i][1] = sc.nextInt(); // 끝나는 시간
		}
	
		Arrays.sort(schedule,(a, b)-> a[1]==b[1] ? a[0]-b[0] : a[1]-b[1]); 
		// 끝나는 시간 기준으로 정렬 끝나는 시간이 같으면 시작시간 기준으로 정렬
		
		int endTime = 0; // 끝나는 시간
		int count = 0; // 회의의 수

		for(int i=0; i<N; i++){
			if (schedule[i][0] >= endTime) { // 회의 시작 시간이 이전 회의의 끝나는 시간 이후면
				endTime = schedule[i][1]; // 끝나는 시간 바꿔주고 
				count++; // 회의 추가
			}
		}
		System.out.print(count);
		
	}

}
