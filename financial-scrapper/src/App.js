import logo from './logo.svg';
import './App.css';
import LoginPage from './Components/LoginPage/LoginPage';
import AboutPage from './Components/AboutPage/AboutPage';
import Dashboard from './Components/Dashboard/Dashboard';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/loginpage" element={<LoginPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
