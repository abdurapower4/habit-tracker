-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 19, 2023 at 07:51 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `TaskTracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `Schedule`
--

CREATE TABLE `Schedule` (
  `id` int(11) NOT NULL,
  `Task` int(11) NOT NULL,
  `Monday` varchar(100) DEFAULT NULL,
  `Tuesday` varchar(100) DEFAULT NULL,
  `Wednesday` varchar(100) DEFAULT NULL,
  `Thursday` varchar(100) DEFAULT NULL,
  `Friday` varchar(100) DEFAULT NULL,
  `Saturday` varchar(100) DEFAULT NULL,
  `Sunday` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Schedule`
--

INSERT INTO `Schedule` (`id`, `Task`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`) VALUES
(1, 12, NULL, NULL, NULL, NULL, NULL, NULL, 'Checked-Off'),
(2, 15, NULL, NULL, NULL, NULL, NULL, NULL, 'Checked-Off'),
(3, 16, NULL, NULL, NULL, NULL, NULL, NULL, 'Checked-Off'),
(4, 17, NULL, NULL, NULL, NULL, NULL, NULL, 'Checked-Off');

-- --------------------------------------------------------

--
-- Table structure for table `Tasks`
--

CREATE TABLE `Tasks` (
  `id` int(11) NOT NULL,
  `Task` varchar(400) NOT NULL,
  `Status` varchar(100) NOT NULL DEFAULT 'Active',
  `Days` varchar(1000) NOT NULL,
  `is_on_track` varchar(100) NOT NULL DEFAULT 'Yes',
  `dateAdded` datetime NOT NULL DEFAULT current_timestamp(),
  `dateCompleted` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Tasks`
--

INSERT INTO `Tasks` (`id`, `Task`, `Status`, `Days`, `is_on_track`, `dateAdded`, `dateCompleted`) VALUES
(10, 'Wash Dishes', 'Active', 'Weekly', 'Yes', '2023-02-19 13:55:21', NULL),
(11, 'Shower', 'Checked-Off', 'Weekly', 'Yes', '2023-02-19 14:13:34', NULL),
(12, 'Watch Football', 'Checked-Off', 'Tuesday', 'Yes', '2023-02-19 14:14:17', NULL),
(14, 'Last', 'Checked-Off', 'Tuesday', 'Yes', '2023-02-19 14:58:52', NULL),
(15, 'Football', 'Checked-Off', 'Weekly', 'Yes', '2023-02-19 15:58:16', NULL),
(16, 'Test 34', 'Checked-Off', 'Monday', 'No', '2023-02-19 17:09:27', NULL),
(17, 'Popcorns', 'Checked-Off', 'Sunday', 'Yes', '2023-02-19 17:20:16', '2023-02-19 17:20:32.957939'),
(18, 'Test task1', 'Active', 'Monday', 'Yes', '2023-02-19 19:06:59', NULL),
(19, 'Test task1', 'Active', 'Monday', 'Yes', '2023-02-19 19:10:07', NULL),
(20, 'Test task1', 'Active', 'Monday', 'Yes', '2023-02-19 19:10:54', NULL),
(21, 'Test task1', 'Active', 'Monday', 'Yes', '2023-02-19 19:11:42', NULL),
(22, 'Test task1', 'Active', 'Monday', 'Yes', '2023-02-19 21:35:08', NULL),
(23, 'Test task1', 'Active', 'Monday', 'Yes', '2023-02-19 21:48:02', NULL),
(24, 'Test task1', 'Active', 'Monday', 'Yes', '2023-02-19 21:50:37', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Schedule`
--
ALTER TABLE `Schedule`
  ADD PRIMARY KEY (`id`),
  ADD KEY `task` (`Task`);

--
-- Indexes for table `Tasks`
--
ALTER TABLE `Tasks`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Schedule`
--
ALTER TABLE `Schedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Tasks`
--
ALTER TABLE `Tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Schedule`
--
ALTER TABLE `Schedule`
  ADD CONSTRAINT `task` FOREIGN KEY (`Task`) REFERENCES `Tasks` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
