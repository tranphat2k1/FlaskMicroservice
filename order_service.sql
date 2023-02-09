-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Dec 06, 2022 at 03:43 AM
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
-- Database: `order_service`
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
('29faa698a25e');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `total` float NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime NOT NULL,
  `modified_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`id`, `total`, `status`, `created_at`, `modified_at`, `user_id`, `address_id`) VALUES
(6, 42660000, 'Đang chờ xác nhận', '2022-11-22 17:20:23', NULL, 2, 1),
(7, 30420000, 'Đang được chuẩn bị', '2022-11-23 10:14:47', NULL, 2, 2),
(14, 36720000, 'Đang chờ xác nhận', '2022-12-01 20:44:28', NULL, 2, 2),
(15, 23760000, 'Đang chờ xác nhận', '2022-12-03 09:39:25', NULL, 6, 3),
(16, 20000000, 'Đang chờ xác nhận', '2022-12-03 14:04:16', NULL, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `orderitem`
--

CREATE TABLE `orderitem` (
  `id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `modified_at` datetime DEFAULT NULL,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderitem`
--

INSERT INTO `orderitem` (`id`, `quantity`, `created_at`, `modified_at`, `order_id`, `product_id`) VALUES
(9, 1, '2022-11-22 17:20:23', NULL, 6, 4),
(10, 1, '2022-11-22 17:20:23', NULL, 6, 3),
(11, 2, '2022-11-23 10:14:47', NULL, 7, 2),
(12, 1, '2022-11-23 10:14:47', NULL, 7, 6),
(21, 2, '2022-12-01 20:44:28', NULL, 14, 3),
(22, 1, '2022-12-01 20:44:28', NULL, 14, 2),
(23, 1, '2022-12-03 09:39:25', NULL, 15, 3),
(24, 1, '2022-12-03 09:39:25', NULL, 15, 2),
(25, 2, '2022-12-03 14:07:12', NULL, 16, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orderitem`
--
ALTER TABLE `orderitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `orderitem`
--
ALTER TABLE `orderitem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orderitem`
--
ALTER TABLE `orderitem`
  ADD CONSTRAINT `orderitem_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
