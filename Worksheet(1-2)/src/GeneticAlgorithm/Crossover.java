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
    
    Individual temp = new Individual();
    Individual[] offCross;
    int totalFitnessCrossover, crossfit, sum = 0;
    
    public Crossover (Individual[] offSpring ) {
        
        Random rand = new Random();
        
        int crossPoint = Math.abs(rand.nextInt(Main.N));
        System.out.println("cross point: "+ (crossPoint+1));
        
        for(int i=0; i<Main.P; i+=2){   
//            System.out.println("BEFORE CROSSOVER:");
//            System.out.println("child1->: "+Arrays.toString(offSpring[i].genes));
//            System.out.println("child2->: "+Arrays.toString(offSpring[i+1].genes));
            
            for(int j=crossPoint; j<Main.N; j++){
                
                this.temp.genes[j] = offSpring[i].genes[j];             //THIS....       
                offSpring[i].genes[j] = offSpring[i+1].genes[j];
                offSpring[i+1].genes[j] = temp.genes[j];
            }
            
//            System.out.println("AFTER CROSSOVER:");
//            System.out.println("child1->: "+Arrays.toString(offSpring[i].genes));
//            System.out.println("child2->: "+Arrays.toString(offSpring[i+1].genes));
//
//            System.out.println("------------------------------------------------");
            
        }
        this.offCross = offSpring;
        totalFitnessCrossover += calCrossFitness(offSpring);
        
        
    }

	
    public int calCrossFitness(Individual[] offtemp){
        for(int i=0; i<Main.P; i++){
            for(int j=0; j<Main.N; j++){
                if(offtemp[i].genes[j]==1){
                    crossfit++;
                }
            }
        }
        return crossfit;
    }
    
}
