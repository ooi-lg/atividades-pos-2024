// src/App.js
import React from 'react';
import './App.css';
import Artistas from './components/Artistas';
import Albuns from './components/Albuns';
import Musicas from './components/Musicas';

function App() {
  return (
    <div className="App">
      <h1>Spotifake</h1>
      <Artistas />
      <Albuns />
      <Musicas />
    </div>
  );
}

export default App;
