/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package GeneAlgo;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author Marken Tuan Nguyen
 */
public class Population {
    double[][] dataset;
    private double[][] normalizedTrainSet;
    private double[][] normalizedTesting;
    Individuals[] population;
    Individuals[] matingPool;
    double mutationRate;
    int populationSize;
    int chromosomeLength;
    int chromosomeSize;

    int bestFitness;
    double averageFitness;
    int worstFitness;
    private int totalFitness;
    
    
    public Population(double mutation, int PopSize, int choromLen, int choromSize) {
            
        this.mutationRate = mutation;
        this.populationSize = PopSize;
        this.chromosomeLength = choromLen;
        this.chromosomeSize = choromSize;

        population = new Individuals[populationSize];
        matingPool = new Individuals[populationSize];

        for (int i = 0; i < population.length; i++) {
            population[i] = new Individuals(chromosomeSize, chromosomeLength);
            population[i].createChromosome();
        }

    }
    
    public void getDatasetData(String file) {
        Scanner scn = new Scanner(Population.class.getResourceAsStream(file));
        double[][] dataSet;
        ArrayList<Double[]> tempList = new ArrayList();
        Double[] arr;

        while (scn.hasNextLine()) {
            String data = scn.nextLine();
            String[] split = data.split(" ");
            arr = new Double[split.length];

            for (int i = 0; i < split.length; i++) {
                arr[i] = Double.parseDouble(split[i]);
            }
            tempList.add(arr);
        }

//            System.out.println("Size: "+tempList.get(0).length);

        dataSet = new double[tempList.size()][tempList.get(0).length];

        for (int i = 0; i < dataSet.length; i++) {
            for (int j = 0; j < dataSet[i].length; j++) {
                dataSet[i][j] = tempList.get(i)[j];
            }
        }
        
//        System.out.println(dataSet[0].length);
        //copy trinmed verson to normalised dataset
        double[][] normalizedDataset;
        normalizedDataset = new double[dataSet.length][dataSet[0].length];

        for (int i = 0; i < dataSet.length; i++) {
            for (int j = 0; j < dataSet[i].length; j++) {
                normalizedDataset[i][j] = Double.parseDouble(new DecimalFormat("#.##").format(dataSet[i][j]));
            }
        }
        //split into traing and testing sets
        int var = 0;
        normalizedTrainSet = new double[(int) (dataSet.length * 0.50)][dataSet[0].length];
        normalizedTesting = new double[(int) (dataSet.length * 0.50)][dataSet[0].length];
//                System.out.println("normalizedTesting " +normalizedDataset.length);
        for (int i = 0; i < normalizedDataset.length; i++) {
            
            if (i < normalizedTrainSet.length) {
                normalizedTrainSet[i] = normalizedDataset[i];
                System.out.println("<<<"+Arrays.toString(normalizedDataset[i]));
//                System.out.println("normalized TRAIN " +i);
            } 
            else {
                normalizedTesting[var] = normalizedDataset[i];
                System.out.println(">>>"+Arrays.toString(normalizedDataset[i]));
                var++;
            };
        }
    }
    
    public void fitnessFunction() {
        totalFitness = 0;
        bestFitness = 0;
        worstFitness = population[0].getFitness();
        averageFitness = 0;
        for (Individuals pop : population) {
            pop.fitnessFunction(normalizedTrainSet);
            if (bestFitness < pop.getFitness()) {
                bestFitness = pop.getFitness();
            }
            if (worstFitness > pop.getFitness()) {
                worstFitness = pop.getFitness();
            }
            averageFitness += pop.getFitness();
            totalFitness += pop.getFitness();
//            System.out.println("Total fitness: "+totalFitness);
        }
        averageFitness = averageFitness / population.length;
    }
    
    private Individuals rouletteWheelSelection() {
        int randomNumber = new Random().nextInt(totalFitness + 1);
        int sumOfFitness = 0;
        int savedIndex;
        for (savedIndex = 0; savedIndex < population.length; savedIndex++) {
            if (sumOfFitness > randomNumber) {
                break;
            }
            sumOfFitness += population[savedIndex].getFitness();
        }
        return population[savedIndex - 1];
    }

    private Individuals[] singlePointCrossover(Individuals parent1, Individuals parent2) {
        Individuals[] children = new Individuals[2];
        children[0] =  new Individuals(parent1);
        children[1] =  new Individuals(parent2);
        Random rand = new Random();
        int crossoverPoint = rand.nextInt(chromosomeLength*chromosomeSize);
        int pointer = 0;
        for(int i = 0; i < parent1.getChromosome().length; i++) {
            for(int j = 0; j < parent1.getChromosome()[i].length; j++) {
                if(pointer < crossoverPoint) {
                    double temp = children[0].getChromosome()[i][j];
                    children[0].getChromosome()[i][j] = children[1].getChromosome()[i][j];
                    children[1].getChromosome()[i][j] = temp;
                }
                else break;
                pointer++;
            }
            if(pointer >= crossoverPoint)
                break;
        }
        return children;
    }
        
    public void newGeneration() {
        for(int i = 0; i < population.length; i++) {
            population[i] = new Individuals(matingPool[i]);
        }
    }
    
    public void mutation() {
        for (Individuals pool : matingPool) {
            pool.mutation(mutationRate);
        }
    }

    public void crossover() {
        for (int i = 0; i < matingPool.length / 2; i++) {
            int offset = i * 2;
            Individuals[] children = singlePointCrossover(matingPool[offset], matingPool[offset + 1]);
            matingPool[i] = children[0];
            matingPool[i + 1] = children[1];
        }
    }

    public void selection() {
        for (int i = 0; i < matingPool.length; i++) {
            matingPool[i] = rouletteWheelSelection();
        }
    }
    
    
    
    public int getBestFitness() {
        return bestFitness;
    }

    public double getAverageFitness() {
        return averageFitness;
    }

    public int getWorstFitness() {
        return worstFitness;
    }
    
    
}
