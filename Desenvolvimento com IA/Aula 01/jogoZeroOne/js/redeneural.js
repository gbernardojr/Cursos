class NeuralNetwork {
    constructor() {
      // Inicializa os pesos com valores aleatórios
      this.weights = [Math.random(), Math.random(), Math.random()];
      // Define a taxa de aprendizado
      this.learningRate = 0.1;
    }
  
    predictGrade(studyHours, sleepHours, testScore) {
      // Calcula a soma ponderada das entradas com os pesos
      const weightedSum = this.weights[0] * studyHours + this.weights[1] * sleepHours + this.weights[2] * testScore;
  
      // Aplica uma função de ativação (opcional - depende da necessidade do problema)
  
      // Retorna a nota prevista
      return weightedSum;
    }
  
    train(studyHours, sleepHours, testScore, targetGrade) {
      // Faz a previsão da nota final
      const predictedGrade = this.predictGrade(studyHours, sleepHours, testScore);
  
      // Calcula o erro
      const error = targetGrade - predictedGrade;
  
      // Atualiza os pesos usando o algoritmo de retropropagação
      for (let i = 0; i < this.weights.length; i++) {
        this.weights[i] += this.learningRate * error;
      }
  
      // Repete o processo de treinamento com mais exemplos e iterações (épocas) para melhorar o desempenho da rede
    }
  }
  
 
  