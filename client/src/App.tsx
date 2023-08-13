import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Landing from "./Views/Landing/Landing";
import Vault from "./Views/Vault/Vault";

const App: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />

      <Route path="/vault" element={<Vault />} />

      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
};

export default App;
