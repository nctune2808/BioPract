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
public class Crossover {
   
    Individual Child1, Child2;
    Individual temp;
    
    public Crossover (Individual stTest, Individual ndTest, int numberOfGenes) {
        temp = new Individual(numberOfGenes);
        
        Random rand = new Random();
        int crossPoint = Math.abs(rand.nextInt(stTest.geneLength));
        
        System.out.println("------------------------------------------------");
        System.out.println("cross point: "+ (crossPoint+1));
        System.out.println("------------------------------------------------");
        System.out.println("BEFORE CROSSOVER:");
        System.out.println("first test:\t"+ Arrays.toString(stTest.getGenes()));
        System.out.println("second test:\t"+ Arrays.toString(ndTest.getGenes()));
        System.out.println("------------------------------------------------");
        for(int i=crossPoint; i<numberOfGenes; i++){        //swap head
            temp.genes[i] = stTest.genes[i];
            stTest.genes[i] = ndTest.genes[i];
            ndTest.genes[i] = temp.genes[i];
        }

        Child1 = stTest;
	Child2 = ndTest;
        
        
//        System.out.println("temp test:\t"+ Arrays.toString(temp.getGenes()));
        
    }
    
    public String getChild1(){
        return "first test:\t"+ Arrays.toString(Child1.getGenes());
    }
    
    public String getChild2(){
        return "second test:\t"+ Arrays.toString(Child2.getGenes());
    }
    
    @Override
    public String toString(){
        return getChild1() +"\n"+getChild2();
    }
	
    
}
