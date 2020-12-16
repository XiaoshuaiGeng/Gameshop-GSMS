-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 17, 2020 at 03:28 AM
-- Server version: 10.0.38-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gamestop`
--

-- --------------------------------------------------------

--
-- Table structure for table `Bought_Games`
--

CREATE TABLE `Bought_Games` (
  `customer_id` int(11) NOT NULL,
  `store_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `purchaseDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Bought_Games`
--

INSERT INTO `Bought_Games` (`customer_id`, `store_id`, `game_id`, `purchaseDate`) VALUES
(2, 2, 4, '2020-10-13 20:58:01'),
(1, 1, 3, '2020-10-08 14:37:31'),
(1, 2, 3, '2020-10-15 22:48:57');

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `customer_id` int(11) NOT NULL,
  `fname` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `lname` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`customer_id`, `fname`, `lname`, `address`) VALUES
(1, 'Tom', 'James', '234 Ave, Windsor, ON'),
(2, 'Rick', 'Bus', '123 Street, London, ON'),
(4, 'xiaoshuai', 'geng', 'Windsor'),
(5, 'Sam', 'Fisher', 'London');

-- --------------------------------------------------------

--
-- Table structure for table `Customer_Membership`
--

CREATE TABLE `Customer_Membership` (
  `membership_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Customer_Membership`
--

INSERT INTO `Customer_Membership` (`membership_id`, `customer_id`) VALUES
(1, 2),
(3, 1),
(1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `Developer`
--

CREATE TABLE `Developer` (
  `developer_id` int(11) NOT NULL,
  `developer_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Developer`
--

INSERT INTO `Developer` (`developer_id`, `developer_name`, `address`) VALUES
(1, ' Bethesda Game Studios', 'Rockville, Maryland, United States'),
(2, 'Phobia Game Studio', ' Austin, Texas, United States'),
(3, 'Ubisoft Quebec, Ubisoft Montreal,', ' Montreuil, France'),
(4, 'Re-Logic', 'Unknown'),
(5, 'Klei Entertainment', 'Vancouver'),
(9, 'NO STUDIO', 'Windsor');

-- --------------------------------------------------------

--
-- Table structure for table `Game`
--

CREATE TABLE `Game` (
  `game_id` int(11) NOT NULL,
  `game_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `release_date` date NOT NULL,
  `genre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `platform` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `price` double(10,2) NOT NULL,
  `availability` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Game`
--

INSERT INTO `Game` (`game_id`, `game_name`, `release_date`, `genre`, `platform`, `price`, `availability`) VALUES
(2, 'CARRION', '2020-07-23', 'Action,Indie,Villain Protagonist', 'PC', 12.99, ''),
(3, 'Assassin\'s Creed® Odyssey', '2018-08-05', 'Open World, RPG, Assassin', 'PC/PlayStation', 79.99, ''),
(4, 'Terraria', '2011-05-16', 'Open World Survival Craft, Sandbox,Survival', 'PC/Mobile', 10.99, ''),
(22, 'Fallout 4', '2014-05-06', 'Open World, Post-apocalypse', 'Xbox', 25.99, 'Not Available'),
(23, 'Metro Exodus', '2020-11-16', 'Post Apocalypse, FPS', 'PC', 59.99, 'Available'),
(27, 'Cyberpunk', '2020-12-10', 'Open World, RPG', 'PC/XBOX/PS', 79.99, 'Not available');

-- --------------------------------------------------------

--
-- Table structure for table `Has_Games`
--

CREATE TABLE `Has_Games` (
  `store_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `num_of_copies` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Has_Games`
--

INSERT INTO `Has_Games` (`store_id`, `game_id`, `num_of_copies`) VALUES
(1, 4, 20),
(2, 4, 13),
(2, 3, 15),
(1, 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `Membership`
--

CREATE TABLE `Membership` (
  `membership_id` int(11) NOT NULL,
  `membership_type` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Membership`
--

INSERT INTO `Membership` (`membership_id`, `membership_type`) VALUES
(1, 'Silver'),
(2, 'Gold'),
(3, 'Platinum');

-- --------------------------------------------------------

--
-- Table structure for table `Published_Games`
--

CREATE TABLE `Published_Games` (
  `developer_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Published_Games`
--

INSERT INTO `Published_Games` (`developer_id`, `game_id`) VALUES
(3, 3),
(2, 2),
(4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `Store`
--

CREATE TABLE `Store` (
  `store_id` int(11) NOT NULL,
  `store_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Store`
--

INSERT INTO `Store` (`store_id`, `store_name`, `address`) VALUES
(1, 'GameStation - ABC', '567 ABC Ave, London, ON'),
(2, 'GameStation - Windsor', '152 Street, Windsor, ON'),
(7, 'Game Store - London', '256 Ave, London, ON');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Bought_Games`
--
ALTER TABLE `Bought_Games`
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `game_id` (`game_id`),
  ADD KEY `store_id` (`store_id`);

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `Customer_Membership`
--
ALTER TABLE `Customer_Membership`
  ADD KEY `membership_id` (`membership_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `Developer`
--
ALTER TABLE `Developer`
  ADD PRIMARY KEY (`developer_id`);

--
-- Indexes for table `Game`
--
ALTER TABLE `Game`
  ADD PRIMARY KEY (`game_id`);

--
-- Indexes for table `Has_Games`
--
ALTER TABLE `Has_Games`
  ADD KEY `game_id` (`game_id`),
  ADD KEY `store_id` (`store_id`) USING BTREE;

--
-- Indexes for table `Membership`
--
ALTER TABLE `Membership`
  ADD PRIMARY KEY (`membership_id`);

--
-- Indexes for table `Published_Games`
--
ALTER TABLE `Published_Games`
  ADD KEY `developer_id` (`developer_id`),
  ADD KEY `game_id` (`game_id`);

--
-- Indexes for table `Store`
--
ALTER TABLE `Store`
  ADD PRIMARY KEY (`store_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Customer`
--
ALTER TABLE `Customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `Developer`
--
ALTER TABLE `Developer`
  MODIFY `developer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `Game`
--
ALTER TABLE `Game`
  MODIFY `game_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `Membership`
--
ALTER TABLE `Membership`
  MODIFY `membership_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Store`
--
ALTER TABLE `Store`
  MODIFY `store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Bought_Games`
--
ALTER TABLE `Bought_Games`
  ADD CONSTRAINT `Bought_Games_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `Customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Bought_Games_ibfk_2` FOREIGN KEY (`game_id`) REFERENCES `Game` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Bought_Games_ibfk_3` FOREIGN KEY (`store_id`) REFERENCES `Store` (`store_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Customer_Membership`
--
ALTER TABLE `Customer_Membership`
  ADD CONSTRAINT `Customer_Membership_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `Customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Customer_Membership_ibfk_2` FOREIGN KEY (`membership_id`) REFERENCES `Membership` (`membership_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Has_Games`
--
ALTER TABLE `Has_Games`
  ADD CONSTRAINT `Has_Games_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `Game` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Has_Games_ibfk_2` FOREIGN KEY (`store_id`) REFERENCES `Store` (`store_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Published_Games`
--
ALTER TABLE `Published_Games`
  ADD CONSTRAINT `Published_Games_ibfk_1` FOREIGN KEY (`developer_id`) REFERENCES `Developer` (`developer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Published_Games_ibfk_2` FOREIGN KEY (`game_id`) REFERENCES `Game` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
