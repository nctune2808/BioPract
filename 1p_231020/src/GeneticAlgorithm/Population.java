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
public class Population {
    Individual[] individuals;
    int popSize;
    int geneLength;
    
    public Population(int popSize, int geneLength){
        super();
        this.popSize = popSize;
        this.geneLength = geneLength;
        this.individuals = new Individual[popSize];
        
        for(int i=0; i<popSize; i++){
            individuals[i] = new Individual(geneLength);
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
