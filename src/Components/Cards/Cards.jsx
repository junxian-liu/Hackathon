import React from 'react';
import './Cards.css';
import CardItem from './CardItems';
import finstock from '../../Assets/finstock.jpg'
import findadv from '../../Assets/finadv.webp'
import simplestocks from '../../Assets/simplestocks.jpg'
import stocksGif from '../../Assets/stocks.gif'

function Cards() {
  return (
    <div id="cardsSection">
        <div className='cards'>
            <h2>FEATURES</h2>
            <h1>What We Provide</h1>
            <div className='cards__container'>
            <div className='cards__wrapper'>
            <ul className='cards__items'>
                <CardItem
                src={finstock}
                text='Time Is Money, We Generate Advanced Financial Reports In Seconds To Help You Make Decisions Quicker And Better.'
                label='Efficiency'
                />
                <CardItem
                src={findadv}
                text='Know What You Are Getting Into. Our Reports Produce Expert Advice On The Stocks YOU Are Interested In.'
                label='Insights'
                />
                <CardItem
                src={simplestocks}
                text='We Hate Complexity. Our Tool Makes Your Statistics Easily Interpretable, Who Said Investing Has To Be Hard?'
                label='Simplicity'
                />
            </ul>
            <div className = "stockGif">
                <img src={stocksGif} alt=''/>
            </div>
            </div>
        </div>
        </div>
    </div>
  );
}

export default Cards;