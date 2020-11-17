/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package GeneticAlgorithm;

import java.util.Arrays;
import java.util.Random;

/**
 *
 * @author Marken Tuan Nguyen
 */
public class Crossover {
   
    Individual temp;
    Selection select;
    public Crossover (Selection select) {
        
        this.select = select;
        
        for( int i=0; i< 5; i+=1){
            
            Random rand = new Random();
            int crossPoint = Math.abs(rand.nextInt()%10);
            System.out.println("=> i= "+i);
            for(int j=crossPoint; j<10; j++){
                System.out.println("j= "+ j);
//                System.out.println("Cross1: "+ Arrays.toString(select.offSpring[i].genes));
//                System.out.println("Cross2: "+ Arrays.toString(select.offSpring[i+1].genes));
            }
            System.out.println("----------------------------------");
        }
        

    }
	
    
}
