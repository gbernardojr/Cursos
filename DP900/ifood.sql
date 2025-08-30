Create table cliente(
  cpf varchar(14) primary key,
  nome varchar(100),
  endereco varchar(100)
  email varchar(100)
  celular varchar(20)
);

Create table enderecos_entrega(
  codigoEndereco int identity(1,1) primary key,
  codigoCliente varchar(14),
  cep varchar(10),
  numero varchar(15),
  referencia varchar(255)
);

Create Table lanchonete(
  cnpj varchar(20) primary key,
  nomeLanchonete varchar(100),
  EnderecoCep varchar(10),
  site varchar(100),
  telefone varchar(20)
);

Create Table entregador(
  cpf varchar(14) primary key,
  nome varchar(100),
  transporte varchar(20),
  telefone varchar(20)
)

Create table cardapio(
  codigo int identity(1,1) primary key,
  cnpj varchar(20),
  nomeProduto varchar(50),
  tamanho varchar(50),
  preco decimal,
  descricao varchar (250),
  imagem varchar(100)
);

Create table pedidos(
  codigoPedido int identity(1,1) primary key,
  cpfCliente varchar(14),
  Data date,
  Hora time,
  codigoEntrega int,
  formaPagto varchar(20),
  taxaEntrega decimal,
  valorPedido decimal
  );

Create Detalhe_pedido(
  codigoDetalhe int identity(1,1) primary key,
  codigoPedido int,
  codigoCardapio int,
  Quantidade decimal,
  precounitario decimal,
  precoTotal decimal
);
