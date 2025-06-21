// теперь у нас именно default-экспорт, чтобы
// в компонентах можно было писать:
//
//    import api from '../api'
//
// без фигурных скобок

import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
});

export default api;
