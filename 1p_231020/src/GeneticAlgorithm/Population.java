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
    int totalFitnessPopulation = 0;     //takes fitness from individuals
    int totalFitnessOffsprings = 0;     //takes fitness from better offsprings
    public Population(int popSize, int geneLength){
        this.popSize = popSize;
        this.geneLength = geneLength;
        this.individuals = new Individual[popSize];
        
        for(int i=0; i<popSize; i++){
            individuals[i] = new Individual(geneLength);
            totalFitnessPopulation += individuals[i].calcIndFitness();
            
            System.out.println(Arrays.toString(individuals[i].getGenes()));
            System.out.println(individuals[i].getFitness());
            System.out.println(totalFitnessPopulation);
        }
        
        
        
    }
    
    public Individual[] selection () {
        
        Individual[] offSpring = new Individual[popSize];    //temp[]
        Individual off1, off2;
        int parent1,parent2;
        
        Random ran = new Random();
        for(int i=0;i<popSize; i++){
            parent1 = Math.abs(ran.nextInt()%popSize);
            off1 = individuals[parent1];
            parent2 = Math.abs(ran.nextInt()%popSize);
            off2 = individuals[parent2];
            
            if(off1.fitness > off2.fitness){
                offSpring[i] = off1;
            }else{
                offSpring[i] = off2;
            }
            
            
            System.out.println("--------------------------");
//            System.out.println("Parent1: "+parent1);
            System.out.println("off1: " + (off1.fitness));
//            System.out.println("Parent2: "+parent2);
            System.out.println("off2: " + (off2.fitness));
            
            System.out.println("select->: " + offSpring[i].fitness );
            System.out.println("--------------------------");
        }  
        
        for (int i = 0; i < offSpring.length; i++) {
            totalFitnessOffsprings += offSpring[i].fitness;
        }
        
        System.out.println("Total Fitness Offsprings: "+totalFitnessOffsprings);
                    
        return null;
    }
    
//    public int calcPopFitness(){
//        
//        
//        
//        
//        return selection().fitness;
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
