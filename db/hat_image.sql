-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 17, 2020 at 07:17 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `hat_image`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `utype`, `status`) VALUES
('shyam', 'sa', 'user', 'pending'),
('Drisya v', 'sa', 'user', 'pending'),
('ff', 'a', 'user', 'pending'),
('admin', 'admin', 'admin', 'approved'),
('riu', 'r', 'user', 'pending'),
('amrutha', '3010', 'user', 'pending'),
('devu', '123', 'user', 'pending'),
('nisari', '147', 'user', 'pending'),
('nisari', '2211', 'user', 'pending'),
('riya', 'roshan', 'user', 'pending'),
('appu', 'xyz', 'user', 'pending'),
('shaji', '11219', 'user', 'pending'),
('vindhya', '789', 'user', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE IF NOT EXISTS `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `frommail` varchar(50) NOT NULL,
  `tomail` varchar(50) NOT NULL,
  `sub` varchar(50) NOT NULL,
  `msg` varchar(150) NOT NULL,
  `date` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  `password` varchar(50) NOT NULL,
  `path` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=33 ;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`id`, `frommail`, `tomail`, `sub`, `msg`, `date`, `status`, `password`, `path`) VALUES
(20, 'devu', 'shyam', 'haha', 'face book image', '2019-12-30 16:55:30.626644', 'sent', '123', 'static/media/price1.jpg'),
(21, 'shyam', 'devu', 'facebook image', 'gmail password', '2019-12-30 16:57:50.638489', 'sent', '123', 'static/media/blog2.jpg'),
(22, 'devu', 'amrutha', 'asdf', 'create a password', '2019-12-30 17:22:23.860492', 'sent', '147', 'static/media/bg4.jpg'),
(23, 'amrutha', 'devu', 'kuiii', 'hello ', '2019-12-30 17:25:08.861192', 'sent', '125', 'static/media/blog3_M7FgEXb.jpg'),
(24, 'devu', 'amrutha', 'hoo', 'how are you', '2019-12-30 17:30:29.684339', 'sent', '523', 'static/media/bg4_zGbdYgz.jpg'),
(25, 'amrutha', 'devu', 'kuiii', 'hello hello', '2019-12-31 13:24:15.326183', 'sent', '147', 'static/media/blog3_7AaO7ni.jpg'),
(26, 'amrutha', 'devu', 'kuiii', 'hello', '2019-12-31 13:25:41.451851', 'sent', '147', 'static/media/blog2_AFfivCu.jpg'),
(27, 'nisari', 'amrutha', 'hloo', 'hi appi ninakk sugamanoo', '2019-12-31 13:35:51.701123', 'sent', '2425', 'static/media/4.jpg'),
(28, 'riya', 'riya', 'ooiiii', 'abcd', '2020-01-11 15:54:25.091385', 'sent', 'roshan', 'static/media/5.jpg'),
(29, 'amrutha', 'devu', 'hello', 'hello how are you', '2020-01-16 13:04:48.681889', 'sent', '456', 'static/media/20190223_071552.jpg'),
(30, 'appu', 'devu', 'qwerty', 'asdfghjkl', '2020-01-16 13:21:46.744316', 'sent', 'xyz', 'static/media/20190207_180335.jpg'),
(31, 'shaji', 'shaji@gmail.com', 'i love u', 'twinkle twinkle little star\r\nhow are wonder what you want', '2020-01-16 13:28:05.620666', 'sent', '11219', 'static/media/5_P2aWYvs.jpg'),
(32, 'shaji', 'vindhya', 'haiiii', 'twinkle twinkle little star', '2020-01-16 13:31:15.163661', 'sent', '789', 'static/media/5_FXNz5oA.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `userreg`
--

CREATE TABLE IF NOT EXISTS `userreg` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  `email` varchar(50) NOT NULL,
  `number` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `userreg`
--

INSERT INTO `userreg` (`uid`, `name`, `address`, `email`, `number`, `gender`, `dob`, `username`) VALUES
(2, 'shyam', 'qsf', 'shyamsasi94@gmail.com', '9633710717', 'Male', '2019-02-19', 'shyam'),
(3, 'Drisya v', 'edaghf', 'periyar@vpr.com', '7896541230', 'Female', '2019-03-08', 'Drisya v'),
(4, 'shyam', '4jedfb4', 'periyar@vpr.com', '9633710717', 'Male', '2019-01-31', 'ff'),
(5, 'riya', 'oajskjd', 'riyar@gmail.com', '7896541230', 'Female', '1998-12-11', 'riu'),
(6, 'Amrutha', 'Ushabhavanam,chathiyara,thamarakulam p.o', 'amrutha30101999@gmail.co', '7561028948', 'Female', '1999-10-30', 'amrutha'),
(7, 'Devika', 'Devikalayam\r\nkottayam\r\nkottayam p.o', 'devika567@gmail.com', '7523908676', 'Female', '1998-10-30', 'devu'),
(8, 'nisari', 'dfjuyggfhiub\r\nujoioilk\r\njhi', 'nisari@gmail.com', '546789245', 'Female', '1996-02-24', 'nisari'),
(9, 'nisari', 'dfgyhuikjfdf\r\ngjhkhfgdg\r\nddggjhi', 'nisarysasok@gmail.com', '07034470959', 'Female', '1996-02-24', 'nisari'),
(10, 'riya', 'kuzhikkadan house nilamboor p.o malappuram', 'riya123@gmail.com', '1234567895', 'Female', '1999-06-01', 'riya'),
(11, 'appu', 'abcd', 'appu123@gmail.com', '1234567895', 'Male', '1999-05-01', 'appu'),
(12, 'shaji', 'seminivally estate\r\nkottayam', 'shaji@gmail.com', '987654310', 'Male', '5445-04-12', 'shaji'),
(13, 'vindhya', 'Kulathaniyil ,\r\nVallana ,\r\nkuttikkanam P.O,\r\nidukki', 'vindhya@gmail.com', '4561237891', 'Female', '1998-02-21', 'vindhya');
