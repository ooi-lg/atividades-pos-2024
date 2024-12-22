import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Funções CRUD para Artistas
export const getArtistas = () => api.get('artistas/');
export const createArtista = (data) => api.post('artistas/', data);
export const updateArtista = (id, data) => api.put(`artistas/${id}/`, data);
export const deleteArtista = (id) => api.delete(`artistas/${id}/`);

// Funções CRUD para Álbuns
export const getAlbuns = () => api.get('albuns/');
export const createAlbum = (data) => api.post('albuns/', data);
export const updateAlbum = (id, data) => api.put(`albuns/${id}/`, data);
export const deleteAlbum = (id) => api.delete(`albuns/${id}/`);

// Funções CRUD para Músicas
export const getMusicas = () => api.get('musicas/');
export const createMusica = (data) => api.post('musicas/', data);
export const updateMusica = (id, data) => api.put(`musicas/${id}/`, data);
export const deleteMusica = (id) => api.delete(`musicas/${id}/`);