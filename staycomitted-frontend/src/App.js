import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';
import UserList from './components/UserList';
import CreateUser from './components/CreateUser';
import Goals from './components/Goals';
import Habits from './components/Habits';
import Home from './components/Home';

function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
            <li>
              <Link to="/goals">Goals</Link>
            </li>
            <li>
              <Link to="/habits">Habits</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<div><CreateUser /><UserList /></div>} />
          <Route path="/goals" element={<Goals />} />
          <Route path="/habits" element={<Habits />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
