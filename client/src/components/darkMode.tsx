import React, { useState } from "react";
import sunIcon from "../../public/sun.svg"
import moonIcon from "../../public/dark.svg";

const DarkModeToggle: React.FC = () => {
  const [darkMode, setDarkMode] = useState(false);

  const toggleDarkMode = () => {
    document.documentElement.classList.toggle("dark");
    setDarkMode(!darkMode);
  };

  return (
    <div className="dark-mode-toggle" onClick={toggleDarkMode}>
      {darkMode ? (
        <img src={moonIcon} alt="Moon Icon" width={36} height={36} />
      ) : (
        <img src={sunIcon} alt="Sun Icon" width={36} height={36} />
      )}
    </div>
  );
};

export default DarkModeToggle;
