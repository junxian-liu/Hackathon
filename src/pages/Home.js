import React from 'react';
import '../App.css';
import HomePage from '../Components/HomePage/HomePage';
import Cards from '../Components/Cards/Cards';
import AboutUs from '../Components/AboutUs/AboutUs';
import HowDo from '../Components/HowDo/HowDo';

const Home = () => {
    return (
        <>
            <HomePage />
            <Cards />
            <AboutUs />
            <HowDo />
        </>
    )
}

export default Home;