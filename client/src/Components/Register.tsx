import { useState } from "react";
import axios from "axios";

interface LoginProps {
  isLogin: boolean;
  setIsLogin: React.Dispatch<React.SetStateAction<boolean>>;
}

const Register: React.FC<LoginProps> = ({ setIsLogin }) => {
  const [registerForm, setRegisterForm] = useState({
    email: "",
    password: "",
    username: "",
  });
  const registerHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    setRegisterForm({ ...registerForm, [e.target.name]: e.target.value });
  };

  const handleFormSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const res = await axios.post("auth/user_register", registerForm);
      console.log(res);
      setIsLogin(true);
    } catch (error) {
      console.log("Error:", error);
    }
  };

  return (
    <div className="bg-slate-600 text-white rounded-2xl shadow-2xl  flex flex-col w-full  md:w-1/3 items-center max-w-4xl transition duration-1000 ease-in">
      <h2 className="p-3 text-3xl font-bold text-teal-500">VaultKeeper</h2>
      <div className="inline-block border-[1px] justify-center w-20 border-blue-400 border-solid"></div>
      <h3 className="text-xl font-semibold text-blue-400 pt-2">
        Create Account!
      </h3>
      {/* Inputs */}
      <form onSubmit={handleFormSubmit}>
        <div className="flex flex-col items-center justify-center mt-2">
          <input
            type="username"
            id="username"
            name="username"
            onChange={registerHandler}
            value={registerForm.username}
            className="rounded-2xl px-2 py-1 w-4/5 md:w-full text-black border-[1px] border-blue-400 m-1 focus:shadow-md focus:border-pink-400 focus:outline-none focus:ring-0"
            placeholder="username"
          ></input>
          <input
            type="email"
            id="email"
            name="email"
            onChange={registerHandler}
            value={registerForm.email}
            className="rounded-2xl px-2 py-1 w-4/5 md:w-full border-[1px] text-black border-blue-400 m-1 focus:shadow-md focus:border-pink-400 focus:outline-none focus:ring-0"
            placeholder="Email"
          ></input>
          <input
            type="password"
            id="password"
            name="password"
            onChange={registerHandler}
            value={registerForm.password}
            className="rounded-2xl px-2 py-1 w-4/5 md:w-full border-[1px] text-black border-blue-400 m-1 focus:shadow-md focus:border-pink-400 focus:outline-none focus:ring-0"
            placeholder="Password"
          ></input>

          <button
            type="submit"
            className="rounded-2xl m-4 text-teal-500 bg-white w-3/5 px-4 py-2 shadow-md hover:text-white hover:bg-teal-500 transition duration-200 ease-in"
          >
            Sign Up
          </button>
        </div>
      </form>
      <div className="inline-block border-[1px] justify-center w-20 border-white border-solid"></div>
      <p className="text-white mt-4 text-sm">Already have an account?</p>
      <p
        className="text-teal-500 mb-4 text-sm font-medium cursor-pointer bg-white mt-2 pl-3 pr-3 pt-1 pb-1 rounded hover:text-white hover:bg-teal-500 transition duration-200 ease-in"
        onClick={() => setIsLogin(true)}
      >
        Sign In to your Account?
      </p>
    </div>
  );
};

export default Register;
