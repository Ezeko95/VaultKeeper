import { Route, Routes } from "react-router-dom";
import Landing from "./Views/Landing";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />

      <Route path="*" element={<h1>Not Found</h1>} />
    </Routes>
  );
}

export default App;
