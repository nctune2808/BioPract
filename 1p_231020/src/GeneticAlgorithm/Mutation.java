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
public class Mutation {
    
    Individual mutation;

    public Mutation(int numberOfGenes) {
        Random rand = new Random();
        mutation = new Individual(numberOfGenes);
        int mutationPoint = Math.abs(rand.nextInt(mutation.geneLength));
        double randRate = rand.nextDouble();
        System.out.println("mutationPoint: " + mutationPoint);
        System.out.println("randRate: " + randRate);
        
        if( randRate < 0.3 ){
            System.out.println("OK");
            if(mutation.genes[mutationPoint] == 0) {
                mutation.genes[mutationPoint] = 1;
            }else {
                mutation.genes[mutationPoint] = 0;
            }
        }
        
    }
    
    
    
}
