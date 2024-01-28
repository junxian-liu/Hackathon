import React from 'react'
import { Link } from 'react-router-dom'
import './NavBar.css'
import { Link as ScrollLink, animateScroll as scroll } from 'react-scroll';


export const NavBar = () =>  {
    return (
        <div className = 'navigation'>
            <div className = "title">
                <ScrollLink to="homeSection" smooth={true} duration={1000} offset={-100}>FinScrap</ScrollLink>
            </div>
            <div className = "navButtons">
                <ScrollLink to="cardsSection" smooth={true} duration={1000} offset={-80}>Features</ScrollLink>
                <ScrollLink to="aboutSection" smooth={true} duration={1000} offset={-100}>About Us</ScrollLink>
                <a href="https://finance.yahoo.com/" style={{textDecoration: 'none', color: '#F9F6EE'}}>View Market </a>
            </div>
        </div>
    )
}