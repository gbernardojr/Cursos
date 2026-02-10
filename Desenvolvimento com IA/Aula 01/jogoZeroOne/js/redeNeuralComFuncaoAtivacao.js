class NeuralNetwork {
    constructor() {
      // Inicializa os pesos da rede neural
      this.weights = [
        Math.random(), // Peso para a distância
        Math.random(), // Peso para a velocidade
        Math.random()  // Peso para a altura
      ];
    }
  
    predictAction(distance, speed, height) {
      // Calcula o valor de entrada da rede neural (soma ponderada das entradas com os pesos)
      const weightedSum = this.weights[0] * distance + this.weights[1] * speed + this.weights[2] * height;
  
      // Aplica a função de ativação ReLU
      const activation = Math.max(0, weightedSum);
  
      // Retorna a ação prevista (0 para não saltar, 1 para saltar)
      return activation > 0 ? 1 : 0;
    }
  
    updateWeights(action, reward, distance, speed, height) {
      // Taxa de aprendizado
      const learningRate = 0.1;
  
      // Atualiza os pesos da rede neural com base na recompensa recebida e nos valores de entrada
      const delta = learningRate * reward;
      this.weights[0] += delta * distance;
      this.weights[1] += delta * speed;
      this.weights[2] += delta * height;
    }
  }
  
  // Simula a obtenção das informações do ambiente (distância, velocidade e altura do obstáculo)
  function getObstacleInformation() {
    const distance = Math.random() * 10;  // Distância entre o agente e o obstáculo
    const speed = Math.random() * 5;     // Velocidade do obstáculo
    const height = Math.random() * 3;    // Altura do obstáculo
  
    return { distance, speed, height };
  }
  
  // Simula a execução da ação e obtém a recompensa com base na distância e na ação tomada
  function simulateActionExecution(action, distance) {
    if (action === 1 && distance < 5) {
      return 1; // Recompensa positiva se saltar o obstáculo com sucesso
    } else {
      return -1; // Recompensa negativa se não saltar o obstáculo ou colidir com ele
    }
  }
  
  // Treinamento da rede neural com aprendizado por reforço
  function trainNeuralNetwork() {
    const network = new NeuralNetwork();
    const numEpisodes = 100;
  
    for (let episode = 0; episode < numEpisodes; episode++) {
      const { distance, speed, height } = getObstacleInformation();
      const action = network.predictAction(distance, speed, height);
      const reward = simulateActionExecution(action, distance);
      network.updateWeights(action, reward, distance, speed, height);
    }
  
    return network;
  }
  
  // Exemplo de uso da rede neural treinada
  function testNeuralNetwork(network) {
    const { distance, speed, height } = getObstacleInformation();
    const action = network.predictAction(distance, speed, height);
  
    console.log("Distância:", distance.toFixed(2));
    console.log("Velocidade:", speed.toFixed(2));
    console.log("Altura:", height.toFixed(2));
    console.log("Ação prevista:", action);
  }
  
  // Treina a rede neural
  const trainedNetwork = trainNeuralNetwork();
  
  // Testa a rede neural treinada
  testNeuralNetwork(trainedNetwork);
  