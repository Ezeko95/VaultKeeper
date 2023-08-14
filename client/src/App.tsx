import { Route, Routes } from "react-router-dom";
import Landing from "./Views/Landing";
import Vault from "./Views/Vault";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />

      <Route path="/vault" element={<Vault />} />

      <Route path="*" element={<h1>Not Found</h1>} />
    </Routes>
  );
}

export default App;
