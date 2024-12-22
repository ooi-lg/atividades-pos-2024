// src/components/Artistas.js
import React, { useState, useEffect } from 'react';
import { getArtistas, createArtista, updateArtista, deleteArtista } from '../api';

const Artistas = () => {
  const [artistas, setArtistas] = useState([]);
  const [nome, setNome] = useState('');
  const [local, setLocal] = useState('');
  const [anoCriacao, setAnoCriacao] = useState('');
  const [editing, setEditing] = useState(false);
  const [currentArtista, setCurrentArtista] = useState(null);

  // Fetch artistas
  useEffect(() => {
    const fetchArtistas = async () => {
      const response = await getArtistas();
      setArtistas(response.data);
    };
    fetchArtistas();
  }, []);

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (editing) {
      await updateArtista(currentArtista.id, { nome, local, ano_criacao: anoCriacao });
      setEditing(false);
      setCurrentArtista(null);
    } else {
      const newArtista = { nome, local, ano_criacao: anoCriacao };
      await createArtista(newArtista);
    }
    setNome('');
    setLocal('');
    setAnoCriacao('');
    const response = await getArtistas();
    setArtistas(response.data);
  };

  // Handle edit
  const handleEdit = (artista) => {
    setEditing(true);
    setNome(artista.nome);
    setLocal(artista.local);
    setAnoCriacao(artista.ano_criacao);
    setCurrentArtista(artista);
  };

  // Handle delete
  const handleDelete = async (id) => {
    await deleteArtista(id);
    const response = await getArtistas();
    setArtistas(response.data);
  };

  return (
    <div>
      <h2>Artistas</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Nome do Artista"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />
        <input
          type="text"
          placeholder="Local de Origem"
          value={local}
          onChange={(e) => setLocal(e.target.value)}
        />
        <input
          type="number"
          placeholder="Ano de Criação"
          value={anoCriacao}
          onChange={(e) => setAnoCriacao(e.target.value)}
        />
        <button type="submit">{editing ? 'Atualizar Artista' : 'Adicionar Artista'}</button>
      </form>

      <ul>
        {artistas.map((artista) => (
          <li key={artista.id}>
            {artista.nome} - {artista.local} - {artista.ano_criacao}
            <button onClick={() => handleEdit(artista)}>Editar</button>
            <button onClick={() => handleDelete(artista.id)}>Excluir</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Artistas;
