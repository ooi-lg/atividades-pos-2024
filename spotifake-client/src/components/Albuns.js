// src/components/Albuns.js
import React, { useState, useEffect } from 'react';
import { getAlbuns, createAlbum, updateAlbum, deleteAlbum } from '../api';

const Albuns = () => {
  const [albuns, setAlbuns] = useState([]);
  const [nome, setNome] = useState('');
  const [ano, setAno] = useState('');
  const [artistaId, setArtistaId] = useState('');
  const [editing, setEditing] = useState(false);
  const [currentAlbum, setCurrentAlbum] = useState(null);

  // Fetch albuns
  useEffect(() => {
    const fetchAlbuns = async () => {
      const response = await getAlbuns();
      setAlbuns(response.data);
    };
    fetchAlbuns();
  }, []);

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (editing) {
      await updateAlbum(currentAlbum.id, { nome, ano, artista: artistaId });
      setEditing(false);
      setCurrentAlbum(null);
    } else {
      const newAlbum = { nome, ano, artista: artistaId };
      await createAlbum(newAlbum);
    }
    setNome('');
    setAno('');
    setArtistaId('');
    const response = await getAlbuns();
    setAlbuns(response.data);
  };

  // Handle edit
  const handleEdit = (album) => {
    setEditing(true);
    setNome(album.nome);
    setAno(album.ano);
    setArtistaId(album.artista);
    setCurrentAlbum(album);
  };

  // Handle delete
  const handleDelete = async (id) => {
    await deleteAlbum(id);
    const response = await getAlbuns();
    setAlbuns(response.data);
  };

  return (
    <div>
      <h2>Álbuns</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Nome do Álbum"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />
        <input
          type="number"
          placeholder="Ano"
          value={ano}
          onChange={(e) => setAno(e.target.value)}
        />
        <input
          type="number"
          placeholder="ID do Artista"
          value={artistaId}
          onChange={(e) => setArtistaId(e.target.value)}
        />
        <button type="submit">{editing ? 'Atualizar Álbum' : 'Adicionar Álbum'}</button>
      </form>

      <ul>
        {albuns.map((album) => (
          <li key={album.id}>
            {album.nome} - {album.ano} - Artista ID: {album.artista}
            <button onClick={() => handleEdit(album)}>Editar</button>
            <button onClick={() => handleDelete(album.id)}>Excluir</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Albuns;
