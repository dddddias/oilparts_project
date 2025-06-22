import { render } from '@testing-library/react';
import App from './App';

jest.mock('axios', () => ({
  create: () => ({ get: jest.fn(() => Promise.resolve({ data: [] })) })
}));

test('renders without crashing', () => {
  render(<App />);
  expect(document.body).toBeInTheDocument();
});
