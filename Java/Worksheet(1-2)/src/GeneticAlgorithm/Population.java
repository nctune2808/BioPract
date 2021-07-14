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
public class Population {

    int totalFitnessPopulation = 0;
    Individual[] population = new Individual[Main.P];
    
    
    
    public Population(){
        
        for(int i=0; i<Main.P; i++){
            population[i] = new Individual();
            totalFitnessPopulation += population[i].calFit();
//            totalFitnessPopulation = getTotalFitnessPopulation(population[i]);
//            System.out.println("Genes: "+Arrays.toString(population[i].genes));
        }
        
    }
    
//    public int getTotalFitnessPopulation(Individual ind) {
//        totalFitnessPopulation += ind.calFit();
//        return totalFitnessPopulation;
//    }

    
    
    
    
    
}
