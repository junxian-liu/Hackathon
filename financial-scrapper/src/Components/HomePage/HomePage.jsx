import React from 'react'
import { Link } from 'react-router-dom'
import './HomePage.css' 
import stocksvid from "../../Assets/stockhome.mp4"

const HomePage = () => {
    return (
        <div className = 'container'>
            <video src={stocksvid} autoPlay loop muted />
            <h1> Financial Investments Simplified </h1>
            <p> Reports generated through a simple touch.</p>
            <a href="/dashboard" style={{textDecoration: 'none'}}> GET STARTED </a>
        </div>
    )
}

export default HomePage;