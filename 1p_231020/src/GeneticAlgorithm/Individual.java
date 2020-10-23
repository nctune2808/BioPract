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
    int[] genes = new int[10];
    int fitness = 0;
    
    public Individual() {
        Random ran = new Random();
 
        for(int i=0; i<genes.length; i++){
            genes[i] = ran.nextInt()%2;
        }
        fitness = 0;
    }
}
