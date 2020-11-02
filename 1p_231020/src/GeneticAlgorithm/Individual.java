/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package GeneticAlgorithm;

import java.util.Random;

/**
 *
 * @author Marken Tuan Nguyen
 */
public class Individual {
    int geneLength;
    int[] genes;
    int fitness = 0;
    
    public Individual(int geneLength) {
        this.geneLength = geneLength;
        this.genes = new int[geneLength];
        
        Random ran = new Random();
        for(int i=0; i<genes.length; i++){
            genes[i] = Math.abs(ran.nextInt()%2);
        }
        fitness = 0;
    }
    
    public void calcFitness() {
        for (int i = 0; i < genes.length; i++) {
            if (genes[i] == 1) {
                fitness++;
            }
        }
    }

    public int getGeneLength() {
        return geneLength;
    }

    public void setGeneLength(int geneLength) {
        this.geneLength = geneLength;
    }

    public int[] getGenes() {
        return genes;
    }

    public void setGenes(int[] genes) {
        this.genes = genes;
    }

    public int getFitness() {
        return fitness;
    }

    public void setFitness(int fitness) {
        this.fitness = fitness;
    }
    
    
}
