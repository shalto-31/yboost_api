import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Layout from "./Components/Layout";
import Home from "./Pages/Home";
import Liste from "./Pages/Liste";
import PageNotFound from "./Pages/PageNotFound";



function App() {
  return (
    <BrowserRouter>
      <div className="flex min-h-screen flex-col bg-[#192037] p-8">
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="/Liste" element={<Liste />} />
            <Route path="*" element={<PageNotFound />} />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
