// Parâmetros do algoritmo genético
const populationSize = 100; // Tamanho da população
const mutationRate = 0.1; // Taxa de mutação

// Função de ativação (sigmoid)
function sigmoid(x) {
  return 1 / (1 + Math.exp(-x));
}

// Classe da Rede Neural
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

    // Aplica a função de ativação sigmoidal
    const activation = sigmoid(weightedSum);

    // Retorna a ação prevista (0 para não pular, 1 para pular)
    return activation > 0.5 ? 1 : 0;
  }
}

// Função para criar uma população inicial de redes neurais
function createInitialPopulation(size) {
  const population = [];
  for (let i = 0; i < size; i++) {
    const network = new NeuralNetwork();
    population.push(network);
  }
  return population;
}

// Função para avaliar o desempenho de uma rede neural
function evaluateNetwork(network, obstacleData) {
  let fitness = 0;
  for (let data of obstacleData) {
    const { distance, speed, height, shouldJump } = data;
    const predictedAction = network.predictAction(distance, speed, height);
    if (predictedAction === shouldJump) {
      fitness++; // Incrementa a pontuação se a ação prevista for correta
    }
  }
  return fitness;
}

// Função para selecionar indivíduos para reprodução usando seleção por torneio
function tournamentSelection(population, obstacleData, tournamentSize) {
  let bestNetwork = null;
  let bestFitness = -1;
  for (let i = 0; i < tournamentSize; i++) {
    const network = population[Math.floor(Math.random() * population.length)];
    const fitness = evaluateNetwork(network, obstacleData);
    if (fitness > bestFitness) {
      bestFitness = fitness;
      bestNetwork = network;
    }
  }
  return bestNetwork;
}

// Função para realizar o crossover entre dois indivíduos (redes neurais)
function crossover(parentA, parentB) {
  const child = new NeuralNetwork();
  for (let i = 0; i < parentA.weights.length; i++) {
    // Crossover de um ponto
    if (Math.random() < 0.5) {
      child.weights[i] = parentA.weights[i];
    } else {
      child.weights[i] = parentB.weights[i];
    }
  }
  return child;
}

// Função para realizar a mutação em um indivíduo (rede neural)
function mutate(network, mutationRate) {
  for (let i = 0; i < network.weights.length; i++) {
    if (Math.random() < mutationRate) {
      // Adiciona um valor aleatório pequeno à mutação
      network.weights[i] += Math.random() * 0.2 - 0.1;
    }
  }
}

// Função para evoluir a população utilizando o algoritmo genético
function evolvePopulation(population, obstacleData, tournamentSize, mutationRate) {
  const newPopulation = [];

  // Elitismo: mantém o melhor indivíduo da população atual
  const bestNetwork = tournamentSelection(population, obstacleData, tournamentSize);
  newPopulation.push(bestNetwork);

  while (newPopulation.length < population.length) {
    // Seleção de pais
    const parentA = tournamentSelection(population, obstacleData, tournamentSize);
    const parentB = tournamentSelection(population, obstacleData, tournamentSize);

    // Crossover
    const child = crossover(parentA, parentB);

    // Mutação
    mutate(child, mutationRate);

    // Adiciona o filho à nova população
    newPopulation.push(child);
  }

  return newPopulation;
}

// Simulação do jogo com obstáculos e dados de treinamento
const obstacleData = [
  { distance: 0.5, speed: 0.8, height: 0.4, shouldJump: 1 },
  { distance: 0.3, speed: 0.6, height: 0.8, shouldJump: 0 },
  { distance: 0.8, speed: 0.2, height:```javascript
0.1, shouldJump: 1 },
  { distance: 0.7, speed: 0.9, height: 0.6, shouldJump: 1 },
  // Adicione mais dados de obstáculos e ações esperadas conforme necessário
];

// Configurações do algoritmo genético
const maxGenerations = 50; // Número máximo de gerações
const tournamentSize = 5; // Tamanho do torneio para seleção
const mutationRate = 0.1; // Taxa de mutação

// Criação da população inicial
let population = createInitialPopulation(populationSize);

// Loop das gerações
for (let generation = 1; generation <= maxGenerations; generation++) {
  console.log(`Generation ${generation}`);

  // Avaliação da população atual
  for (let network of population) {
    const fitness = evaluateNetwork(network, obstacleData);
    console.log(`Fitness: ${fitness}`);
  }

  // Evolução da população
  population = evolvePopulation(population, obstacleData, tournamentSize, mutationRate);
}

// Avaliação do melhor indivíduo
const bestNetwork = tournamentSelection(population, obstacleData, tournamentSize);
console.log('Melhor indivíduo:');
console.log(bestNetwork);
