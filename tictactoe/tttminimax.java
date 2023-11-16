import java.util.*;

public class tttminimax
{
    private static char cpu = 'O';
    private static char player = 'X';
    
    public int minimax(char[] ch, int depth, boolean maximizer)
    {
    	int score = 0;
    	tttminimax ob1 = new tttminimax();
    	char winner = ob1.checkWinner(ch);
    	if(depth==0 || winner != ' ' ) {
    		if(winner == cpu)
    			score = 1;
    		if(winner == player)
    			score = -1;
    		if(winner == 'T')
    			score = 0;
    		return(score);
    	}
    	
    	if(maximizer == true) {
    		int bestscore =  Integer.MIN_VALUE;	
    		for(int i=1; i<=9; i++) {
    			if(ch[i]==' ') {
    				ch[i] = cpu;
    				score = ob1.minimax(ch, depth--, false);
    				ch[i] = ' ';
    				bestscore = Math.max(score, bestscore);
    			}
    		}
    		return(bestscore);
    	}
    	else {
    		int bestscore =  Integer.MAX_VALUE;	
    		for(int i=1; i<=9; i++) {
    			if(ch[i]==' ') {
    				ch[i] = player;
    				score = ob1.minimax(ch, depth--, true);
    				ch[i] = ' ';
    				bestscore = Math.min(score, bestscore);
    			}
    		}
    		return(bestscore);
    	}
    }
    
    public int cpuinput(char[] ch)
    {
        int bestscore = Integer.MIN_VALUE;
        int pos = 0;
		for(int i=1; i<=9; i++)
		{
			if(ch[i]==' ')
			{
				ch[i] = cpu;
				int score = minimax(ch, 10, false);
				ch[i] = ' ';
				if(score>bestscore)
				{
					bestscore = score;
					pos = i;
				}
			}
		}
		return(pos);
    }
    
    public int playerinput()
    {
        Scanner in = new Scanner(System.in);
        int pos = 0;
        do
        {
            System.out.println("\nEnter position (1-9)");
            pos = in.nextInt();
            if(pos>9 || pos<1)
                System.out.println("Invalid input! Enter again.");
        }while(pos>9 || pos<1);
        return(pos);
    }
    
    public void print(char[] ch)
    {
        System.out.println();
        for(int i=0; i<3; i++)
        {
            for(int j=1; j<=3; j++)
            {
                if(j==3)
                    System.out.print(" "+ch[(3*i)+j]);
                else
                    System.out.print(" "+ch[(3*i)+j]+" |");
            }
            if(i==0 || i==1)
                System.out.println("\n---+---+---");    
        }
        System.out.println();
    }
    
    public boolean checkpos(char[] ch, int pos)
    {
        if(ch[pos]==' ')
            return(true);
        else
            return(false);
    }
    
    public char checkWinner(char[] ch)
    {
    	char winner = ' ';
    	int freespaces = 0;
        if((ch[1]==player&&ch[2]==player&&ch[3]==player) ||  (ch[1]==player&&ch[4]==player&&ch[7]==player) ||  (ch[1]==player&&ch[5]==player&&ch[9]==player) ||  (ch[2]==player&&ch[5]==player&&ch[8]==player) || (ch[4]==player&&ch[5]==player&&ch[6]==player) ||  (ch[7]==player&&ch[8]==player&&ch[9]==player) || (ch[3]==player&&ch[5]==player&&ch[7]==player) ||  (ch[3]==player&&ch[6]==player&&ch[9]==player))
        	winner = player;
        if((ch[1]==cpu&&ch[2]==cpu&&ch[3]==cpu) || (ch[1]==cpu&&ch[4]==cpu&&ch[7]==cpu) || (ch[1]==cpu&&ch[5]==cpu&&ch[9]==cpu) || (ch[2]==cpu&&ch[5]==cpu&&ch[8]==cpu) || (ch[4]==cpu&&ch[5]==cpu&&ch[6]==cpu) || (ch[7]==cpu&&ch[8]==cpu&&ch[9]==cpu) || (ch[3]==cpu&&ch[5]==cpu&&ch[7]==cpu) || (ch[3]==cpu&&ch[6]==cpu&&ch[9]==cpu))
        	winner = cpu;
        for(int i=1; i<=9; i++) {
        	if(ch[i]==' ') {
        		freespaces++;
        	}
        }
        
        if(winner==' ' && freespaces==0) {
        	winner = 'T';
        }
        
        return(winner);
    }
    
    public void initialize()
    {
        Scanner in = new Scanner(System.in);
        System.out.println("TIC TAC TOE!!!");
        System.out.println("YOU : "+player+"\nCPU : "+cpu+"\n");
        for(int i=0; i<3; i++)
        {
            for(int j=1; j<=3; j++)
            {
                if(j==3)
                    System.out.print(" "+((3*i)+j));
                else
                    System.out.print(" "+((3*i)+j)+" |");
            }
            if(i==0 || i==1)
                System.out.println("\n---+---+---");    
        }
        System.out.println();
    }
    
    public static void main(String[]args)
    {
        tttminimax ob = new tttminimax();
        char[] ch = new char[10];
        int pos = 0;
        char chr = ' ';
        boolean checker = false;
        for(int i=0; i<10; i++)
        {
            ch[i] = ' ';
        }
        ob.initialize();
        
        for(int i=1; i<=9; i++)
        {
            do
            {
                if(i%2==0)
                {
                    pos = ob.playerinput();
                    chr = player;
                }
                else
                {
                    pos = ob.cpuinput(ch);
                    chr = cpu;
                }
                
                checker = ob.checkpos(ch, pos);
                if(checker==true)
                    ch[pos] = chr;
                else
                    if(chr == player)  
                        System.out.println("Position occupied! Enter again!");
            }while(checker==false);
            
            
            ob.print(ch);
            char winner = ob.checkWinner(ch);
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

