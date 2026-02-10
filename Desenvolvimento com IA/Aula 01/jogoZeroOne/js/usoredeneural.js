import * from './redeneural.js';

// Exemplo de uso da rede neural
 const network = new NeuralNetwork();
  
 // Exemplo de entrada e saída desejada para treinamento
 const studyHours = 500;
 const sleepHours = 800;
 const testScore = 85;
 const targetGrade = 90;
 
 // Treinamento da rede neural
 network.train(studyHours, sleepHours, testScore, targetGrade);
 
 // Exemplo de entrada para previsão
 const newStudyHours = 600;
 const newSleepHours = 700;
 const newTestScore = 80;
 
 // Previsão da nota final
 const finalGrade = network.predictGrade(newStudyHours, newSleepHours, newTestScore);
 
 // Exibe a nota prevista
 console.log('Nota prevista no exame final: ${finalGrade.toFixed(2)}');