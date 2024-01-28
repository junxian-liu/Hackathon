import React from 'react'
import { Link } from 'react-router-dom'
import './AboutPage.css' 


const AboutPage = () => {
  return (
    <div className="container">
      <h1>About FinScrap</h1>

      <section>
        <h2>Who We Are</h2>
        <p>
          FinScrap is more than just a financial analysis platform; we're a team
          of passionate college students from the University of California, San
          Diego (UCSD), driven by the mission to empower individuals with the
          tools and insights needed to make informed decisions in the world of
          stock investments.
        </p>
      </section>

      <section>
        <h2>Our Mission</h2>
        <p>
          At FinScrap, we recognize the challenges individuals face when
          navigating the complexities of the stock market. Our mission is to
          simplify the investment process and provide users with reliable,
          data-driven insights. We believe that everyone deserves access to the
          information needed to make educated decisions about their financial
          future.
        </p>
      </section>

      <section>
        <h2>How We Do It</h2>
        <div className="team-section">
          <h3>Financial Report Analysis</h3>
          <p>
            Our platform specializes in analyzing financial reports to assess
            the current state of various stocks. Leveraging cutting-edge
            technology and methodologies, we sift through extensive financial
            data to identify trends, potential risks, and promising
            opportunities.
          </p>
        </div>

        <div className="team-section">
          <h3>User-Friendly Interface</h3>
          <p>
            We understand that not everyone has a background in finance, so
            we've designed an intuitive and user-friendly interface. Whether
            you're a seasoned investor or just starting, FinScrap provides a
            seamless experience, allowing you to explore financial analyses with
            ease.
          </p>
        </div>
      </section>

      <section>
        <h2>Meet the Team</h2>
        <div className="team-member">
          <img
            src="https://placekitten.com/100/100"
            alt="Team Member 1"
            className="team-member-img"
          />
          <div>
            <h3>John Doe</h3>
            <p>Co-founder | Finance Enthusiast</p>
          </div>
        </div>

        <div className="team-member">
          <img
            src="https://placekitten.com/100/101"
            alt="Team Member 2"
            className="team-member-img"
          />
          <div>
            <h3>Jane Smith</h3>
            <p>Co-founder | Tech Geek</p>
          </div>
        </div>
        {/* Add more team members as needed */}
      </section>
    </div>
  );
};

export default AboutPage;