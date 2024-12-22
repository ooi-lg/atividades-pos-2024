import './style.css';
import { iniPokemons } from './api.js';
import { Pokemons } from './dom.js';

document.querySelector('#app').innerHTML = `
  <div class="container mt-5">
      <h1 class="text-center mb-4">Lista de Pokémon</h1>
      <div class="accordion mt-4" id="pokemon-accordion"></div>
  </div>
`;

async function iniciar() {
    try {
        const pokemons = await iniPokemons();
        await Pokemons(pokemons);
    } catch (error) {
        alert('Não foi possível carregar os Pokémon.');
    }
}

iniciar();
