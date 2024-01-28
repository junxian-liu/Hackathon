import logo from './logo.svg';
import './App.css';
import { useRef } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { NavBar } from './Components/NavBar/NavBar'
import './App.css'
import Home from './pages/Home'
import Cards from './Components/Cards/Cards'
import AboutUs from './Components/AboutUs/AboutUs'

function App() {
  return (
    <div>
      <BrowserRouter>
      <NavBar />
      <div>
        <Routes>
          <Route path= '/'
          element={<Home />}
          />
          <Route path= '/features'
          element={<Cards />}
          />
          <Route path= '/about'
          element={<AboutUs />}
          />
        </Routes>
      </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
