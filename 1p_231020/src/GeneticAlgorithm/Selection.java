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
public class Selection {
    
    Individual off1, off2;
    Individual[] offSpring;
    int parent1,parent2;
    int totalFitnessOffsprings = 0;     //takes fitness from offsprings
        
    public Selection (Population pop) {      //return Individual[]
        
        offSpring = new Individual[pop.popSize];    //temp[]
        
        Random ran = new Random();
        for(int i=0;i<pop.popSize; i++){
            parent1 = Math.abs(ran.nextInt(pop.popSize));
            off1 = pop.individuals[parent1];
            parent2 = Math.abs(ran.nextInt(pop.popSize));
            off2 = pop.individuals[parent2];
            
            if(off1.fitness > off2.fitness){
                offSpring[i] = off1;
            }else{
                offSpring[i] = off2;
            }
//            
            System.out.println("select->: " + Arrays.toString(offSpring[i].genes) );
        }  
        
        for (int i = 0; i < offSpring.length; i++) {
            totalFitnessOffsprings += offSpring[i].fitness;
        }
        
//        System.out.println("Total Fitness Offsprings: "+totalFitnessOffsprings);
            
    }
    
    public Individual firstFittest(){
        return off1;
    }
    
    public Individual secondFittest(){
        return off2;
    }
}
