import React from 'react'
import { Link } from 'react-router-dom'
import './NavBar.css'

export const NavBar = () =>  {
    return (
        <div className = 'navigation'>
            <div className = "title">
                <Link to="/" style={{textDecoration: 'none', color: '#F9F6EE'}}>FinScrap</Link>
            </div>
            <div className = "navButtons">
                <a href="/features" style={{textDecoration: 'none', color: '#F9F6EE'}}> Features</a>
                <a href="/about" style={{textDecoration: 'none', color: '#F9F6EE'}}>About Us</a>
                <a href="https://finance.yahoo.com/" style={{textDecoration: 'none', color: '#F9F6EE'}}>View Market </a>
            </div>
        </div>
    )
}