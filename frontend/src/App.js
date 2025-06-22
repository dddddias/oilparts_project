import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import CatalogPage from './pages/CatalogPage'
import OrderPage from './pages/OrderPage'
import DiagramPage from './pages/DiagramPage'

const router = createBrowserRouter([
  { path: "/", element: <CatalogPage /> },
  { path: "/order", element: <OrderPage /> },
  { path: "/diagram", element: <DiagramPage /> }
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App
