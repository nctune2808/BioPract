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
    private static Population population;    
    private static Selection selection;
    private static Crossover crossover;
    
    private static int numberOfGenes;
    private static int numberOfIndividuals;
              
    public static void main(String[] args) {
 
        numberOfGenes = 10;
        numberOfIndividuals = 5;
                
        population = new Population(numberOfIndividuals, numberOfGenes);
        System.out.println("Total Fitness Population: "+ population.totalFitnessPopulation);
        
        selection = new Selection(population);
        System.out.println("Total Fitness Offsprings: "+ selection.totalFitnessOffsprings);
        
        crossover = new Crossover(selection.firstFittest(), selection.secondFittest(), numberOfGenes);
        System.out.println("After Crossover:\n"+crossover.toString());
        
//        System.out.println(population.calcPopFitness());
//        System.out.println("Population of "+population.getIndividuals()+" individual(s).");

    }
    
    
    
}
