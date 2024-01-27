import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { NavBar } from './Components/NavBar/NavBar'
import './App.css'
import Home from './pages/Home'

function App() {
  return (
    <div>
      <BrowserRouter>
      <NavBar/>
      <div>
        <Routes>
          <Route path= '/'
          element={<Home />}
          />
        </Routes>
      </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
