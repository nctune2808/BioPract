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
        Individual[] offCr = crossover.offCross;
//        System.out.println("offCross: "+ Arrays.toString(crossover.offCross[0].genes));
//        System.out.println("offCross: "+ Arrays.toString(crossover.offCross[1].genes));
//        System.out.println("offCross: "+ Arrays.toString(crossover.offCross[2].genes));
//        System.out.println("offCross: "+ Arrays.toString(crossover.offCross[3].genes));
        System.out.println("Total Fitness CrossOver: "+ crossover.totalFitnessCrossover); 
        System.out.println("================================================");
        
        Mutation mutation = new Mutation(offCr);
        System.out.println("Total Fitness Mutution: "+ mutation.totalFitnessMutation); 
        System.out.println("================================================");

    }
    
    
    
}
