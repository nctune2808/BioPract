/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package GeneticAlgorithm;

import java.util.Arrays;

/**
 *
 * @author Marken Tuan Nguyen
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    
    public static int N=10;
    public static int P=50;
    
              
    public static void main(String[] args) {
        
        Individual individual = new Individual();
        System.out.println("================================================");
        
        Population population = new Population();
        Individual[] pop = population.population;
        System.out.println("Total Fitness Population: "+ population.totalFitnessPopulation);
        System.out.println("================================================");
 
//        
        Selection selection = new Selection(pop);
        Individual[] off = selection.offSpring;
        System.out.println("Total Fitness Offsprings: "+ selection.totalFitnessOffsprings);
        System.out.println("================================================");
        
        Crossover crossover = new Crossover(off);
        System.out.println("Total Fitness CrossOver: "+ crossover.totalFitnessCrossover); 
        System.out.println("================================================");
//        System.out.println("After Crossover:\n"+crossover.toString());
//        
//        mutation = new Mutation(numberOfGenes);
//        
////        System.out.println(population.calcPopFitness());
////        System.out.println("Population of "+population.getIndividuals()+" individual(s).");

    }
    
    
    
}
