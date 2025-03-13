-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 13/03/2025 às 23:50
-- Versão do servidor: 8.3.0
-- Versão do PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `db_megabyte`
--
DROP DATABASE IF EXISTS `db_megabyte`;
CREATE DATABASE IF NOT EXISTS `db_megabyte` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `db_megabyte`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_categoria`
--

DROP TABLE IF EXISTS `tb_categoria`;
CREATE TABLE IF NOT EXISTS `tb_categoria` (
  `id_categoria` tinyint NOT NULL AUTO_INCREMENT,
  `ds_categoria` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `tb_categoria`
--

INSERT INTO `tb_categoria` (`id_categoria`, `ds_categoria`) VALUES
(1, 'HARDWARES'),
(2, 'PERIFÉRICOS'),
(3, 'MONITORES'),
(4, 'CADEIRAS GAMERS'),
(5, 'NOTEBOOKS');

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_fornecedor`
--

DROP TABLE IF EXISTS `tb_fornecedor`;
CREATE TABLE IF NOT EXISTS `tb_fornecedor` (
  `id_fornecedor` tinyint NOT NULL AUTO_INCREMENT,
  `nm_empresa` varchar(45) NOT NULL,
  `nr_cnpj` varchar(15) NOT NULL,
  `ds_endereco` varchar(100) NOT NULL,
  `nr_telefone` varchar(15) NOT NULL,
  `id_usuario` tinyint NOT NULL,
  PRIMARY KEY (`id_fornecedor`),
  KEY `fk_fornecedor_usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `tb_fornecedor`
--

INSERT INTO `tb_fornecedor` (`id_fornecedor`, `nm_empresa`, `nr_cnpj`, `ds_endereco`, `nr_telefone`, `id_usuario`) VALUES
(1, 'Nvidia', '123.456/0001-78', '2788 San Tomas Expy, Santa Clara, CA 95051, Estados Unidos', '(47)98765-4321', 1),
(2, 'Logitech', '987.654/0002-32', 'Rte Cantonale, 1015 Ecublens, Suíça', '(21)863-5511', 1),
(3, 'Micro-Star International', '456.987/0003-45', 'No. 69, Lide St, Zhonghe District, New Taipei City, Taiwan 235', '(62)3234-5599', 1),
(4, 'Razer', '951.357/0004-65', '9-1, 9 Pasteur # 100, Irvine, CA 92618, Estados Unidos', '(19)49655-8888', 1),
(5, 'Serjao Livraria', '123.456/7890-00', 'Rua da Alegria', '4712344567', 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_produto`
--

DROP TABLE IF EXISTS `tb_produto`;
CREATE TABLE IF NOT EXISTS `tb_produto` (
  `cd_produto` tinyint NOT NULL,
  `ds_produto` varchar(45) NOT NULL,
  `vl_produto` decimal(8,2) NOT NULL,
  `qt_produto` smallint NOT NULL,
  `id_subcategoria` tinyint NOT NULL,
  `id_fornecedor` tinyint NOT NULL,
  `id_usuario` tinyint NOT NULL,
  PRIMARY KEY (`cd_produto`),
  KEY `fk_produto_subcategoria` (`id_subcategoria`),
  KEY `fk_produto_fornecedor` (`id_fornecedor`),
  KEY `fk_produto_usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `tb_produto`
--

INSERT INTO `tb_produto` (`cd_produto`, `ds_produto`, `vl_produto`, `qt_produto`, `id_subcategoria`, `id_fornecedor`, `id_usuario`) VALUES
(1, 'Galax GeForce GTX 1650', 849.99, 500, 1, 1, 1),
(2, 'PNY GeForce RTX 6000', 52599.99, 1, 1, 1, 1),
(3, 'Mouse Gamer Logitech G Pro 2', 719.99, 10, 2, 2, 1),
(4, 'Mouse Logitech Pebble 2', 114.99, 50, 2, 2, 1),
(5, 'Monitor Gamer MSI MAG401QR', 3299.99, 5, 3, 3, 1),
(6, 'Monitor Gamer MSI MAG345CQR', 2699.99, 5, 3, 3, 1),
(7, 'Teclado Optico Razer Huntsman V2 Tenkeyless', 999.99, 24, 4, 4, 1),
(8, 'Teclado Mecanico Razer Blackwidow V4', 1999.99, 16, 4, 4, 1),
(9, 'Livro Python', 158.00, 15, 5, 5, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_subcategoria`
--

DROP TABLE IF EXISTS `tb_subcategoria`;
CREATE TABLE IF NOT EXISTS `tb_subcategoria` (
  `id_subcategoria` tinyint NOT NULL AUTO_INCREMENT,
  `ds_subcategoria` varchar(45) NOT NULL,
  `id_categoria` tinyint NOT NULL,
  `id_usuario` tinyint NOT NULL,
  PRIMARY KEY (`id_subcategoria`),
  KEY `fk_subcategoria_categoria` (`id_categoria`),
  KEY `fk_subcategoria_usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `tb_subcategoria`
--

INSERT INTO `tb_subcategoria` (`id_subcategoria`, `ds_subcategoria`, `id_categoria`, `id_usuario`) VALUES
(1, 'Placa de video', 1, 1),
(2, 'Mouse', 2, 1),
(3, 'Ultrawide', 3, 1),
(4, 'Teclado', 2, 1),
(5, 'Livros', 2, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_usuario`
--

DROP TABLE IF EXISTS `tb_usuario`;
CREATE TABLE IF NOT EXISTS `tb_usuario` (
  `id_usuario` tinyint NOT NULL AUTO_INCREMENT,
  `nm_usuario` varchar(45) NOT NULL,
  `nr_cpf` varchar(14) NOT NULL,
  `nr_telefone` varchar(15) NOT NULL,
  `ds_perfil` enum('admin','padrao') NOT NULL,
  `ds_email` varchar(100) NOT NULL,
  `ds_senha` varchar(45) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `tb_usuario`
--

INSERT INTO `tb_usuario` (`id_usuario`, `nm_usuario`, `nr_cpf`, `nr_telefone`, `ds_perfil`, `ds_email`, `ds_senha`) VALUES
(1, 'admin', '000.000.000-00', '(00)00000-0000', 'admin', 'admin@admin', 'admin'),
(2, 'Gabriel', '123.456.789-00', '(47)98765-4321', 'padrao', 'gabriel@gabriel', '123');

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `tb_fornecedor`
--
ALTER TABLE `tb_fornecedor`
  ADD CONSTRAINT `fk_fornecedor_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuario` (`id_usuario`);

--
-- Restrições para tabelas `tb_produto`
--
ALTER TABLE `tb_produto`
  ADD CONSTRAINT `fk_produto_fornecedor` FOREIGN KEY (`id_fornecedor`) REFERENCES `tb_fornecedor` (`id_fornecedor`),
  ADD CONSTRAINT `fk_produto_subcategoria` FOREIGN KEY (`id_subcategoria`) REFERENCES `tb_subcategoria` (`id_subcategoria`),
  ADD CONSTRAINT `fk_produto_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuario` (`id_usuario`);

--
-- Restrições para tabelas `tb_subcategoria`
--
ALTER TABLE `tb_subcategoria`
  ADD CONSTRAINT `fk_subcategoria_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `tb_categoria` (`id_categoria`),
  ADD CONSTRAINT `fk_subcategoria_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuario` (`id_usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
