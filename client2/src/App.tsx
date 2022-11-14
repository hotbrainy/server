import './App.css';
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Welcome from './components/Welcome';
import Hierachy from './components/Hierachy';

function App() {
  return (
    <Router>
		<Routes>
			<Route path="/" element={<Welcome />} />
			<Route path='/hierarchy' element={ <Hierachy /> } />
		</Routes>
    </Router>

  );
}

export default App;
