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
    double dataset[][];
    private double [][] normalizedTrainSet;
    private double [][] normalizedTesting;
    Individuals[] population;
    Individuals[] mateingPool;
    double mutationRate;
    int PopulationSize;
    int chromosomeLength;
    int chromosomeSize;

    int bestFitness;
    double averageFitness;
    int worstFitness;
    private int totalFitness;
    
    
    public Population(double mutation, int PopSize, int choromLen, int choromSize) {
            
        this.mutationRate = mutation;
        this.PopulationSize = PopSize;
        this.chromosomeLength = choromLen;
        this.chromosomeSize = choromSize;

        population = new Individuals[PopulationSize];
        mateingPool = new Individuals[PopulationSize];

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
        //copy trinmed verson to normalised dataset
        double[][] normalizedDataset;
        DecimalFormat df = new DecimalFormat("#.##");
        normalizedDataset = new double[dataSet.length][dataSet[0].length];

        for (int i = 0; i < dataSet.length; i++) {
            for (int j = 0; j < dataSet[i].length; j++) {
                normalizedDataset[i][j] = Double.parseDouble(df.format(dataSet[i][j]));
            }
        }
        //split into traing and testing sets
        int var = 0;
        normalizedTrainSet = new double[(int) (dataSet.length * 0.50)][dataSet[0].length];
        normalizedTesting = new double[(int) (dataSet.length * 0.50)][dataSet[0].length];
        for (int i = 0; i < normalizedDataset.length; i++) {
            
            if (i < normalizedTrainSet.length) {
                normalizedTrainSet[i] = normalizedDataset[i];
            } 
//            else {
//                normalizedTesting[var] = normalizedDataset[i];
//                System.out.println("normalizedTesting " +var);
//                var++;
//            }
        }
    }
    
    private Individuals rouletteWheelSelection() {
        int randomNumber = new Random().nextInt(totalFitness + 1);
        int sumOfFitness = 0;
        int savedIndex;
        for (savedIndex = 0; savedIndex < population.length; savedIndex++) {
            if (sumOfFitness > randomNumber) {
                break;
            }
//            System.out.println("sumFitness " + sumOfFitness);
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
        int pointer  =0;
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
            population[i] = new Individuals(mateingPool[i]);
        }
    }
    
    public void mutation() {
        for (Individuals matingpool1 : mateingPool) {
            matingpool1.mutation(mutationRate);
        }
    }

    public void crossover() {
        for (int i = 0; i < mateingPool.length / 2; i++) {
            int offset = i * 2;
            Individuals[] children = singlePointCrossover(mateingPool[offset], mateingPool[offset + 1]);
            mateingPool[i] = children[0];
            mateingPool[i + 1] = children[1];
        }
    }

    public void selection() {
        for (int i = 0; i < mateingPool.length; i++) {
            mateingPool[i] = rouletteWheelSelection();
        }
    }
    
    public void fitnessFunction() {
        totalFitness = 0;
        bestFitness = 0;
        worstFitness = population[0].getFitness();
        averageFitness = 0;
        for (Individuals population1 : population) {
            population1.fitnessFunction(normalizedTrainSet);
            if (bestFitness < population1.getFitness()) {
                bestFitness = population1.getFitness();
            }
            if (worstFitness > population1.getFitness()) {
                worstFitness = population1.getFitness();
            }
            averageFitness += population1.getFitness();
            totalFitness += population1.getFitness();
//            System.out.println("Total fitness: "+totalFitness);
        }
        averageFitness = averageFitness / population.length;
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
