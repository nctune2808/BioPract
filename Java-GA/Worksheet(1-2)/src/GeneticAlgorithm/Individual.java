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
public class Individual {
    int[] genes = new int[10];
    int fitness = 0;
    
    public Individual() {
        Random rand = new Random();

        for(int i=0; i<Main.N; i++) {
            this.genes[i] = (Math.abs(rand.nextInt())%2); //generates 0 or 1 randomly
        }
        this.fitness=0;
    }
    
    public int calFit(){
        for (int i = 0; i <Main.N; i++) {
            if (this.genes[i] == 1) {
                this.fitness +=1;
            }
        }
        return fitness;
    }
}
