
import { DetalhePokemon } from './api.js';

export async function Pokemons(pokemons) {
    const addPokemons = document.getElementById('pokemon-accordion');
    addPokemons.innerHTML = '';

    pokemons.forEach((pokemon, index) => {
        const accordionItem = document.createElement('div');
        accordionItem.className = 'accordion-item';

        accordionItem.innerHTML = `
            <h2 class="accordion-header" id="heading-${index}">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-${index}" aria-expanded="false" aria-controls="collapse-${index}">
                    ${pokemon.name}
                </button>
            </h2>
            <div id="collapse-${index}" class="accordion-collapse collapse" aria-labelledby="heading-${index}" data-bs-parent="#pokemon-accordion">
                <div class="accordion-body" id="pokemon-details-${index}">
                    <div class="text-center">Carregando detalhes...</div>
                </div>
            </div>
        `;

        addPokemons.appendChild(accordionItem);

        accordionItem.querySelector('.accordion-button').addEventListener('click', async () => {
            const detailsElement = document.getElementById(`pokemon-details-${index}`);
            if (!detailsElement.classList.contains('loaded')) {
                const pokemonDetails = await DetalhePokemon(pokemon.url);
                buscarDetPokemon(pokemonDetails, index);
            }
        });
    });
}

function buscarDetPokemon(pokemon, index) {
    const abilities = pokemon.abilities.map(ability => `<li>${ability.ability.name} ${ability.is_hidden ? '(Hidden)' : ''}</li>`).join('');
    const detalhes = document.getElementById(`pokemon-details-${index}`);
    
    detalhes.innerHTML = `
        <table cellspacing="1" cellpadding="0" width="43%" class="pokemon-table" style="background: #be7fe2; border: 2px solid #652689; font-size: 12px; color: #000000;">
            <tbody>
                <tr>
                    <td>
                        <table width="100%">
                            <tbody>
                                <tr>
                                    <td align="center" width="30%" style="background: #61bb59; border-right: 1px solid #be7fe2; line-height: 1.6; border-radius: 11px;">
                                        <big><b>Nº ${pokemon.id}</b></big>
                                    </td>
                                    <td align="center" width="70%" style="background: #61bb59; line-height: 1.6; padding: 0.7em; border-radius: 11px;">
                                        <big><b>${pokemon.name}</b></big>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td>
                        <table cellpadding="10" width="100%" style="border: 2px solid #be7fe2; border-radius: 11px;">
                            <tbody>
                                <tr>
                                    <td width="100%" align="center" style="line-height: 1.6;">
                                        <div class="center">
                                            <div class="floatnone">
                                                <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}" class="img-fluid" width="180" height="180"> 
                                            </div>
                                            <br>
                                            <small>Arte de Pokémon</small>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td>
                        <table cellpadding="3" width="100%" style="background: #61bb59; border: 2px solid #be7fe2; border-radius: 11px;">
                            <tbody>
                                <tr>
                                    <td width="100%" colspan="2" align="center" style="line-height: 1.9;">
                                        <big><b>Informações</b></big>
                                    </td>
                                </tr>
                                <tr>
                                    <td width="50%" align="center" style="background: #88e47f; line-height: 1.6;"><span style="color: #498144;"><b>Altura</b></span></td>
                                    <td width="50%" align="center" style="background: #88e47f; line-height: 1.6;"><span style="color: #498144;"><b>Peso</b></span></td>
                                </tr>
                                <tr>
                                    <td class="modoclaroescuro" align="center">${pokemon.height} m</td>
                                    <td class="modoclaroescuro" align="center">${pokemon.weight} kg</td>
                                </tr>
                                <tr>
                                    <td width="100%" colspan="2" align="center" style="background: #88e47f; line-height: 1.6;">
                                        <span style="color: #498144;"><b>Habilidade(s)</b></span>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="modoclaroescuro" colspan="2" align="center">
                                        <table width="100%">
                                            <tbody>
                                                <tr align="center">
                                                    <td width="50%"><p>${abilities}</p></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    `;
    detalhes.classList.add('loaded');
}
