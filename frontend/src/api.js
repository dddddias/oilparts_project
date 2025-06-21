// frontend/src/api.js
import axios from 'axios';

const api = axios.create({
  // т.к. в package.json прописан "proxy": "http://localhost:8000",
  // все запросы к /parts, /hotzones и т. д. автоматически пойдут на бэкенд
  baseURL: '/',
  // при необходимости можете добавить здесь общие заголовки:
  // headers: { 'Content-Type': 'application/json' },
});

export default api;
