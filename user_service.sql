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
-- Database: `user_service`
--

-- --------------------------------------------------------

--
-- Table structure for table `address`
--

CREATE TABLE `address` (
  `id` int(11) NOT NULL,
  `city` varchar(80) NOT NULL,
  `district` varchar(80) NOT NULL,
  `ward` varchar(80) NOT NULL,
  `road` varchar(80) NOT NULL,
  `created_at` datetime NOT NULL,
  `modified_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `address`
--

INSERT INTO `address` (`id`, `city`, `district`, `ward`, `road`, `created_at`, `modified_at`, `user_id`) VALUES
(1, 'Hồ Chí Minh', 'Bình Tân', 'Bình Trị Đông', '551/3 Hương Lộ 2', '2022-11-22 15:35:34', NULL, 2),
(2, 'Hồ Chí Minh', 'Bình Tân', 'Bình Trị Đông', '551/4 Hương Lộ 2', '2022-11-23 10:14:47', NULL, 2),
(3, 'Hồ Chí Minh', '7', 'Tân Phong', '211 Nguyễn Hữu Thọ', '2022-12-03 09:39:25', NULL, 6);

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
('6d47da4d2106');

-- --------------------------------------------------------

--
-- Table structure for table `otp`
--

CREATE TABLE `otp` (
  `id` varchar(6) NOT NULL,
  `expire_at` datetime NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `otp`
--

INSERT INTO `otp` (`id`, `expire_at`, `user_id`) VALUES
('033163', '2022-11-24 12:08:42', 2),
('240722', '2022-11-24 11:56:31', 2),
('344971', '2022-11-24 11:57:38', 2),
('953142', '2022-12-01 20:48:20', 2);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `role_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `role_name`) VALUES
(1, 'Admin'),
(2, 'User');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `fullname` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `create_at` datetime NOT NULL,
  `modified_at` datetime DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  `api_key` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `fullname`, `phone_number`, `email`, `username`, `password`, `create_at`, `modified_at`, `role_id`, `api_key`) VALUES
(1, 'Trần Ngọc Phát', '0912345678', 'phattran248vn@gmail.com', 'admin', '0192023a7bbd73250516f069df18b500', '2022-11-19 14:43:29', NULL, 1, '$5$rounds=535000$zHN9iDfimHRsvBnG$k9xqUJxFfw3vBu9SZSiDFxze9Eax2sKID3ib2JO6uL7'),
(2, 'Trần Ngọc Phát', '0932613346', 'phatngoctran2001vn@gmail.com', 'phat248vn', '16d7a4fca7442dda3ad93c9a726597e4', '2022-11-20 13:09:50', '2022-12-01 20:43:20', 2, '$5$rounds=535000$Tuxig1HmuthwZ7cW$t2t6hgw1cF.X2nS32kO/koU86/pvrwt0m4oUcgyi3XC'),
(6, 'Vũ Trọng Lâm Thanh', '0932613345', 'vutronglamthanh@gmail.com', 'thanh123', '893c3fd491f30b629fde7abe2ba1b516', '2022-12-03 09:38:32', NULL, 2, '$5$rounds=535000$PkiJexKaA.louE6a$iuGaZVlheLAzpn7JPsKJHH9s2uPjsKJdSzdqJDQtBw8');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `address`
--
ALTER TABLE `address`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `otp`
--
ALTER TABLE `otp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `api_key` (`api_key`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `address`
--
ALTER TABLE `address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `address`
--
ALTER TABLE `address`
  ADD CONSTRAINT `address_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `otp`
--
ALTER TABLE `otp`
  ADD CONSTRAINT `otp_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
