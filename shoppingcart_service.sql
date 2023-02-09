-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Dec 06, 2022 at 03:42 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shoppingcart_service`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('cd42e11c30d6');

-- --------------------------------------------------------

--
-- Table structure for table `cartitem`
--

CREATE TABLE `cartitem` (
  `id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `modified_at` datetime DEFAULT NULL,
  `product_id` int(11) NOT NULL,
  `shoppingcart_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cartitem`
--

INSERT INTO `cartitem` (`id`, `quantity`, `created_at`, `modified_at`, `product_id`, `shoppingcart_id`) VALUES
(41, 3, '2022-12-01 20:47:46', '2022-12-03 13:59:03', 1, 1),
(42, 1, '2022-12-01 20:47:50', NULL, 2, 1),
(43, 2, '2022-12-01 20:47:51', '2022-12-02 19:54:34', 3, 1),
(49, 1, '2022-12-03 09:38:41', NULL, 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `shoppingcart`
--

CREATE TABLE `shoppingcart` (
  `id` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `modified_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shoppingcart`
--

INSERT INTO `shoppingcart` (`id`, `created_at`, `modified_at`, `user_id`, `quantity`) VALUES
(1, '2022-11-22 09:41:43', '2022-12-01 20:44:28', 2, 6),
(4, '2022-12-03 09:38:40', '2022-12-03 09:39:25', 6, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `cartitem`
--
ALTER TABLE `cartitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `shoppingcart_id` (`shoppingcart_id`);

--
-- Indexes for table `shoppingcart`
--
ALTER TABLE `shoppingcart`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cartitem`
--
ALTER TABLE `cartitem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `shoppingcart`
--
ALTER TABLE `shoppingcart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cartitem`
--
ALTER TABLE `cartitem`
  ADD CONSTRAINT `cartitem_ibfk_1` FOREIGN KEY (`shoppingcart_id`) REFERENCES `shoppingcart` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
