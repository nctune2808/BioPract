/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package GeneAlgo;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFormattedTextField;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JRadioButton;
import javax.swing.text.NumberFormatter;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

/**
 *
 * @author Marken Tuan Nguyen
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        ControlPanel cpanel = new Main().new ControlPanel();
        cpanel.dashboard();
    }
    
    public class ControlPanel {
        JFrame frame = new JFrame("Control Panel");
        JPanel optionsPanel = new JPanel();
        JPanel chartPanel = new JPanel();
        JRadioButton radioBtn1 = new JRadioButton("data1.txt");
        JRadioButton radioBtn2 = new JRadioButton("data2.txt");
        JRadioButton radioBtn4 = new JRadioButton("data4.txt");
        ButtonGroup datasetsBtn = new ButtonGroup();
        
        NumberFormatter nf = new NumberFormatter();
        JFormattedTextField mutationRate  = new JFormattedTextField(nf);
        JFormattedTextField populationSize  = new JFormattedTextField(nf);
        JFormattedTextField chromosomeLength  = new JFormattedTextField(nf);
        JFormattedTextField chromosomeSize  = new JFormattedTextField(nf);
        JFormattedTextField generatuinSize  = new JFormattedTextField(nf);
        JButton runBtn = new JButton("Run");
        JProgressBar progress = new JProgressBar();
        XYSeries best = new XYSeries("Best Fitness");
        XYSeries worst = new XYSeries("Worst Fitness");
        XYSeries avrg = new XYSeries("Average Fitness");
        JFreeChart lineGraph;
        public void dashboard(){
            frameSetup();
            radioBtnSetup();
            chartSetup("Graph");
            inputFeildSetup();
            progressBarSetup();
            runBtnSetup();
            functions();
            frame.pack();
        }
        
        private void functions() {
            
            radioBtn1.addActionListener((ActionEvent e) -> {
                frame.repaint();
                optionsPanel.repaint();
                
                populationSize .setValue(1000);
                mutationRate .setValue(0.02);
                chromosomeLength .setValue(7);
                chromosomeSize .setValue(32);
                generatuinSize .setValue(200);
            });

            radioBtn2.addActionListener((ActionEvent e) -> {
                frame.repaint();
                optionsPanel.repaint();
                populationSize .setValue(1000);
                mutationRate .setValue(0.02);
                chromosomeLength .setValue(7);
                chromosomeSize .setValue(32);
                generatuinSize .setValue(200);
            });

            radioBtn4.addActionListener((ActionEvent e) -> {
                frame.repaint();
                optionsPanel.repaint();
                populationSize .setValue(1000);
                mutationRate .setValue(0.02);
                chromosomeLength .setValue(11);
                chromosomeSize .setValue(512);
                generatuinSize .setValue(200);
            });
            
            runBtn.addActionListener((ActionEvent e) -> {
                 double mRate = Double.parseDouble(mutationRate .getValue()+"");
                 int pop = Integer.parseInt(populationSize .getValue()+"");
                 int chroLen = Integer.parseInt(chromosomeLength .getValue()+"");
                 int chroSize = Integer.parseInt(chromosomeSize .getValue()+"");
                 String dataSet;
                 if(radioBtn4.isSelected()) {
                    dataSet = radioBtn4.getText();
//                    lineGraph.setTitle("Pop size: " + populationSize .getValue() + ", Mutation: " + mutationRate .getValue() + ", Chromosome Size: " + chromosomeSize .getValue() + ", Total Generation: " + generatuinSize .getValue() + ", " +dataSet);
                    lineGraph.setTitle("Dataset 4");
                    progress.setMaximum(Integer.parseInt(generatuinSize .getValue()+""));
                    algrithm (mRate,pop,chroLen,chroSize,dataSet );
                 }
                 else if(radioBtn2.isSelected()) {
                    dataSet = radioBtn2.getText();
//                    lineGraph.setTitle("Pop size: " + populationSize .getValue() + ", Mutation: " + mutationRate .getValue() + ", Chromosome Size: " + chromosomeSize .getValue() + ", Total Generation: " + generatuinSize .getValue() + ", " +dataSet);
                    lineGraph.setTitle("Dataset 2");
                    algrithm (mRate,pop,chroLen,chroSize,dataSet );
                 }
                 else {
                    dataSet = radioBtn1.getText();
//                    lineGraph.setTitle("Pop size: " + populationSize .getValue() + ", Mutation: " + mutationRate .getValue() + ", Chromosome Size: " + chromosomeSize .getValue() + ", Total Generation: " + generatuinSize .getValue() + ", " +dataSet);
                    lineGraph.setTitle("Dataset 1");
                    progress.setMaximum(Integer.parseInt(generatuinSize .getValue()+""));
                    algrithm (mRate,pop,chroLen,chroSize,dataSet );
                 }
            });
        }
        
        private void frameSetup() {
            frame.setSize(800, 600);
            frame.setResizable(false);
            frame.setLayout(new BorderLayout());
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
            try { Thread.sleep(50); } catch (InterruptedException ex) {Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);}
            
            optionsPanel.setBackground(Color.WHITE);
            optionsPanel.setLayout(new GridBagLayout());
            frame.getContentPane().add(optionsPanel, BorderLayout.LINE_END);
            
            frame.add(chartPanel, BorderLayout.WEST);
            chartPanel.setLayout(new BorderLayout());
            
            
        }
        
        private void radioBtnSetup() {
            GridBagConstraints gbc = new GridBagConstraints();
            
            datasetsBtn.add(radioBtn1);
            datasetsBtn.add(radioBtn2);
            datasetsBtn.add(radioBtn4);

            radioBtn1.setBackground(Color.WHITE);
            radioBtn2.setBackground(Color.WHITE);
            radioBtn4.setBackground(Color.WHITE);
            
            gbc.gridx = 0;
            gbc.gridy = 0;
            gbc.insets = new Insets(10, 10, 15, 10);
            optionsPanel.add(radioBtn1, gbc);
            gbc.gridx = 1;
            gbc.gridy = 0;
            optionsPanel.add(radioBtn2, gbc);
            gbc.gridx = 2;
            gbc.gridy = 0;
            optionsPanel.add(radioBtn4, gbc);
        }
        
        private void chartSetup(String title){
            
            XYSeriesCollection dataCollection = new XYSeriesCollection();
            dataCollection.addSeries(best);
            dataCollection.addSeries(avrg);
            dataCollection.addSeries(worst);
            
            lineGraph = ChartFactory.createXYLineChart(title, "Number of Generations", "Fitness Values", dataCollection);
            
            chartPanel.add(new ChartPanel (lineGraph), BorderLayout.CENTER);
            
        }
        
        private void inputFeildSetup() {
            GridBagConstraints gbc = new GridBagConstraints();
            // dashbord text feilds 
            JLabel mutationLabel = new JLabel("Mutation Rate: ");
            JLabel populationLabel = new JLabel("Population Size: ");
            JLabel chromosomeLenLabel = new JLabel("Chromosome Length: ");
            JLabel chromosomeSizeLabel = new JLabel("Chromosome Size: ");
            JLabel genLabel = new JLabel("Number of Generation: ");

            nf.setOverwriteMode(true);
            
            gbc.insets = new Insets(10, 10, 10, 10);
            gbc.gridwidth = 2;
            gbc.fill = GridBagConstraints.HORIZONTAL;
            
            gbc.gridx = 0;
            gbc.gridy = 2;
            optionsPanel.add(mutationLabel, gbc);
            
            gbc.gridx = 0;
            gbc.gridy = 4;
            optionsPanel.add(populationLabel,gbc);
            
            gbc.gridx = 0;
            gbc.gridy = 6;
            optionsPanel.add(chromosomeLenLabel,gbc);
            
            gbc.gridx = 0;
            gbc.gridy = 8;
            optionsPanel.add(chromosomeSizeLabel,gbc);
            
            gbc.gridx = 0;
            gbc.gridy = 10;
            optionsPanel.add(genLabel,gbc);

            gbc.gridx = 2;
            gbc.gridy = 2;
            optionsPanel.add(mutationRate , gbc);
            
            gbc.gridx = 2;
            gbc.gridy = 4;
            optionsPanel.add(populationSize ,gbc);
            
            gbc.gridx = 2;
            gbc.gridy = 6;
            optionsPanel.add(chromosomeLength , gbc);
            
            gbc.gridx = 2;
            gbc.gridy = 8;
            optionsPanel.add(chromosomeSize , gbc);
            
            gbc.gridx = 2;
            gbc.gridy = 10;
            optionsPanel.add(generatuinSize , gbc);
        }
        
        private void progressBarSetup() {
            GridBagConstraints gbc = new GridBagConstraints();
            JLabel progressLable = new JLabel("Genetic Algorithm Progress: ");
            
            gbc.insets = new Insets(10, 10, 25, 10);
            gbc.gridx = 0;
            gbc.gridy = 14;
            gbc.gridwidth = 3;
            gbc.fill = GridBagConstraints.HORIZONTAL;
            progress.setMinimum(0);
            
            optionsPanel.add(progress, gbc);
            
            gbc.gridx = 0;
            gbc.gridy = 12;
            optionsPanel.add(progressLable,gbc);
        }
        
        private void runBtnSetup() {
            GridBagConstraints gbc = new GridBagConstraints();
            
            gbc.insets = new Insets(10, 10, 5, 10);
            gbc.fill = GridBagConstraints.HORIZONTAL;
            gbc.gridy = 16;
            gbc.gridx = 2;
            optionsPanel.add(runBtn, gbc);
            optionsPanel.repaint();
        }
        
        public void drawLine(int currentgenerations, int bestfitness, double avgfitness, int worstfitness) {
            best.add(currentgenerations, bestfitness);
            avrg.add(currentgenerations, avgfitness);
            worst.add(currentgenerations, worstfitness);
        }
        
        public void algrithm (double mutation, int Population, int chromosomeLen, int chromosomeSize, String file) {
            runBtn.setEnabled(false);
            Thread t = new Thread(){
                @Override
                public void run(){
                    Population x = new Population(mutation, Population, chromosomeLen, chromosomeSize);
                    
                    x.getDatasetData(file);
                    int current = 0;
                    while (current <= Integer.parseInt(generatuinSize .getValue()+"")) {
                        progress.setValue(current);
                        drawLine(current, x.getBestFitness(),x.getAverageFitness(),x.getWorstFitness());
                        x.selection();
                        x.fitnessFunction();
                        x.crossover();
                        x.mutation();
                        x.newGeneration();
                        current++;
                        System.out.println(current);
                    }
                    runBtn.setEnabled(true);
                }
            };
            t.start();
        }
    }
    
}
