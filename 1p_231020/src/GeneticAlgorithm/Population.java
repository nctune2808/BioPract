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
    
    public Population(int popSize, int geneLength){
        this.popSize = popSize;
        this.geneLength = geneLength;
        this.individuals = new Individual[popSize];
        
        for(int i=0; i<popSize; i++){
            individuals[i] = new Individual(geneLength);
            individuals[i].calcIndFitness();
            
            System.out.println(Arrays.toString(individuals[i].getGenes()));
            System.out.println(individuals[i].getFitness());
        }
        
    }
    
    public int[] selection () {
        
        int[] selected_inds = new int[popSize];    //temp[]
        int off1, off2;
        int parent1,parent2;
        
        Random ran = new Random();
        for(int i=0;i<popSize; i++){
            parent1 = Math.abs(ran.nextInt()%popSize);
            off1 = individuals[parent1].getFitness();
            parent2 = Math.abs(ran.nextInt()%popSize);
            off2 = individuals[parent2].getFitness();
            
            if(off1 > off2){
                selected_inds[i] = off1;
            }else{
                selected_inds[i] = off2;
            }
            System.out.println("--------------------------");
//            System.out.println("Parent1: "+parent1);
            System.out.println("off1: " + (off1));
//            System.out.println("Parent2: "+parent2);
            System.out.println("off2: " + (off2));
            System.out.println("--------------------------");
        }
        
        
        
        return selected_inds;
    }
    
//    public void calcPopFitness(){
//        for (int i = 0; i < individuals.length; i++) {
//            individuals[i].calcIndFitness();
//        }
//    }
    

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
