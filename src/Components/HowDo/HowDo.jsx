import React from 'react';
import './HowDo.css';
import { useState } from "react";
import bullStocks from '../../Assets/bullstocks.gif'

function HowDo() {
    const [parkings] = useState([
        {
            title: 'Financial Report Analysis',
            text: 'Our platform specializes in analyzing financial reports to assess the current state of various stocks. Leveraging cutting-edge technology and methodologies, we sift through extensive financial data to identify trends, potential risks, and promising opportunities.',
        },
        {
            title: 'User-Friendly Interface',
            text: 'We understand that not everyone has a background in finance, so we have designed an intuitive and user-friendly interface. Whether you are a seasoned investor or just starting, FinScrap provides a seamless experience, allowing you to explore financial analyses with ease.',
        },
        {
            title: 'Free Usage',
            text: 'We do not require signups to use our platform, everyone should have unrestricted access to financial information, at least that is what we believe in. Enjoy free public access to our tool in seconds upon entering our domain.',
        }
    ])
  return (
    <div className='howcard'>
        <h1>How We Do It</h1>
        <div className='parkings'>
            {
                parkings.map((parking, i) => (
                    <div key={i} className ='parking'>
                        <h3>{ parking.title }</h3>
                        <p>{ parking.text }</p>
                    </div>
                ))
            }
        </div>
        <div className = "copyright">
                <p> Ⓒ2024 FinScrap. No Rights Reserved. </p>
        </div>
        <div className = "bullStocks">
                <img src={bullStocks} alt=''/>
        </div>
    </div>
  );
}

export default HowDo;