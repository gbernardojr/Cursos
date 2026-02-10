class NeuralNetwork {
    constructor() {
      // Inicializa a estrutura e os pesos da rede neural
      this.weights = [
        Math.random(), // Peso para a distância
        Math.random(), // Peso para a velocidade
        Math.random()  // Peso para a tamanho
      ];
    }
  
    predictAction(distance, speed, width) {
      // Calcula o valor de entrada da rede neural (soma ponderada das entradas com os pesos)
      const weightedSum = this.weights[0] * distance + this.weights[1] * speed + this.weights[2] * width;
  
      // Aplica uma função de ativação (opcional - depende da necessidade do problema)
  
      // Retorna a ação prevista (0 para não saltar, 1 para saltar)
      return weightedSum > 0 ? 1 : 0;
    }
  }
  
  // Exemplo de uso da rede neural com treinamento por reforço
  const network = new NeuralNetwork();
  
  // Função para simular o ambiente e obter as informações do obstáculo
  function getObstacleInformation() {
    // Simula a obtenção das informações do ambiente
    const distance = Math.random() * 10;  // Distância entre o agente e o obstáculo
    const speed = Math.random() * 5;     // Velocidade do obstáculo
    const width = Math.random() * 3;    // tamanho do obstáculo
  
    return { distance, speed, width };
  }
  
  // Função para realizar o treinamento da rede neural
  function trainNeuralNetwork(xdistance, xspeed, xwidth) {
    // Número de episódios de treinamento
    const numEpisodes = 100;
  
    for (let episode = 0; episode < numEpisodes; episode++) {
      // Reinicializa as informações do ambiente para cada episódio
      const { distance, speed, width } = { xdistance, xspeed, xwidth };
  
      // Obtém a ação prevista pela rede neural
      const predictedAction = network.predictAction(distance, speed, width);
  
      // Simula a execução da ação e obtém a recompensa
      const reward = simulateActionExecution(predictedAction, distance);
  
      // Atualiza os pesos da rede neural com base na recompensa
      updateWeights(predictedAction, reward);
    }
  
    console.log("Treinamento concluído!");
  }
  
  // Função para simular a execução da ação e obter a recompensa
  function simulateActionExecution(action, distance) {
    // Simula a execução da ação (exemplo simplificado)
    if (action === 1 && distance < 5) {
      return 1; // Recompensa positiva se saltar o obstáculo
    } else {
      return -1; // Recompensa negativa se não saltar o obstáculo
    }
  }
  
  // Função para atualizar os pesos da rede neural com base na recompensa
  function updateWeights(action, reward) {
    // Atualiza os pesos da rede neural com base na recompensa recebida (exemplo simplificado)
    if (action === 1 && reward === 1) {
      // Reforço positivo se saltar o obstáculo com sucesso, aumenta os pesos
      network.weights = network.weights.map(weight => weight + 0.1);
    } else if (action === 0 && reward === -1) {
      // Reforço negativo se não saltar o obstáculo, diminui os pesos
      network.weights = network.weights.map(weight => weight - 0.1);
    }
  }
  



  // Treina a rede neural
  trainNeuralNetwork();
  
  // Exemplo de uso da rede neural treinada
  const { distance, speed, width } = getObstacleInformation();
  const predictedAction = network.predictAction(distance, speed, width);
  
  console.log("Ação prevista:", predictedAction);
  