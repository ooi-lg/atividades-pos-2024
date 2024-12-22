// src/components/Musicas.js
import React, { useState, useEffect } from 'react';
import { getMusicas, createMusica, updateMusica, deleteMusica } from '../api';

const Musicas = () => {
  const [musicas, setMusicas] = useState([]);
  const [nome, setNome] = useState('');
  const [segundos, setSegundos] = useState('');
  const [albumId, setAlbumId] = useState('');
  const [editing, setEditing] = useState(false);
  const [currentMusica, setCurrentMusica] = useState(null);

  // Fetch musicas
  useEffect(() => {
    const fetchMusicas = async () => {
      const response = await getMusicas();
      setMusicas(response.data);
    };
    fetchMusicas();
  }, []);

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (editing) {
      await updateMusica(currentMusica.id, { nome, segundos, album: albumId });
      setEditing(false);
      setCurrentMusica(null);
    } else {
      const newMusica = { nome, segundos, album: albumId };
      await createMusica(newMusica);
    }
    setNome('');
    setSegundos('');
    setAlbumId('');
    const response = await getMusicas();
    setMusicas(response.data);
  };

  // Handle edit
  const handleEdit = (musica) => {
    setEditing(true);
    setNome(musica.nome);
    setSegundos(musica.segundos);
    setAlbumId(musica.album);
    setCurrentMusica(musica);
  };

  // Handle delete
  const handleDelete = async (id) => {
    await deleteMusica(id);
    const response = await getMusicas();
    setMusicas(response.data);
  };

  return (
    <div>
      <h2>Músicas</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Nome da Música"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />
        <input
          type="number"
          placeholder="Segundos"
          value={segundos}
          onChange={(e) => setSegundos(e.target.value)}
        />
        <input
          type="number"
          placeholder="ID do Álbum"
          value={albumId}
          onChange={(e) => setAlbumId(e.target.value)}
        />
        <button type="submit">{editing ? 'Atualizar Música' : 'Adicionar Música'}</button>
      </form>

      <ul>
        {musicas.map((musica) => (
          <li key={musica.id}>
            {musica.nome} - {musica.segundos} segundos - Álbum ID: {musica.album}
            <button onClick={() => handleEdit(musica)}>Editar</button>
            <button onClick={() => handleDelete(musica.id)}>Excluir</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Musicas;
