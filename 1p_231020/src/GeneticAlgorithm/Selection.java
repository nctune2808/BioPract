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
    
    Individual[] offSpring = new Individual[Main.P];
    Individual off1, off2;
    int totalFitnessOffsprings = 0;     //takes fitness from offsprings
        
    public Selection (Individual[] population) {      //return Individual[]
                
        Random ran = new Random();
        for(int i=0;i<Main.P; i++){
            int parent1 = Math.abs(ran.nextInt(Main.P));
            int parent2 = Math.abs(ran.nextInt(Main.P));
//            off1 = population[parent1];
//            off2 = population[parent2];
            
            if(population[parent1].fitness > population[parent2].fitness){
                this.offSpring[i] = population[parent1];
            }else{
                this.offSpring[i] = population[parent2];
            }
//            System.out.println("---------------------------------------------------------");
//            System.out.println("p1: " + Arrays.toString(population[parent1].genes)+ "\tF= "+population[parent1].fitness);
//            System.out.println("p2: " + Arrays.toString(population[parent2].genes)+ "\tF= "+population[parent2].fitness);
//            
            System.out.println("select->: " + Arrays.toString(this.offSpring[i].genes) );
        }
        calSelectFitness();
    }
    
    public int calSelectFitness(){
        for (int i = 0; i < offSpring.length; i++) {
            this.totalFitnessOffsprings += offSpring[i].fitness;
        }
        return totalFitnessOffsprings;
    }

}
