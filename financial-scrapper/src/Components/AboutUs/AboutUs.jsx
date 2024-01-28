import React from 'react';
import './AboutUs.css';
import { useState } from "react";

function AboutUs() {
    const [slots] = useState([
        {
            title: 'Who We Are',
            text: 'FinScrap is more than just a financial analysis platform; we are a team of passionate college students from the University of California - San Diego, driven by the mission to empower individuals with the tools and insights needed to make informed decisions in the world of stock investments.',
        },
        {
            title: 'Field Diversity',
            text: 'Our Team composes of students of different fields, each with their own unique set of knowledge of the industry to produce insights of different stock sectors.  ',
        },
        {
            title: 'Our Mission',
            text: 'At FinScrap, we recognize the challenges individuals face when navigating the complexities of the stock market. Our mission is to simplify the investment process and provide users with reliable, data-driven insights. We believe that everyone deserves access to the information needed to make educated decisions about their financial future.',
        }
    ])
  return (
    <div id="aboutSection">
        <div className='aboutcard'>
            <h1>About Us</h1>
            <div className='slots'>
                {
                    slots.map((card, i) => (
                        <div key={i} className ='slot'>
                            <h3>{ card.title }</h3>
                            <p>{ card.text }</p>
                        </div>
                    ))
                }
            </div>
        </div>
    </div>
  );
}

export default AboutUs;