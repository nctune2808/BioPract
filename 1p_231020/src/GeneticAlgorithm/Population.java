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
    
//    Pop ( Ind ( Gen )  )
    
    Individual[] individuals;
    int popSize;    // P:numberOfIndividuals
    int geneLength; // N:numberOfGenes
    int totalFitnessPopulation = 0;     //takes fitness from population
    
    public Population(int popSize, int geneLength){
        this.popSize = popSize;
        this.geneLength = geneLength;
        this.individuals = new Individual[popSize];
        
        for(int i=0; i<popSize; i++){
            individuals[i] = new Individual(geneLength);
            totalFitnessPopulation += individuals[i].calcIndFitness();
            
            System.out.println(Arrays.toString(individuals[i].getGenes()));
//            System.out.println(individuals[i].getFitness());
//            System.out.println(totalFitnessPopulation);
        }
        
        
        
    }
    
    
    public Individual[] getIndividuals() {
        return individuals;
    }

    public void setIndividuals(Individual[] individuals) {
        this.individuals = individuals;
    }

    public int getPopSize() {
        return popSize;
    }

    public void setPopSize(int popSize) {
        this.popSize = popSize;
    }

    public int getGeneLength() {
        return geneLength;
    }

    public void setGeneLength(int geneLength) {
        this.geneLength = geneLength;
    }
    
    
    
}
