import { useState } from "react";
import Login from "../Components/Login";
import Register from "../Components/Register";
const Landing = () => {
  const [isLogin, setIsLogin] = useState<boolean>(true);

  return (
    <div className="bg-gray-100 flex flex-col items-center justify-center min-h-screen md:py-2">
      <main className="flex items-center w-full px-2 md:px-20 bg-gray-800 p-32">
        <div className="hidden md:inline-flex flex-col flex-1 space-y-1">
          <p className="text-6xl text-blue-500 font-bold">VaultKeeper</p>
          <p className="font-medium text-lg leading-1 text-teal-500">
            Open source password manager for everyone to use and contribute.
            <br></br>
            No ads, no tracking, no strings attached.
          </p>
        </div>
        {isLogin ? <Login isLogin={isLogin} setIsLogin={setIsLogin} /> : <Register isLogin={isLogin} setIsLogin={setIsLogin} />}
      </main>
    </div>
  );
};

export default Landing;
