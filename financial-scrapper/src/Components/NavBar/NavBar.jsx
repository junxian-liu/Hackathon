import React from 'react'
import { Link } from 'react-router-dom'
import './NavBar.css'

export const NavBar = () =>  {
    return (
        <div className = 'navigation'>
            <div className = "title">
                <Link to="/" style={{textDecoration: 'none', color: 'white'}}>FinScrap</Link>
            </div>
            <div className = "navButtons">
                <a href="/features" style={{textDecoration: 'none', color: 'white'}}> Features</a>
                <a href="/about" style={{textDecoration: 'none', color: 'white'}}>About Us</a>
                <a href="https://finance.yahoo.com/" style={{textDecoration: 'none', color: 'white'}}>View Market </a>
            </div>
        </div>
    )
}