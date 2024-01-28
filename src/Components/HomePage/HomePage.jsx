import React, { useState, useEffect, useRef } from 'react'
import { Link } from 'react-router-dom'
import './HomePage.css' 
import stocksvid from "../../Assets/stockhome2.mov"
import ucsd from "../../Assets/ucsd.png"
import lpl from "../../Assets/lpl.png"

const wordArray = ['Wherever', 'Whoever', 'Whenever'];

const HomePage = () => {
    const [currWord, setCurrWord] = useState(wordArray[0]);
	const [isActive, setIsActive] = useState(true);

	const index = useRef(0);
	useEffect(() => {
		let interval = null;
		if (isActive) {
			interval = setInterval(() => {
                setCurrWord(wordArray[index.current]);
				index.current++;
				if (index.current === wordArray.length) {
					index.current = 0;
				}
			}, 1000);
		}
		return () => clearInterval(interval);
	});

    return (
        <div id="homeSection">
            <div className = 'container'>
                <video src={stocksvid} autoPlay loop muted />
                <h1> Search and Discover on FinScrap </h1>
                <h2>{currWord}</h2>
                <p>Unlock finance reports on your favorite stocks listed on NASDAQ instantly, no registration required.</p>
                <a href="/dashboard" style={{textDecoration: 'none'}}> GET STARTED </a>
                
                <div className = "bottom-text">
                    <p>Presented By</p>
                </div>
                <div className="ucsd_logo">
                <a href="https://ucsd.edu/" style={{textDecoration: 'none', color: '#F9F6EE'}}><img src={ucsd} alt=""/></a>
                </div>
                <div className="lpl_logo">
                    <img src={lpl} alt=""/>
                    <a href="https://www.lpl.com/" style={{textDecoration: 'none', color: '#F9F6EE'}}><img src={lpl} alt=""/></a>
                </div>
            </div>
        </div>
    )
}

export default HomePage;