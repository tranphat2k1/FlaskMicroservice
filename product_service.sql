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
-- Database: `product_service`
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
('cab68f39535a');

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `created_at` datetime NOT NULL,
  `modified_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`id`, `name`, `created_at`, `modified_at`) VALUES
(1, 'Bentley', '2022-11-20 09:52:47', '2022-11-24 13:30:03'),
(2, 'Orient', '2022-11-20 09:52:47', NULL),
(3, 'Ogival', '2022-11-20 09:53:17', NULL),
(4, 'Edox', '2022-11-20 09:53:17', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `price` float NOT NULL,
  `discount` int(11) DEFAULT NULL,
  `stock` int(11) NOT NULL,
  `desc` text NOT NULL,
  `created_at` datetime NOT NULL,
  `modified_at` datetime DEFAULT NULL,
  `brand_id` int(11) NOT NULL,
  `image` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`, `price`, `discount`, `stock`, `desc`, `created_at`, `modified_at`, `brand_id`, `image`) VALUES
(1, 'Bentley BL1784-252KBB-S2', 10000000, 20, 114, 'Chiếc đồng hồ G-SHOCK phủ kim loại màu vàng và đen vốn được ưa chuộng. Thiết kế đường gờ kim loại mạ ion vàng trên nền đen vô cùng sành điệu. Chiếc đồng hồ nổi bật về phong cách thời trang cùng diện mạo sang trọng và sành điệu đưa bạn đến nơi bạn cần đến.', '2022-11-20 09:53:39', '2022-12-03 14:07:12', 1, 'Bentley-BL1784-252KBB-S2-1000x100-3.jpg'),
(2, 'Orient SUN and MOON Gen 4 2021 RA-AS0009S10B', 12000000, 10, 117, 'Orient SUN and MOON Gen 4 2021 RA-AS0009S10B là phiên bản cập nhật mới nhất của dòng Gen 4 trứ danh. Một dòng sản phẩm đã làm nên tên tuổi của Orient Nhật Bản, nổi tiếng bền bỉ với chất lượng vượt trội nằm trong Seri sưu tập Sun & Moon. Orient SUN and MOON Gen 4 2021 RA-AS0009S10B có sự cải tiến tinh tế so với người đàn anh trước đó và luôn là một sản phẩm nổi trội của Orient, là hiện thân của sự đẳng cấp, lịch lãm và sang trọng mang lại sự thích thú và cuốn hút cho các quý ông.', '2022-11-20 09:53:39', '2022-12-03 09:39:25', 2, 'Orient-SUN-and-MOON-Gen-4-2021-RA-AS0009S10B.jpg'),
(3, 'Ogival OG1929-24AGK-T', 14400000, 10, 206, 'Đồng hồ Ogival OG1929-24AGK-T ( Ogival cá nhảy ) là đồng hồ thương hiệu Thụy Sĩ. Ogival cá nhảy phiên bản Classic Demi Gold đỉnh cao của sự tối giản với màu vàng truyền thống là biểu tượng của tình yêu và khát vọng thành công, là  mẫu đồng hồ tinh tế, sang trọng được thiết kế tinh xảo, độ bền bỉ là thượng thừa. Hình ảnh cá nhảy không những đem lại tài lộc, công danh mà còn là may mắn, thuận buồm xuôi gió trong công việc và cuộc sống', '2022-11-20 09:55:39', '2022-12-03 09:39:25', 3, 'Ogival-OG1929-24AGK-T-2.jpg'),
(4, 'Edox 83015-37R-BUIR', 33000000, 10, 20, 'Edox 83015-37R-BUIR là dòng sản phẩm đỉnh cao chế tác đồng hồ Thụy Sĩ đến từ nhà Edox. Mang lại cảm hứng mãnh liệt, những trải nghiệm không thể nào quên khi đeo chiếc đồng hồ trên tay.', '2022-11-20 09:55:39', NULL, 4, 'edox-83015-37r-buir-1_1.jpg'),
(5, 'Bentley BL2096-152KBI-S', 13600000, 10, 70, 'Bentley BL2096-152KBI-S là mẫu đồng hồ cơ mới nhất hiện nay, xuất xứ thương hiệu đồng hồ của Đức nổi tiếng hàng đầu về sự chính xác và bền bỉ trong nghệ thuật chế tác đồng hồ. Nổi bật với 30 viên kim cương ( 12 viên tại cọc số, 18 viên còn lại được trải khắp đường viền của mặt phụ small second) và > 400 viên đá sapphire đầy sang trọng với độ tinh xảo cao mang tới phong cách sang trọng quý tộc và thanh lịch.', '2022-11-20 09:57:17', NULL, 1, 'Bentley-BL2096-152KBI-S.jpg'),
(6, 'Orient SUN and MOON Gen 3 SAK00005D0', 9800000, 10, 100, 'Orient SUN and MOON Gen 3 SAK00005D0 là một thương hiệu đồng hồ Nhật Bản nổi tiếng bền bỉ với chất lượng vượt trội nằm trong Seri sưu tập Sun & Moon. Orient SUN and MOON Gen 3 SAK00005D0 có sự cải tiến tinh tế so với người đàn anh trước đó và luôn là một sản phẩm nổi trội của Orient, là hiện thân của sự đẳng cấp, lịch lãm và sang trọng mang lại sự thích thú và cuốn hút cho các quý ông.', '2022-11-20 09:57:17', NULL, 2, 'Orient-SUN-and-MOON-Gen-3-SAK00005D0-1.jpg'),
(7, 'Orient SK RA-AA0B03L19B', 6300000, 0, 200, 'Đồng hồ Orient SK RA-AA0B03L19B là một thương hiệu đồng hồ Nhật Bản nổi tiếng bền bỉ với chất lượng vượt trội, sản phẩm là đánh dấu sự trở lại của một huyền thoại mang tên SK mặt lửa khi trước đó được biết tới năm 1970 – mệnh danh gọi là Sea King, là hiện thân của sự đẳng cấp, mạnh mẽ và sang trọng mang lại sự thích thú và cuốn hút cho các quý ông. Đồng Hồ Tuấn Hưng là đơn vị phân phối chính hãng dòng sản phẩm đồng hồ thương hiệu Orient', '2022-11-20 09:58:41', NULL, 2, 'Orient-SK-RA-AA0B03L19B-shop_1.jpg'),
(8, 'Ogival OG358.88AGR-GL', 27200000, 0, 70, 'Đồng hồ Ogival OG358.88AGR-GL ( Bát mã truy phong ) là đồng hồ thương hiệu Thụy Sĩ. Ogival bát mã truy theo phong thủy hàm nghĩa nói đến hình ảnh 8 con ngựa ( tuấn mã ) mạnh khỏe phi nhanh như gió, mang ý nghĩa biểu thị sức mạnh, ý chí quyết tâm sắt đá, một khát vọng thành công cùng chung một chí hướng (8 chú ngựa cùng tiến về một hướng), đồng lòng tiến lên phía trước để đem chiến thắng trở về , thịnh vượng, thành đạt và thắng lợi.', '2022-11-20 09:58:41', NULL, 3, 'Ogival-OG358.88AGR-GL-Bat-Ma-Truy-Phong-v.jpg'),
(9, 'Edox 80117-3M-NIN', 15500000, 10, 178, 'Edox 80117-3M-NIN là thương hiệu đồng hồ Thụy Sĩ lâu đời, danh tiếng với thiết kế sáng tạo vô cùng hiện đại, quy trình sản xuất hoàn hảo, sở hữu vẻ đẹp thời thượng, sự mạnh mẽ, chính xác của bộ máy. Đặc biệt nổi bật với những sản phẩm theo xu hướng người dùng tạo nên sự khỏe khoắn, mạnh mẽ, chính xác, bền bỉ ở mức cao.', '2022-11-20 09:59:58', NULL, 4, 'Edox-80117-3M-NIN-402-2.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `brand_id` (`brand_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `brand`
--
ALTER TABLE `brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
