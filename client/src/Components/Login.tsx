import { useState } from "react";
import axios from "axios";
import { setCookie } from "typescript-cookie";

interface LoginProps {
  isLogin: boolean;
  setIsLogin: React.Dispatch<React.SetStateAction<boolean>>;
}

const Login: React.FC<LoginProps> = ({ setIsLogin }) => {
  const [loginForm, setLoginForm] = useState({
    email: "",
    password: "",
  });

  const loginHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    setLoginForm({ ...loginForm, [e.target.name]: e.target.value });
  };

  const handleFormSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const res = await axios.post("/auth/user_login", loginForm);
      setCookie("token", res.data.token);
      setIsLogin(true);
    } catch (error) {
      console.log("Error:", error);
    }
  };

  return (
    <div className="bg-slate-600 rounded-2xl shadow-2xl flex flex-col w-full md:w-1/3 items-center max-w-4xl transition duration-1000 ease-out">
      <h2 className="p-3 text-3xl font-bold text-blue-500">VaultKeeper</h2>
      <div className="inline-block border-[1px] justify-center w-20 border-teal-500 border-solid"></div>
      <h3 className="text-xl font-semibold text-teal-500 pt-2">Sign In!</h3>
      {/* Inputs */}
      <form onSubmit={handleFormSubmit}>
        <div className="flex flex-col items-center justify-center">
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Email"
            value={loginForm.email}
            onChange={loginHandler}
            className="rounded-2xl px-2 py-1 w-4/5 md:w-full border-[1px] border-blue-400 m-1 "
          />
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Password"
            value={loginForm.password}
            onChange={loginHandler}
            className="rounded-2xl px-2 py-1 w-4/5 md:w-full border-[1px] border-blue-400 m-1 focus:shadow-md focus:border-pink-400 focus:outline-none focus:ring-0"
          />
          <button
            type="submit"
            className="rounded-2xl m-2 text-white bg-teal-500 w-2/5 px-4 py-2 shadow-md hover:text-teal-500 hover:bg-white transition duration-200 ease-in"
          >
            Sign In
          </button>
        </div>
      </form>
      <div className="inline-block border-[1px] justify-center w-20 border-blue-400 border-solid mt-2"></div>
      <p className="text-blue-400 mt-4 text-sm">Don't have an account?</p>
      <p
        className="text-teal-500 mb-4 text-sm font-medium cursor-pointer bg-white mt-2 pl-3 pr-3 pt-1 pb-1 rounded hover:text-white hover:bg-teal-500 transition duration-200 ease-in"
        onClick={() => setIsLogin(false)}
      >
        Create a New Account?
      </p>
    </div>
  );
};

export default Login;
