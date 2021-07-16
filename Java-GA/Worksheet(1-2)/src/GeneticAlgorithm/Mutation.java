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
public class Mutation {
    
    Individual mutation;
    double MUTRATE = 0.3;
    int totalFitnessMutation, mutateFit = 0;
    public Mutation(Individual[] offspring) {
        Random rand = new Random();
        for( int i=0; i<Main.P; i++) {
            for( int j=0; j<Main.N; j++ ) {
                
                if( rand.nextDouble() < MUTRATE ) {
                    if( offspring[i].genes[j] == 1 ) {
                        offspring[i].genes[j] = 0;
                    }
                    else {
                        offspring[i].genes[j] = 1;
                    }
                }
            }
//            System.out.println("mutate->: "+Arrays.toString(offspring[i].genes));
            
        }
        totalFitnessMutation += calMutateFitness(offspring);
    }
    
    public int calMutateFitness(Individual[] offtemp){
        for(int i=0; i<Main.P; i++){
            for(int j=0; j<Main.N; j++){
                if(offtemp[i].genes[j]==1){
                    mutateFit++;
                }
            }
        }
        return mutateFit;
    }
    
    
}
