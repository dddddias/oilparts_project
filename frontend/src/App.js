import { BrowserRouter, Routes, Route } from 'react-router-dom'
import CatalogPage  from './pages/CatalogPage'
import OrderPage    from './pages/OrderPage'
import DiagramPage  from './pages/DiagramPage'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/"        element={<CatalogPage />} />
        <Route path="/order"   element={<OrderPage   />} />
        <Route path="/diagram" element={<DiagramPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
