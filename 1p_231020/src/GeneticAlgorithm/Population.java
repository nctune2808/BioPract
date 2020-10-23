/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package GeneticAlgorithm;

/**
 *
 * @author Marken Tuan Nguyen
 */
public class Population {
    Individual[] pop = new Individual[50];
    
    public void initialPop (int size){
        for(int i=0; i<size; i++){
            pop[i] = new Individual();
        }
    }
}
