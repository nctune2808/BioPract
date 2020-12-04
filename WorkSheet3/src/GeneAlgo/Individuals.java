package GeneAlgo;


import java.text.DecimalFormat;
import java.util.Random;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Marken Tuan Nguyen
 */
public class Individuals {
    private double[][] chromosome;
    private int fitness;
    
    public Individuals(int size, int length) {
        chromosome = new double[size][length];
    }
    
    public Individuals(Individuals nextGen) {
        double temp[][] = nextGen.getChromosome();
        chromosome = new double [temp.length][temp[0].length];
        for(int i = 0; i < temp.length; i++) {
            System.arraycopy(temp[i], 0, chromosome[i], 0, temp[i].length);
        }
        fitness = nextGen.getFitness();
    }
    
    public void fitnessFunction(double[][] dataset) {
        fitness = 0;
        boolean match = false;
        for (double[] dataset1 : dataset) 
        {
            for (double[] rule : chromosome) 
            {
                for (int k = 0; k < dataset1.length - 1; k++) 
                {
                    if (((dataset1[k] >= 0.5) && (rule[k] >= 0.5)) ||
                        ((dataset1[k] <= 0.5) && (rule[k] <= 0.5)) ||
                         (dataset1[k] ==  rule[k])         ||
                         (rule[k]     == 0.5)) {

                        match = true;
                    } 
                    else 
                    {
                        match = false;
                        break;
                    }
                }
                if (match == true) 
                {
                    if (dataset1[dataset1.length - 1] == rule[rule.length - 1]) 
                    {
                        fitness++;
                    }
                    break;
                }
            }
        }
    }
    
    public void createChromosome() {
        DecimalFormat df = new DecimalFormat("#.##");
        for (double[] rule : chromosome) {
            for (int j = 0; j < rule.length - 1; j++) {
                rule[j] = (new Random().nextInt(3) == 2) ? 0.50 : Double.parseDouble(df.format(Math.random())); // 0.05 is the wildcard
            }
            rule[rule.length - 1] = new Random().nextInt(2); 
        }
    }
    
    public void mutation(double rate) {
        for (double[] rule : chromosome) {
            for (int j = 0; j < rule.length - 1; j++) {
                if (rate <= Math.random()) {
                    rule[j] = (new Random().nextInt(3) == 2) ? 0.50 : Double.parseDouble(new DecimalFormat("#.##").format(Math.random())); // 0.05 is the wildcard
                }
            }
            if (rate <= Math.random()) {
                rule[rule.length - 1] = new Random().nextInt(2);
            }
        }
    }
    
    public double[][] getChromosome() {
        return chromosome;
    }
    
    public int getFitness() {
        return fitness;
    }
}
