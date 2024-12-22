
export async function iniPokemons() {
    try {
        const url = 'https://pokeapi.co/api/v2/pokemon?limit=10';
        const response = await fetch(url);
        const data = await response.json();
        return data.results;
    } catch (error) {
        console.error('Erro ao buscar os Pokémon:', error);
        throw error; 
    }
}

export async function DetalhePokemon(url) {
    try {
        const response = await fetch(url);
        return await response.json();
    } catch (error) {
        console.error('Erro ao carregar os detalhes do Pokémon:', error);
        throw error; 
    }
}
