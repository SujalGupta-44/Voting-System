-- Create Database
CREATE DATABASE IF NOT EXISTS VotingSystem;
USE VotingSystem;

-- Drop tables if they exist 
DROP TABLE IF EXISTS votes;
DROP TABLE IF EXISTS myuser;

-- Create User Table
CREATE TABLE myuser (
    aadhar DOUBLE PRIMARY KEY,
    name TEXT,
    fathername TEXT,
    age INT,
    city TEXT,
    password TEXT,
    pincode INT,
    address TEXT,
    mobileno DOUBLE
);

-- Create Votes Table
CREATE TABLE votes (
    party_name VARCHAR(50) PRIMARY KEY,
    vote_count INT DEFAULT 0
);

-- Insert parties into votes table
INSERT INTO votes (party_name, vote_count) VALUES
('BJP', 0),
('CONG', 0),
('BSP', 0),
('SP', 0),
('AAP', 0),
('TDP', 0);
