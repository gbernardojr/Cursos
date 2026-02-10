// Exemplo usando a biblioteca axios para fazer requisições HTTP
const axios = require('axios');

// Chave de API Alpha Vantage
const apiKey = 'SUA_CHAVE_DE_API';

// Função para obter o histórico de cotação da ação ITSA4 nos últimos 365 dias
async function getStockData() {
  try {
    // Faz a requisição HTTP para a API Alpha Vantage
    const response = await axios.get(
      `https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=ITSA4.SAO&outputsize=full&apikey=${apiKey}`
    );

    // Extrai os dados do histórico de cotação
    const stockData = response.data['Time Series (Daily)'];
    
    // Converte os dados para um array de objetos
    const stockArray = Object.entries(stockData).map(([date, data]) => ({
      date,
      open: parseFloat(data['1. open']),
      high: parseFloat(data['2. high']),
      low: parseFloat(data['3. low']),
      close: parseFloat(data['4. close']),
    }));

    // Retorna o histórico de cotação
    return stockArray;
  } catch (error) {
    console.error('Erro ao obter dados da API Alpha Vantage:', error.message);
    return null;
  }
}

// Função para criar e treinar um modelo de deep learning para prever o preço da ação
function trainModel(stockData) {
  // Implemente aqui o código para criar e treinar o modelo de deep learning usando os dados obtidos
  // Você pode usar bibliotecas como TensorFlow.js, Keras.js ou outra de sua preferência para isso
  // O código específico para o treinamento do modelo depende do framework escolhido

  // Exemplo simples de uso do TensorFlow.js:
  const tf = require('@tensorflow/tfjs');
  const { Sequential, layers } = require('@tensorflow/tfjs');

  // Preparar os dados
  const inputs = stockData.map(data => [data.open, data.high, data.low]);
  const targets = stockData.map(data => data.close);
  const tensorInputs = tf.tensor2d(inputs);
  const tensorTargets = tf.tensor1d(targets);

  // Criar o modelo
  const model = tf.sequential();
  model.add(layers.dense({ units: 10, inputShape: [3] }));
  model.add(layers.dense({ units: 1 }));

  // Compilar o modelo
  model.compile({ loss: 'meanSquaredError', optimizer: 'sgd' });

  // Treinar o modelo
  model.fit(tensorInputs, tensorTargets, { epochs: 50 });

  // Retornar o modelo treinado
  return model;
}

// Exemplo de uso:
async function runExample() {
  // Obter o histórico de cotação da ação ITSA4
  const stockData = await getStockData();

  if (stockData) {
    // Treinar o modelo de deep learning
    const model = trainModel(stockData);

    // Exemplo de previsão usando o modelo treinado
    const input = [[stockData[0].open, stockData[0].high, stockData[0].low]];
    const tensorInput = tf.tensor2d(input);
    const predictedPrice = model.predict(tensorInput).dataSync()[0];

    console.log('Preço previsto da ação ITSA4:', predictedPrice.toFixed(2));
  }
}

// Executar o exemplo
runExample();
