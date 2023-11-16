import java.util.*;

public class connect4 {

	private static char cpu = 'O';
    private static char player = 'X';

	public static void initialize(char[][] ch) {
		System.out.println("CONNECT 4!!\n You : 'X'\n CPU : 'O'\n");
		
		for(int i=0; i<6; i++) {
			for(int j=0; j<7; j++) {
				ch[i][j] = ' ';
			}
		}
		print(ch);
	}

	public static void print(char[][] ch) {
	System.out.println("\n   1   2   3   4   5   6   7\n   |   |   |   |   |   |   |\n   V   V   V   V   V   V   V\n");
		for(int i=0; i<6; i++) {
			for(int j=0; j<7; j++) {
				System.out.print(" | "+ch[i][j]);
			}
			System.out.print(" |");
			System.out.println();
		}
		System.out.print(" -----------------------------\n");
	}
	
	public static void playerinput(char[][] ch) {
		Scanner in = new Scanner(System.in);
		int column = Integer.MIN_VALUE;
		do {
			do {
				System.out.println("Enter your slot(1-7)");
				column = in.nextInt();
				column--;
				if(column<0 || column>6)
					System.out.println("Input out of range!! Try again.\n");
			}while(column<0 || column>6);
			
			if(ch[0][column] != ' ') {
				System.out.println("This column is fully occupied! Try again.");
			}
		}while(ch[0][column] != ' ');
		for(int i=5; i>=0; i--) {
			if(ch[i][column] == ' ') {
				ch[i][column] = player;
				break;
			}
		}
	}
	
	public static void cpuinput(char[][] ch) {
		Random rand = new Random();
		int column = Integer.MIN_VALUE;
		boolean isFull = false;
		do {
			isFull = false;
			column = rand.nextInt(7);
			// column = 0;
			if(ch[0][column] != ' ') {
				//System.out.println("This column is fully occupied! Try again.");
				isFull = true;
				continue;
			}
			for(int i=5; i>=0; i--) {
				if(ch[i][column] == ' ') {
					ch[i][column] = cpu;
					break;
				}
			}	
			
		}while(isFull == true);
	}
	
	
	
	public static char checkwinner(char[][] ch) {
		char winner = ' ';
		//vertical check
		for(int i=0; i<3; i++) {
			for(int j=0; j<7; j++) {
				if(ch[i][j]!=' ' && (ch[i][j]==ch[i+1][j] && ch[i][j]==ch[i+2][j] && ch[i][j]==ch[i+3][j]))
					winner = ch[i][j];
			}
		}
		//horizontal check
		for(int i=0; i<6; i++) {
			for(int j=0; j<4; j++) {
				if(ch[i][j]!=' ' && (ch[i][j]==ch[i][j+1] && ch[i][j]==ch[i][j+2] && ch[i][j]==ch[i][j+3]))
					winner = ch[i][j];
			}
		}
		//diagonal right->left
		for(int i=0; i<3; i++) {
			for(int j=0; j<4; j++) {
				if(ch[i][j]!=' ' && (ch[i][j]==ch[i+1][j+1] && ch[i][j]==ch[i+2][j+2] && ch[i][j]==ch[i+3][j+3]))
					winner = ch[i][j];
			}
		}
		//diagonal left->right
		for(int i=0; i<3; i++) {
			for(int j=3; j<7; j++) {
				if(ch[i][j]!=' ' && (ch[i][j]==ch[i+1][j-1] && ch[i][j]==ch[i+2][j-2] && ch[i][j]==ch[i+3][j-3]))
					winner = ch[i][j];
			}
		}
		return(winner);
	}
	
	public static void main(String []args) {
		char[][] ch = new char [6][7];
		char winner = ' ';
		initialize(ch);
		for(int i=0; i<42; i++) {
			if(i%2==1)
				cpuinput(ch);
			else
				playerinput(ch);
			print(ch);
			winner = checkwinner(ch);
			if(winner==player) {
            	System.out.println("\n************\n|You win!!!|\n************");
                System.exit(0);
            }
            else if(winner==cpu) {
            	System.out.println("\n*************\n|CPU wins!!!|\n*************");
                System.exit(0);
            }
			
		}
		System.out.println("\n**********\n|DRAWW!!!|\n**********");
	}
}
