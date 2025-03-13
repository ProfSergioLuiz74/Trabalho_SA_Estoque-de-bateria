Banco de dados: `trabalho_sa`

CREATE DATABASE trabalho_sa

-- Estrutura para tabela `fornecedor`

CREATE TABLE `fornecedor` (
  `idfornecedor` int(11) NOT NULL,
  `fornecedores` text DEFAULT NULL,
  `cpf` text DEFAULT NULL,
  `telefone` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `endereco` text DEFAULT NULL,
  `produto` text DEFAULT NULL,
  `quantidade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estrutura para tabela `funcionario`

CREATE TABLE `funcionario` (
  `idfuncionario` int(11) NOT NULL,
  `nome` text DEFAULT NULL,
  `cpf` text NOT NULL,
  `telefone` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `cargo` text DEFAULT NULL,
  `salario` text DEFAULT NULL,
  `cidade` text DEFAULT NULL,
  `bairro` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estrutura para tabela `produto`

CREATE TABLE `produto` (
  `idproduto` int(11) NOT NULL,
  `tipo` text DEFAULT NULL,
  `voltagem` text DEFAULT NULL,
  `marca` text DEFAULT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `preco` text DEFAULT NULL,
  `data` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estrutura para tabela `usuario`

CREATE TABLE `usuario` (
  `idusuario` int(11) NOT NULL,
  `usuario` text DEFAULT NULL,
  `senha` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;